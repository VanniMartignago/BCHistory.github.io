# Project instructions

Once at the start of each project session, before planning or making changes, fetch the latest GitHub main branch from the project's `origin` and read the current `AGENTS.md` and relevant tracked project settings directly from `origin/main`. Use those remote versions as the shared baseline across computers. Reuse that baseline for subsequent prompts in the same session. Preserve local edits and the current branch. If local settings differ, report the differences and use the GitHub versions for session guidance. If the fetch fails, report that the settings could not be verified and identify the local or cached instructions being used.

## Project purpose and files

The project maintains an English-language blog documenting Microsoft Dynamics 365 Business Central features from version 13 through the current release.

- Maintain one current handoff checkpoint in [Checkpoint.md](Checkpoint.md). Update it as research progresses and record the next starting point and outstanding work. Put per-session changes and feature lists in the pull request changelog. Do not create additional cumulative checkpoint files.
- If developing AL code in VS Code, follow `.github/copilot-istructions.md` when present.

## Research and source review

Research features chronologically from version 13 toward current releases. Verify each feature's actual minor release where evidence permits. A release note mentioning a feature does not by itself establish its introduction release.

Start each research session with the pending queues in the [source archive](source_archive/README.md). Work through recorded links awaiting access or feature review and reuse saved evidence. When the queues are empty, resume discovery from the approved primary and complementary sources. Before recording or opening a URL, normalize it and look up the exact canonical URL in the register. Record new relevant URLs there before opening them.

Keep each discovered URL queued until its review is complete. After the first access failure, queue one retry. After the second failure, archive the URL as dead. Skip processed, dead, and excluded URLs in routine scans. Apply this workflow during scheduled maintenance and release-note reviews.

At the beginning of each research session, assess whether independent feature batches can be researched in parallel. When delegating, assign distinct releases, sources, or features, use the latest workbook as the common baseline, and request proposed record changes, official references, and pages reviewed or inaccessible. Reconcile overlaps and conflicting evidence before applying changes chronologically to one sequential workbook. Use one researcher when the task is small or depends on earlier findings.

Treat each approved primary and complementary source URL as an entry point. Follow relevant Business Central links through category and tag indexes, archives, pagination, release notes, KB articles, feature pages, and cited official references. Use other indexes on approved sites to find relevant articles missing from the main navigation. Add newly discovered relevant URLs to the scan register and work through the pending pages in release order where known. Apply the source approval rules to external sites discovered along the way.

For each relevant page, identify the documented features and changes, verify the introduction version and lifecycle against the available evidence, and compare each item with the current workbook. Add missing eligible features and update existing records when the evidence warrants it. Record unresolved candidates and the evidence still needed in the checkpoint. An archive is complete when its relevant indexes, articles, and linked evidence have been reviewed and any remaining gaps have been resolved.

Consult [Business Central sources](Business_Central_Sources.md) for approved sources. Before treating a newly discovered source as approved, follow the source proposal rules below. Do not add or rely on an unapproved secondary source as a project source.

### Microsoft release notes

Check Microsoft Learn `whatsnew-update-{major}-{minor}` pages in order from 15.0 through 29.1. Check minor versions 0 through 5 for majors 15 through 28, then 29.0 and 29.1. Verify each URL because some pages may be unavailable or use another naming pattern. Use approved alternative Microsoft sources where needed. For versions 13 and 14, consult approved historical documentation and update archives. Extend the search as Microsoft publishes releases.

### Description and feature lifecycle

Write descriptions in English as clear syntheses of approved primary and secondary evidence. Explain purpose, behavior, practical context, and documented limits or prerequisites. Prefer official evidence when sources conflict, and do not invent details. Expand existing descriptions when verification shows they are insufficient.

Check for obsolete details and duplicates before adding or updating records. Consolidate confirmed duplicates without conflating distinct features, release-specific enhancements, or localized implementations. Distinguish planned, preview, generally available, deprecated, removed, and replaced features. Reconfirm planned dates against newer evidence.

Propose newly discovered sources for documenting versions 13 through the current release before adding them as primary sources. Obtain user approval before treating a new source as primary. Prefer a specific official Microsoft feature page. Use secondary sources to add description context. If only a secondary source documents a feature, leave its primary source empty. Search for official documentation during later updates and add it only when verified.

The regular maintenance cadence is every Saturday. Review previously approved sources and follow the research, versioning, and evidence rules. Propose newly discovered non-Microsoft sources for user confirmation before adding them to the project source list. During unattended work, record proposed sources for later review and continue independent research with approved sources.

### Source usage and stopping rule

Continue requested feature research while reachable work remains. After each batch, save findings and proceed to the next pending URLs. When a page is inaccessible, record the gap, look for an approved alternative, and continue with other sources. Pause if the user asks, or when less than 25% of the session's starting token budget remains, if the runtime exposes enough information to measure it. If token budget or usage is unavailable, do not estimate a token cutoff.

## Feature data and naming conventions

Maintain these fields for each feature: major version, full minor version, release wave, Microsoft product area, country or region when localization is supported by evidence, title, description, preview date, actual or planned general availability date, SaaS availability, on-premises availability, change type, release status, primary source, official documentation, and blog source.

- Use `Yes` or `No` for cloud and on-premises availability only when evidence supports the value. Leave unknowns unverified.
- When a country or region is specified and Microsoft has no more precise area, use `Country/region` as the product area. Keep an officially documented, more precise area when available.
- Before adding or changing a product area, compare existing labels with case-insensitive, whitespace- and punctuation-insensitive matching. Check singular, plural, and clearly equivalent wording. Reuse one canonical label, preferring the latest verified Microsoft classification spelling or otherwise the established spelling used by most existing records. Update existing values when required. Keep genuinely distinct areas separate and leave unknown areas empty.
- Use the `https://learn.microsoft.com/en-us/` form for Microsoft Learn documentation and release note URLs in the workbook, JSON, and project documentation.

### Source fields

- `Primary source` links to the specific source establishing the feature or change. Do not add a secondary-source column.
- `Official documentation` is a separate link to detailed functional guidance from `https://learn.microsoft.com/en-us/dynamics365/business-central/`. Populate it only after verifying a relevant page.
- `Blog source` links to a non-official article only when it focuses exclusively or predominantly on that feature. Do not use general release roundups or brief mentions. Blog-only discoveries may have empty primary and official documentation fields until official references are verified.

## Workbook update and verification

For each update:

1. Use `Business_Central_Updates.xlsx` as the initial baseline. For later updates, use the highest numbered workbook in the project root. Exclude `archive` from baseline selection, current file counts, and feature searches.
2. Carry forward the baseline data and apply verified changes in the next sequential workbook, starting with `Business_Central_Updates_V1.xlsx`. Regenerate `Business_Central_Updates.json` from it.
3. Verify workbook-to-JSON parity. Before committing, compare new and modified records with all current records using normalized titles, descriptions, release history, country or region, and source references. Resolve confirmed duplicates while preserving distinct enhancements and localized implementations. If evidence leaves doubt about whether to consolidate two entries, update an existing entry, or assign a feature to a release, ask the user before applying the disputed change. Record the unresolved evidence in the checkpoint and continue independent work. Record the result in [Checkpoint.md](Checkpoint.md).
4. After verification, move older numbered workbooks and their inspection sidecars to `archive` without changing their contents. Keep only the newest numbered workbook in the project root.

## GitHub branches, pull requests, and changelogs

- Name each feature-update branch `update/bc-features-v<N>`, where `<N>` is the resulting sequential workbook version.
- A research session begins when the user starts the chat. Close it when the user asks to stop or the available counter reports less than 25% of the starting token budget. Saving a version or checkpoint does not close the session.
- During the session, commit and push each verified workbook version with its generated JSON and changelog. Base each subsequent version branch on the previous version commit so all session commits remain visible on GitHub. Verify each push.
- Open one pull request against `main` from the final version branch when the session closes. Include the version changelogs and preserve the session commits in the pull request. If GitHub is unavailable, keep the verified files ready, record the incomplete update, and resume when access returns.
- Title each pull request `Added features XX, modified YY on DD-MM-YYYY`.
- Before committing, create one Markdown version changelog in `log_pr/` and include it in the pull request. Name it `YYYY-MM-DD-<branch-slug>.md`, replacing branch slashes with hyphens. Record session scope, baseline and resulting workbook, separate lists of added and modified feature titles, other project changes, verification results, and outstanding items. Record zero for empty feature categories. Link the changelog in the pull request description.
- After committing, show the user separate added and modified feature lists. At the end of the session, show the pull request and ask for explicit merge confirmation. Merge only after that confirmation.
- At the end of every session, report the number of canonical URLs already registered and still awaiting a first reading or feature-evidence review. Count the `unopened` and `review` groups from `python source_archive/pending_urls.py --counts`, show their total, and report eligible access retries separately. Exclude archived and fully reviewed URLs. Also report the number of distinct canonical URLs whose content review was completed during the session, including reviews that found no new feature. Track completed URLs as work progresses so repeated visits count once and counts remain accurate for sessions spanning multiple dates. Report fetch-only attempts and access failures separately if relevant.
- After a confirmed merge, synchronize local `main` with GitHub and verify both point to the same commit.
