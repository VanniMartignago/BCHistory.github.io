# Business Central catalog V104

Baseline V103. Result V104. Reviewed Spring 2019 cumulative updates and cross-branch application, platform, and localization evidence.

## Added features (18)

- 14.10 · North America — Add CFDI relations to credit memos
- 14.10 · Netherlands — Use the NT14 schema for electronic tax declarations
- 14.14 · Italy — Distribute non-taxable amounts in withholding tax
- 14.17 · Norway — Improve SAF-T processing performance
- 14.21 · Netherlands — Use the NT15 schema for electronic tax declarations
- 14.23 · Import label and presentation linkbases from newer XBRL taxonomies
- 14.26 · Italy — Reuse the external document number across fiscal years
- 14.36 · Norway — Add free text to VAT return lines
- 14.42 · Belgium — Show vendor names in the EB Payment Journal
- 14.45 · North America — Track CFDI stamp cancellation with an electronic document status
- 14.46 · Belgium — Use version 9 of the Intervat declaration
- 14.49 · Switzerland — Run the DTA Payment Journal report from the payment journal
- 15.3 · Norway — Improve EHF Billing 3.0 for finance charge memos and reminders
- 15.7 · Italy — Show Activity Code fields
- 15.15 · Improve Sync-NavApp upgrades for environments with many companies
- 16.7 · Improve telemetry for directory creation failures
- 16.10 · Improve Sync-NavTenant upgrades for environments with many companies
- 16.12 · Sync extensions with the CommitPerTable option in Sync-NavApp

## Modified features (0)

## Other changes

- Updated the approved source register, checkpoint, and pending queue tooling.
- Documented the per-version commit and session-end pull request workflow.
- Archived the original V103 workbook.

## Verification

- Matched all 17 fields across 1,051 workbook and JSON records.
- Checked normalized titles and descriptions of the 18 additions against the catalog and verified the workbook table range.
- Verified that the archived V103 workbook is byte-for-byte identical to the baseline.

## Outstanding work

- Continue the pending application and platform reviews across the historical Microsoft update branches.
- Verify remaining secondary-source candidates and blocked cross-branch routes through the approved source queue.
