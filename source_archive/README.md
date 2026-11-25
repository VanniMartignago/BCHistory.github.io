# Source scan archive

Use [scanned_urls.json](scanned_urls.json) as the current register. Each entry represents one canonical URL.

1. Before opening an index, article, or linked reference, normalize the URL and match the `url` field exactly. Remove tracking parameters and heading fragments, preserve query parameters that select content or pagination, and use the English Microsoft Learn URL for localized copies of the same article. When a redirect is known, check the final URL.
2. Open URLs absent from the register when relevant. For registered URLs, use the status to decide whether to open the page.

   | Status | Action |
   | --- | --- |
   | `processed` | The review was completed for the recorded scope. Reuse its findings. Reopen for a distinct pending scope only when saved evidence is insufficient, or when explicitly asked to rescan. |
   | `retry` | The URL was discovered, retrieved, or partially reviewed. Continue its outstanding work when relevant. |
   | `error` | An access attempt failed. Retry when relevant. A single 404 remains an error. |
   | `excluded` | Evidence confirms that the URL is inactive, such as HTTP 410 Gone. Record the reason and reopen only on explicit request. |

3. Keep one entry per URL. Set `scanDate` to the latest documented completed review and `lastAttemptDate` to the latest documented access attempt. Use ISO dates (`YYYY-MM-DD`) and keep unknown dates as `null`. Record completed reviews even when they yield no feature. Record HTTP status or error details when available, and set `scope` on the URL entry to describe what the recorded status covers. Use `null` when the scope is unknown. Record relevant child URLs as separate entries, including subsequent index pages, articles, and official references. Keep a partially reviewed URL at `retry` while work on that page remains. If the page review is complete and the remaining work is on a child URL, keep the child pending and retain the parent status. Track outstanding feature verification and archive coverage in the project checkpoint.

From the project root, load the register locally and emit only the requested entry. Reuse the loaded register for other lookups in the same shell and reload it after updates.

```powershell
$canonicalUrl = 'https://example.com/article'
$register = Get-Content -LiteralPath source_archive/scanned_urls.json -Raw | ConvertFrom-Json
$register | Where-Object { $_.url -ceq $canonicalUrl } | ConvertTo-Json
```

The initial JSON preserves the processed URLs from the previous list and imports dates and access outcomes from the V100 [historical register](historical_register.jsonl). Use the JSON for routine lookups and consult the historical register only on explicit user request.
Historical evidence references to `Checkpoint_aggiornamento_2026-11-19.md` can be resolved against the [archived checkpoint in Git history](https://github.com/VanniMartignago/BCHistory.github.io/blob/c92f9c069301e370456f526e3a61b15f6b3295e7/Checkpoint_aggiornamento_2026-11-19.md).
