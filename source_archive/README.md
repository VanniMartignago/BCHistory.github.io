# Source scan archive

Use [scanned_urls.json](scanned_urls.json) as the current register. Each entry represents one canonical URL.

## Resume a research session

Start with the pending queues. Open URLs awaiting a first attempt, complete outstanding evidence reviews using saved content where possible, and give first failures their second attempt. Skip processed, dead, and excluded URLs. Once the queues are empty, revisit the approved primary and complementary source indexes as needed to discover new material. Check every discovered canonical URL against the register before opening it.

## Discover URLs and record them

Before recording or opening an index, article, or linked reference, normalize it and match the `url` field exactly. Remove tracking parameters and heading fragments, preserve parameters that select content or pagination, and use the English Microsoft Learn URL for localized copies of the same article. When a redirect is known, check the final URL too. Keep one record per canonical URL.

Record relevant new URLs from approved sources as soon as they are discovered, including archive pages, pagination, articles, and official references. Set `status` to `retry` and leave `scanDate` and `lastAttemptDate` as `null` until you have evidence for those dates. Identify the parent page in `scope` when available. Apply the project's source approval rules before adding a new source.

## Open URLs and verify the evidence

Use the register to resume pending work. Compare retrieved content with the catalog and confirm the change and version before updating a feature.

| Status | Action |
| --- | --- |
| `processed` | Reuse the completed review for its recorded scope. Skip it in ordinary scans. |
| `retry` | Open a discovered URL or continue the remaining review of a page already opened. |
| `error` | Keep it in the queue after the first failed attempt. Retry once during a later scan. |
| `dead` | Two access attempts failed. Keep the record and skip the URL in future scans. |
| `excluded` | Record the evidence for confirmed inactivity, such as HTTP 410 Gone. Reopen only on explicit request. |

Use ISO dates (`YYYY-MM-DD`). Update `lastAttemptDate` when you attempt access and `scanDate` when you complete a review, including reviews that yield no feature. Keep unknown dates as `null`. Record the HTTP status or error details when available. Record failed attempts in `accessFailures`. A legacy `error` without a count is treated as one recorded failure. A successful retry returns the URL to content review. Preserve any earlier completed findings. If a page is fully reviewed and work remains on child pages, retain the parent's completed status and track the children separately. Record outstanding feature verification in the project checkpoint.

## List pending URLs

From the repository root, run the following commands. The lists are generated directly from the register and show the most recently registered entries first within each group.

| Command | Result |
| --- | --- |
| `python source_archive/pending_urls.py errors` | URLs that are eligible for a second access attempt. |
| `python source_archive/pending_urls.py unopened` | URLs registered for the first time or with no documented access attempt. |
| `python source_archive/pending_urls.py review` | URLs with a documented access attempt whose content or feature evidence still needs review. |
| `python source_archive/pending_urls.py --counts` | Totals for all three groups. |

Omit the group to print all three pending queues. Archived URLs are omitted. To save one list, redirect its output to a text file. Update the register after each batch so the next run reflects the current state.

Use `--record-access failure --url <canonical-url> --date YYYY-MM-DD` after an access failure, with `--http-status` when known. Use `--record-access success` with the same arguments after accessing a pending page. Record the review scope and mark the entry `processed` after evaluating the feature evidence.

From the project root, load the register locally and emit only the requested entry. Reuse the loaded register for other lookups in the same shell and reload it after updates.

```powershell
$canonicalUrl = 'https://example.com/article'
$register = Get-Content -LiteralPath source_archive/scanned_urls.json -Raw | ConvertFrom-Json
$register | Where-Object { $_.url -ceq $canonicalUrl } | ConvertTo-Json
```

The initial JSON preserves the processed URLs from the previous list and imports dates and access outcomes from the V100 [historical register](historical_register.jsonl). Use the JSON for routine lookups and consult the historical register only on explicit user request.
Historical evidence references to `Checkpoint_aggiornamento_2026-11-19.md` can be resolved against the [archived checkpoint in Git history](https://github.com/VanniMartignago/BCHistory.github.io/blob/c92f9c069301e370456f526e3a61b15f6b3295e7/Checkpoint_aggiornamento_2026-11-19.md).
