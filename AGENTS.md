# Project instructions

At the start of every project session, before planning or making changes, fetch the latest GitHub main branch from the project's `origin` and read the current `AGENTS.md` and relevant tracked project settings directly from `origin/main`. Use those remote versions as the shared baseline across computers. Preserve local edits and the current branch. If local settings differ, report the differences and use the GitHub versions for session guidance. If the fetch fails, report that the settings could not be verified and identify the local or cached instructions being used.

## Project purpose and files

The project maintains an English-language blog documenting Microsoft Dynamics 365 Business Central features from version 13 through the current release.

- `Business_Central_Updates.xlsx` is the initial database. The latest sequential workbook in the project root is the current database.
- Generate `Business_Central_Updates.json` from the current Excel workbook after each update.
- `archivio` holds historical numbered workbooks and inspection sidecars. Exclude its contents when selecting the current workbook, counting current data files, or searching current feature records.
- Keep only the latest numbered workbook in the project root. After verifying a new workbook and JSON, move older numbered workbooks and their sidecars into `archivio` without changing their contents.
- Maintain one current handoff checkpoint in [Checkpoint.md](Checkpoint.md). Update it as research progresses and record the next starting point and outstanding work. Put per-session changes and feature lists in the pull request changelog. Do not create additional cumulative checkpoint files.
- Maintain the URL-level source scan history in [archivio_fonti/README.md](archivio_fonti/README.md).
- If developing AL code in VS Code, follow `.github/copilot-istructions.md` when present.

## Research and source review

Research features chronologically from version 13 toward current releases. Verify each feature's actual minor release where evidence permits. A release note mentioning a feature does not by itself establish its introduction release.

Before opening a source URL, consult the [source scan archive](archivio_fonti/README.md). Check the [list of scanned URLs](archivio_fonti/url_scansionati.txt) using exact URL lookups. Skip matches unless the user explicitly asks to rescan them. Record each canonical URL after review, even if it yielded no feature. Consult the archived historical scan log only when the user explicitly asks. Reuse recorded findings and local extracts for sources already retrieved or scanned. Reopen a page only when the user explicitly asks to revisit sources. Record new indexes, articles, linked references, and unsuccessful access attempts as work progresses. Apply this rule to scheduled maintenance and known release-note URLs. Record scan scope so that page access, feature verification, and complete archive coverage remain distinguishable.

At the beginning of each research session, assess whether independent feature batches can be researched in parallel. When delegating, assign distinct releases, sources, or features, use the latest workbook as the common baseline, and request proposed record changes, official references, and pages reviewed or inaccessible. Reconcile overlaps and conflicting evidence before applying changes chronologically to one sequential workbook. Use one researcher when the task is small or depends on earlier findings.

For each feature, follow and verify the official references cited by approved complementary sources. For each approved blog, review its full relevant Business Central coverage, including all pages of relevant paginated archives and relevant posts discovered through other indexes. Compare eligible features with the current workbook and verify each cited official reference. Record pages reviewed and pages that could not be accessed. Mark an archive complete only when all relevant pages have been reviewed.

Consult [Business Central sources](Fonti_Business_Central.md) for approved sources. Before treating a newly discovered source as approved, follow the source proposal rules below. Do not add or rely on an unapproved secondary source as a project source.

### Microsoft release notes

Check Microsoft Learn `whatsnew-update-{major}-{minor}` pages in order from 15.0 through 29.1. Check minor versions 0 through 5 for majors 15 through 28, then 29.0 and 29.1. Verify each URL because some pages may be unavailable or use another naming pattern. Use approved alternative Microsoft sources where needed. For versions 13 and 14, consult approved historical documentation and update archives. Extend the search as Microsoft publishes releases.

### Description and feature lifecycle

Write descriptions in English as clear syntheses of approved primary and secondary evidence. Explain purpose, behavior, practical context, and documented limits or prerequisites. Prefer official evidence when sources conflict, and do not invent details. Expand existing descriptions when verification shows they are insufficient.

Check for obsolete details and duplicates before adding or updating records. Consolidate confirmed duplicates without conflating distinct features, release-specific enhancements, or localized implementations. Distinguish planned, preview, generally available, deprecated, removed, and replaced features. Reconfirm planned dates against newer evidence.

Propose newly discovered sources for documenting versions 13 through the current release before adding them as primary sources. Obtain user approval before treating a new source as primary. Prefer a specific official Microsoft feature page. Use secondary sources to add description context. If only a secondary source documents a feature, leave its primary source empty. Search for official documentation during later updates and add it only when verified.

The regular maintenance cadence is every Saturday. Review previously approved sources and follow the research, versioning, and evidence rules. Propose newly discovered non-Microsoft sources for user confirmation before adding them to the project source list. During unattended work, record proposed sources for later review and continue independent research with approved sources.

### Source usage and stopping rule

Continue requested feature research while work remains. Pause if the user asks, or when less than 25% of the session's starting token budget remains, if the runtime exposes enough information to measure it. If token budget or usage is unavailable, do not estimate a token cutoff. Keep Checkpoint.md current so work can resume.

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

1. Start from the latest sequential workbook and preserve prior versions unchanged until they are moved to `archivio` after the new version is verified.
2. Save the updated database as the next sequential workbook, beginning with `Business_Central_Updates_V1.xlsx`, then incrementing the version number. Carry forward the previous version's data and apply verified additions and updates.
3. Regenerate `Business_Central_Updates.json` from the newest workbook.
4. Before committing, compare the current workbook and JSON for duplicates. Compare new and modified records with all current records using normalized titles, descriptions, release history, country or region, and source references. Resolve confirmed duplicates while preserving distinct enhancements and localized implementations. Record the duplicate check in Checkpoint.md.
5. Verify the workbook, JSON, duplicate check, and resulting GitHub commit, pull request, or deployment before reporting completion. If GitHub access is unavailable, keep verified files ready, record the incomplete update, and resume when access returns.

## GitHub branches, pull requests, and changelogs

- Name each feature-update branch `update/bc-features-v<N>`, where `<N>` is the resulting sequential workbook version.
- When the user explicitly asks to close a session, commit and push the verified workbook and regenerated JSON on that branch, then open a pull request against `main` using the branch as its head. Closing a session does not authorize merging.
- Title each pull request `Added features XX, modified YY on DD-MM-YYYY`.
- Before committing, create one Markdown session changelog in `log_pr/` and include it in the pull request. Name it `YYYY-MM-DD-<branch-slug>.md`, replacing branch slashes with hyphens. Record session scope, baseline and resulting workbook, separate lists of added and modified feature titles, other project changes, verification results, and outstanding items. Record zero for empty feature categories. Link the changelog in the pull request description.
- After committing, show the user separate added and modified feature lists. At the end of the session, show the pull request and ask for explicit merge confirmation. Merge only after that confirmation.
- After a confirmed merge, synchronize local `main` with GitHub and verify both point to the same commit.

## Session source

See [Business Central sources](Fonti_Business_Central.md) for the approved official and complementary source list.
