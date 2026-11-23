# Business Central V101 functional area review

- Scope: classify existing features using their documented business process and correct confirmed misclassifications.
- Baseline: `Business_Central_Updates_V100.xlsx`. Result: `Business_Central_Updates_V101.xlsx` and regenerated `Business_Central_Updates.json`.
- Catalog: 1,026 records. Added: 0. Modified: 56. Assigned: 53. Cleared: 3. Blank: 522 (down from 572).

## Added features

0.

## Modified features (56)

| V100 row | Feature | Functional Area | Evidence |
| ---: | --- | --- | --- |
| 21 | Permission sets are editable | Cleared (Exchanging Data Electronically) | [Existing catalog source](https://learn.microsoft.com/en-us/dynamics365/business-central/ui-how-users-permissions) |
| 23 | Norway — Support EHF 3.0 electronic invoices | Exchanging Data Electronically | [Existing catalog source](https://learn.microsoft.com/en-us/dynamics365/business-central/localfunctionality/norway/how-to-set-up-customers-for-ehf) |
| 24 | United Kingdom — Submit VAT returns through Making Tax Digital | Finance | [Existing catalog source](https://learn.microsoft.com/en-us/dynamics365/business-central/localfunctionality/unitedkingdom/making-tax-digital-submit-vat-return) |
| 26 | Belgium — Recognize IBANs in CODA statement imports | Finance | [Existing catalog source](https://learn.microsoft.com/en-us/dynamics365/business-central/localfunctionality/belgium/how-to-import-coda-statements) |
| 28 | Italy — Support attachments in FatturaPA invoice XML | Exchanging Data Electronically | [Existing catalog source](https://learn.microsoft.com/en-us/dynamics365/business-central/localfunctionality/italy/electronic-invoicing) |
| 29 | Italy — Export self-billing sales invoices as XML | Exchanging Data Electronically | [Existing catalog source](https://learn.microsoft.com/en-us/dynamics365/business-central/localfunctionality/italy/electronic-invoicing) |
| 32 | Mexico — Generate third-party VAT declarations with DIOT | Finance | [Existing catalog source](https://learn.microsoft.com/en-us/dynamics365/business-central/localfunctionality/mexico/ui-extensions-setup-and-generate-diot-report-mx) |
| 44 | Enter shortcut dimensions directly on document and journal lines | Finance | [Existing catalog source](https://learn.microsoft.com/en-us/dynamics365/business-central/finance-dimensions) |
| 69 | Italy — Support Fattura document types in electronic invoicing | Exchanging Data Electronically | [Existing catalog source](https://learn.microsoft.com/en-us/dynamics365/business-central/localfunctionality/italy/electronic-invoicing) |
| 71 | Control the processing order of data exchange mappings | Exchanging Data Electronically | [Existing catalog source](https://learn.microsoft.com/en-us/dynamics365/business-central/across-how-to-set-up-data-exchange-definitions) |
| 108 | Sign-in attempt telemetry in Application Insights for partners | Cleared (Sales) | [Existing catalog source](https://learn.microsoft.com/en-us/dynamics365-release-plan/2019wave2/dynamics365-business-central/sign-in-attempt-telemetry-azure-application-insights-partners) |
| 142 | Review payment matches and report bank reconciliations | Finance | [Existing catalog source](https://learn.microsoft.com/en-us/dynamics365-release-plan/2020wave1/dynamics365-business-central/bank-reconciliation-improvements) |
| 159 | Use new sales pricing experience | Sales | [Existing catalog source](https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/whatsnew/whatsnew-update-17-1) |
| 180 | The Business Central app for Microsoft Teams reaches General Availability | Cleared (Project Management) | [Existing catalog source](https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/whatsnew/whatsnew-update-17-4) |
| 202 | Dimension issues detection and repair tool | Finance | [Existing catalog source](https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/whatsnew/whatsnew-update-18-3) |
| 225 | Group G/L and VAT entries in posting preview | Finance | [Existing catalog source](https://learn.microsoft.com/en-us/dynamics365-release-plan/2021wave2/smb/dynamics365-business-central/group-gl-vat-entries-posting-preview-easily-extend-posting-preview) |
| 237 | United States — Apply the December 2021 Form 1099 format changes | Finance | [Existing catalog source](https://learn.microsoft.com/en-us/dynamics365/business-central/localfunctionality/unitedstates/tax-1099-changes) |
| 259 | Fixed Quantity in production bills of materials | Manufacturing | [Existing catalog source](https://learn.microsoft.com/en-us/dynamics365-release-plan/2022wave1/smb/dynamics365-business-central/planned-features) |
| 295 | Financial reporting replaces account schedules | Financial Business Intelligence | [Existing catalog source](https://learn.microsoft.com/en-us/dynamics365/business-central/bi-how-work-account-schedule) |
| 312 | Sort records flexibly in the Planning Worksheet | Planning | [Existing catalog source](https://learn.microsoft.com/en-us/dynamics365-release-plan/2022wave2/smb/dynamics365-business-central/flexible-sorting-planning-worksheet-page) |
| 344 | Preview the effect of exchange rate adjustments | Finance | [Existing catalog source](https://learn.microsoft.com/en-us/dynamics365/release-plan/2023wave1/smb/dynamics365-business-central/planned-features) |
| 393 | Bank reconciliation with Copilot | Finance | [Existing catalog source](https://learn.microsoft.com/en-us/dynamics365/business-central/bank-reconciliation-with-copilot) |
| 396 | Allocation account type | Finance | [Existing catalog source](https://learn.microsoft.com/en-us/dynamics365/release-plan/2023wave2/smb/dynamics365-business-central/planned-features) |
| 398 | Receive more items than ordered with inventory put-away documents | Warehouse Management | [Existing catalog source](https://learn.microsoft.com/en-us/dynamics365/business-central/design-details-warehouse-management) |
| 401 | Improve inventory count and adjustment workflows | Inventory | [Existing catalog source](https://learn.microsoft.com/en-us/dynamics365/business-central/inventory-how-count-inventory-with-documents) |
| 409 | Include intercompany general journals in approval workflows | Workflow | [Existing catalog source](https://learn.microsoft.com/en-us/dynamics365/release-plan/2023wave2/smb/dynamics365-business-central/include-approvals-intercompany-general-journals-workflows) |
| 415 | Demo tool and data for service scenarios | Service Management | [Existing catalog source](https://learn.microsoft.com/en-us/dynamics365/business-central/contoso-coffee/service/contoso-coffee-service-intro) |
| 668 | Submit IRS 1099 forms electronically to IRIS in the US localization | Finance | [Existing catalog source](https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/whatsnew/whatsnew-update-27-0) |
| 758 | Evaluate the quality of goods and materials | Quality Management | [Existing catalog source](https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/whatsnew/whatsnew-update-28-0) |
| 820 | Use Word layouts for quality management reports | Quality Management | [Existing catalog source](https://learn.microsoft.com/en-us/dynamics365/business-central/qms-manual-test-creation#print-inspection-reports) |
| 821 | Install quality management demo data and follow the setup checklist | Quality Management | [Existing catalog source](https://learn.microsoft.com/en-us/dynamics365/business-central/qms-contoso-coffee-demo-data) |
| 866 | Reduce manual work in quality tests and inspections | Quality Management | [Existing catalog source](https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/whatsnew/whatsnew-update-29-0) |
| 952 | Spain — Close non-taxable entries for VAT reporting | Finance | [Existing catalog source](https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/whatsnew/whatsnew-update-22-1#localization-updates) |
| 956 | Denmark — Use a Microsoft-managed certificate for electronic VAT drafts | Finance | [Existing catalog source](https://learn.microsoft.com/en-us/dynamics365/business-central/localfunctionality/denmark/how-to-evat-statement-dk) |
| 960 | Germany — Support the German Peppol BIS 3 e-invoice format | Exchanging Data Electronically | [Existing catalog source](https://learn.microsoft.com/en-us/dynamics365/business-central/localfunctionality/germany/germany-einvoicing) |
| 961 | Belgium — Support the Belgian Peppol BIS 3 e-invoice format | Exchanging Data Electronically | [Existing catalog source](https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/whatsnew/whatsnew-update-26-3#localization-updates) |
| 996 | Use statistical accounts in financial reports | Financial Business Intelligence | [Existing catalog source](https://learn.microsoft.com/en-us/dynamics365/business-central/bi-use-statistical-accounts) |
| 997 | Netherlands — Apply the vendor blocking flag to telebanking payments | Finance | [Existing catalog source](https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/whatsnew/whatsnew-update-22-3#localization-updates) |
| 998 | France — Use transaction numbers for invoice entries in the FEC export | Finance | [Existing catalog source](https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/whatsnew/whatsnew-update-22-5#localization-updates) |
| 999 | Denmark — Map general ledger accounts to the standard chart of accounts | Finance | [Existing catalog source](https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/whatsnew/whatsnew-update-22-5#localization-updates) |
| 1001 | United States — Use the updated IRS Form 1096 layout | Finance | [Existing catalog source](https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/whatsnew/whatsnew-update-23-3#localization-updates) |
| 1002 | Switzerland — Use ciphers 303 and 383 on the VAT statement | Finance | [Existing catalog source](https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/whatsnew/whatsnew-update-23-3#localization-updates) |
| 1004 | Mexico — Support the Comercio Exterior 2.0 complement for CFDI 4.0 | Exchanging Data Electronically | [Existing catalog source](https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/whatsnew/whatsnew-update-24-2#localization-updates) |
| 1005 | Switzerland — Use the Swiss SEPA direct debit pain.008.001.02.ch03 format | Finance | [Existing catalog source](https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/whatsnew/whatsnew-update-24-3#localization-updates) |
| 1006 | Denmark — Include the Danish scheme ID in Peppol files | Exchanging Data Electronically | [Existing catalog source](https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/whatsnew/whatsnew-update-24-3#localization-updates) |
| 1010 | Schedule item cost adjustment and posting with assisted setup | Inventory | [Existing catalog source](https://learn.microsoft.com/en-us/dynamics365-release-plan/2021wave1/smb/dynamics365-business-central/assisted-setup-helps-move-task-adjusting-item-costs-background) |
| 1011 | Review inventory availability by lot | Inventory | [Existing catalog source](https://learn.microsoft.com/en-us/dynamics365/business-central/inventory-how-availability-overview) |
| 1012 | Adjust stock using inventory receipts and shipments | Inventory | [Existing catalog source](https://learn.microsoft.com/en-us/dynamics365/business-central/inventory-how-count-adjust-reclassify) |
| 1016 | Show bin and zone fields when warehouse bins are mandatory | Warehouse Management | [Existing catalog source](https://learn.microsoft.com/en-us/previous-versions/dynamics365/release-plan/2023wave1/smb/dynamics365-business-central/bin-code-zone-code-fields-are-dynamically-shown-warehouse-documents) |
| 1018 | Enter opening balances for item-tracked inventory | Inventory | [Existing catalog source](https://learn.microsoft.com/en-us/previous-versions/dynamics365/release-plan/2023wave1/smb/dynamics365-business-central/easier-create-opening-balances-item-tracked-inventory) |
| 1020 | Manage intercompany posting setup from one page | Finance | [Existing catalog source](https://learn.microsoft.com/en-us/previous-versions/dynamics365/release-plan/2023wave1/smb/dynamics365-business-central/intercompany-posting-setup-supports-more-transaction-types-streamlines-flows) |
| 1021 | Open warehouse documents directly from source records | Warehouse Management | [Existing catalog source](https://learn.microsoft.com/en-us/previous-versions/dynamics365/release-plan/2023wave1/smb/dynamics365-business-central/navigate-easier-between-warehouse-inventory-documents) |
| 1022 | Improve navigation and layout on Financial Reporting pages | Financial Business Intelligence | [Existing catalog source](https://learn.microsoft.com/en-us/previous-versions/dynamics365/release-plan/2023wave1/smb/dynamics365-business-central/usability-improvements-financial-reporting-pages) |
| 1023 | Use selected advanced warehouse tools without directed put-away and pick | Warehouse Management | [Existing catalog source](https://learn.microsoft.com/en-us/previous-versions/dynamics365/release-plan/2023wave1/smb/dynamics365-business-central/use-advanced-warehouse-functionality-minimal-complexity) |
| 1026 | Czechia — Print blanket purchase orders in the local layout | Purchasing | [Existing catalog source](https://learn.microsoft.com/en-us/previous-versions/dynamics365/release-plan/2023wave1/smb/dynamics365-business-central/new-blanket-purchase-order-report-cz-design--czechia) |
| 1027 | Czechia — Replace the local VAT date with VAT Reporting Date | Finance | [Existing catalog source](https://learn.microsoft.com/en-us/previous-versions/dynamics365/release-plan/2023wave1/smb/dynamics365-business-central/replace-vat-date-cz-vat-reporting-date--czechia) |

## Other project changes

- Updated the current checkpoint and recorded the functional-area source checks in the scan archive.
- Moved V100 into `archivio` and verified its SHA-256 against the original.
- Used `Quality Management` for the documented quality inspection and testing features.

## Verification

- Compared all 1,026 V101 rows and all 17 catalog fields against the regenerated JSON.
- Confirmed the 56 intended Functional Area edits. Verified the workbook layout and styles and the preservation of every package part outside the changed feature worksheet.
- Rechecked normalized titles and descriptions by country or region. No duplicates were found. Release and source fields match the baseline.

## Outstanding items

- Review remaining functional candidates with specific official documentation first. Cross-functional records need a defensible single-area assignment. Platform and development records need a specific business process before an assignment can be made.
- Check existing populated areas for similar misclassifications and continue the historical source review recorded in the checkpoint.
