
import os
import ftplib
from rosapi import Core

ip = "192.168.88.1"
response = os.system("ping -c 1 " + ip)
user = "admin"
psw = ""


def upload():
    filename = "script.rsc"
    ftp = ftplib.FTP(ip)
    ftp.login("admin", "")
    ftp.cwd("")
    os.chdir(r"/home/nnk/")
    myfile = open(filename, 'r')
    ftp.cwd('flash')
    ftp.storlines('STOR ' + filename, myfile)
    myfile.close()
    print "Script", filename, "was uploaded to the device"



def mt_conn():    
    try: 
        a = Core(ip) 
    except: 
        print "WARNING! no connection to the router! Check IP-address reachability and API status on the router"
    else:
        try:
            a.login(user, psw)
        except:
            print "WARNING! Login unsucsessful. Please, check your credentials and restart the script."
        else:    
            print "\nLogin successful"         
            print "Trying to provision new script", "\n"
            try:
                prov = a.response_handler(a.talk(["/system/reset-configuration", "=no-defaults=yes", "=run-after-reset=flash/script.rsc" ,]))

            except:
                print "WARNING! Script can't check if the script was loaded! Restart the script"

            else:
                print "Check result here", prov 
                print "SUCCESS! Please wait 1 minute while the router is starting"
					
if response == 0:
  print ip, 'new RB was found! proceed with provisioning'
  upload()
  mt_conn()
  
else:
  print ip, 'sorry, new RB was not found'					
					
                        

