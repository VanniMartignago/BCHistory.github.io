# Source scan archive

Use [url_scansionati.txt](url_scansionati.txt) to avoid scanning the same pages again. The file contains one canonical URL per line.

1. Before opening an index, article, or linked reference, normalize the URL and check for an exact line match. For example, run `rg -Fx -- "$url" archivio_fonti/url_scansionati.txt`. Skip matching URLs unless the user asks to rescan them.
2. Remove tracking parameters and heading fragments, preserve query parameters that select content or pagination, and use the English Microsoft Learn URL for localized copies of the same article. When a redirect is known, check the final URL.
3. Add the final canonical URL after reviewing the page, even when it yields no feature. Keep entries unique. Each index page and linked article has its own entry. Pages only discovered, opened without a confirmed scan, or inaccessible remain eligible for review.

The initial list was imported from the V100 [historical register](registro.jsonl), using entries marked `scanned`. Maintain the URL list for future scans. During routine updates, look up only the URL being checked and consult the historical log only on explicit user request.

Historical evidence references to `Checkpoint_aggiornamento_2026-11-19.md` can be resolved against the [archived checkpoint in Git history](https://github.com/VanniMartignago/BCHistory.github.io/blob/c92f9c069301e370456f526e3a61b15f6b3295e7/Checkpoint_aggiornamento_2026-11-19.md).
