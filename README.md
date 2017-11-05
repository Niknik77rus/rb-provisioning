# rb-provisioning

this script do the following:
1) searches for Mikrotik RB with default ip-address in the broadcast network
2) uploads the template you want via FTP
3) tries to login via API without a password
4) sends a command to reset with no default configuration, but with your template

additions:
- provisioning server should have address in 192.168.88.0/24 subnet (192.168.88.2/24, for instance)
- for background running please add the job to the cron:
* * * * * username /path/to/rbprov.py

recommendations:
- use as more generic template as possible
