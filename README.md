# rb-provisioning

this script do the following:
1) searches for Mikrotik RB with default ip-address in the broadcast network
2) uploads the template you want via FTP
3) tries to login via API without a password
4) sends a command to reset with no default configuration, but with your template

requirements:
1) rosapi.py for python2 should be placed in the running directory (in this repo rosapi.py has patch for handling error replies from MT)
2) provisioning server should have address in 192.168.88.0/24 subnet (192.168.88.2/24, for instance)
3) for background running please add the job to the cron:
* * * * * username /path/to/rbprov.py

recommendations:
1) use as more generic template as possible.
2) always add ":delay 15" as the first line in your template

MT = Mikrotik
RB = Routerboard
