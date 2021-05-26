# office365-security-log-flattner


### Tool to flatten out the json blob in office365 security log .csv exports.

Written in python3.8 (F strings are used so 3.6 or higher a must).

##### Python packages required:

[Pandas](https://pandas.pydata.org/)

```
pip install pandas
```



## How to:

##### Using powershell run something like the below set of commands to generate an input .csv for this script:


```Install-Module ExchangeOnlineManagement | Import-Module ExchangeOnlineManagement | Connect-ExchangeOnline |
Search-UnifiedAuditLog -StartDate 05-01-2021 -EndDate 05-15-2021 -userids <upn> | export-csv <export.csv>
```
  
##### To run this script use the following command:

```
python office365-security-log-flattner.py <input.csv> <output.xlsx>
```
  
##### Output will ge generate into a xlsx file and each operation type will be in it's own tab.
  
# Enjoy!
