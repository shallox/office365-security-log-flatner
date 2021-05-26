# office365-security-log-flattner
Tool to flatten out the json blob in office365 security log entries.

Written in python3.8 (F strings are used so 3.6 or higher a must).

Python packages required:
pandas

pip install pandas



How to use:

Using power shell run something like the below set of commands to generate an input for this script:

Install-Module ExchangeOnlineManagement
Import-Module ExchangeOnlineManagement
Connect-ExchangeOnline


Once signed in using an account that has rights to serch audit log, run the following command to generate a CSV output.

Search-UnifiedAuditLog -StartDate 05-01-2021 -EndDate 05-15-2021 -userids <upn> | export-csv <path to .csv>
  
To run this script use the following command:
  python office365-security-log-flattner.py <path to .csv> <path to save .xlsx>

  
Output will ge generate into a xlsx file and each operation type will be in it's own tab.
  
  Enjoy!
