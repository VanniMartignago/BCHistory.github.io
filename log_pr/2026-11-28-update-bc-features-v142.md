# Business Central catalog V142

Baseline V141. Result V142. Verified four on-premises availability values against the linked Microsoft sources.

## Added features (0)

## Modified features (4)

- 17.2 · Signal from permission changes to added to Application Insights telemetry for partners. onPrem: empty → No. [Microsoft](https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/administration/telemetry-permission-changes-trace)
- 19.0 · Search Business Central documentation from the Help pane. onPrem: empty → No. [Microsoft](https://learn.microsoft.com/en-us/dynamics365-release-plan/2021wave2/smb/dynamics365-business-central/search-help-pane)
- 21.3 · Media/image support for Business Central connectors. onPrem: empty → No. [Microsoft](https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/whatsnew/whatsnew-update-21-3)
- 24.0 · Define Copilot prompt actions on AL pages. onPrem: empty → Yes. [Microsoft](https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/developer/devenv-page-prompting-floating-actionbar)

## Verification

- Confirmed three online-only cases. Microsoft confirms that AL prompt actions render on-premises even though the Copilot service is online-only.
- Matched all 17 fields across 1,080 Excel and JSON records. Archived V141 byte-for-byte.

## Outstanding work

- Continue checking cloud-only exceptions before applying the on-premises default to the remaining records.
