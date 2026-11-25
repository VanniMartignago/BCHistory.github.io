# Business Central catalog V103

Baseline: V102. Result: V103. This update covers Business Central 13.2, 13.3, 13.6, 14.5, 14.8, and 29.0.

## Added features (7)

- 13.2 · Belgium — Use the 2019 Intrastat reporting format
- 13.3 · Netherlands — Use the 2019 VAT taxonomy for Digipoort
- 13.3 · DACH — Print or export the VIES declaration with dedicated reports
- 13.6 · Russia — Support the 20% VAT rate in the VAT Ledger
- 14.5 · North America — Include substitution references in Mexico CFDI invoice XML
- 14.8 · Norway — Print the KID number on sales documents
- 29.0 · Resolve creator and modifier names through system audit FlowFields

## Modified features (8)

- 28.0 · Show avatars for record creators and modifiers in lists
- 29.0 · Improve purchase order matching in Payables Agent
- 29.0 · Actions on reports and pages can now inherit tooltips
- 29.0 · Check records for uncommitted changes
- 29.0 · Evolve AL interfaces with default implementations
- 29.0 · Run multiple financial reports and get a single PDF output
- 29.0 · Faster data loading with improved data model for table extensions
- 29.0 · Recent Record virtual table

## Other changes

- Expanded the approved source scan register from 13,571 to 29,563 distinct URLs, including their access and review status.
- Updated the research checkpoint and archived the original V102 workbook.

## Verification

- All 17 fields match for all 1,033 workbook and JSON records.
- Checked the catalog table range, normalized titles and descriptions of changed entries for duplicates, and archived V102 byte parity.

## Outstanding work

- Continue reviewing the Spring 2019 branch from cumulative update 09 and check the remaining CFDI and withholding evidence.
- Continue feature-level review of approved secondary-source articles. The minimum version of the Fabric mirroring preview remains unverified.
