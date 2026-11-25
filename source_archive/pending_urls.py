"""List pending source reviews or show recorded access failures."""

import argparse
import json
from datetime import date
from tempfile import NamedTemporaryFile
from pathlib import Path


def queues(register):
    result = {"errors": [], "unopened": [], "review": []}
    for record in reversed(register):
        status = record["status"]
        if status in {"processed", "excluded", "dead"}:
            continue
        if status == "error":
            result["errors"].append(record["url"])
        elif status == "retry":
            queue = "review" if record.get("lastAttemptDate") else "unopened"
            result[queue].append(record["url"])
    return result


def record_access(record, outcome, attempt_date, http_status):
    if record["status"] in {"processed", "excluded", "dead"}:
        raise ValueError("This URL is archived.")
    if outcome == "failure":
        failures = record.get("accessFailures", int(record["status"] == "error")) + 1
        record["accessFailures"] = failures
        record["status"] = "dead" if failures >= 2 else "error"
    else:
        if record["status"] == "error":
            record.setdefault("accessFailures", 1)
        record["status"] = "retry"
    record["lastAttemptDate"] = attempt_date.isoformat()
    if http_status is None:
        record.pop("httpStatus", None)
    else:
        record["httpStatus"] = http_status


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("queue", nargs="?", choices=("errors", "unopened", "review"))
    parser.add_argument("--counts", action="store_true", help="Show totals without listing URLs.")
    parser.add_argument("--record-access", choices=("failure", "success"))
    parser.add_argument("--url", help="Exact canonical URL already in the register.")
    parser.add_argument("--date", type=date.fromisoformat, help="Actual access date (YYYY-MM-DD).")
    parser.add_argument("--http-status", type=int)
    args = parser.parse_args()

    register_path = Path(__file__).with_name("scanned_urls.json")
    register = json.loads(register_path.read_text(encoding="utf-8"))
    if args.record_access:
        if not args.url or not args.date or args.queue or args.counts:
            parser.error("--record-access requires --url and --date and cannot list queues")
        matches = [entry for entry in register if entry["url"] == args.url]
        if len(matches) != 1:
            parser.error("expected one exact canonical URL in the register")
        try:
            record_access(matches[0], args.record_access, args.date, args.http_status)
        except ValueError as error:
            parser.error(str(error))
        with NamedTemporaryFile(mode="w", encoding="utf-8", dir=register_path.parent, delete=False) as file:
            updated_path = Path(file.name)
            json.dump(register, file, ensure_ascii=False, indent=2)
            file.write("\n")
        updated_path.chmod(register_path.stat().st_mode & 0o777)
        updated_path.replace(register_path)
        print(matches[0]["status"])
        return
    if args.url or args.date or args.http_status is not None:
        parser.error("--url, --date and --http-status require --record-access")
    pending = queues(register)

    if args.counts:
        for name, urls in pending.items():
            if args.queue is None or name == args.queue:
                print(f"{name}: {len(urls)}")
        return

    if args.queue:
        for url in pending[args.queue]:
            print(url)
        return

    for name in ("unopened", "review", "errors"):
        urls = pending[name]
        print(f"## {name} ({len(urls)})")
        for url in urls:
            print(url)


if __name__ == "__main__":
    main()
