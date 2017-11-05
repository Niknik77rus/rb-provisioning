:delay 15s
/interface bridge
add admin-mac=64:D1:54:DB:88:08 auto-mac=no comment=defconf name=bridge
/interface wireless
set [ find default-name=wlan1 ] disabled=yes 
/interface bridge port
add bridge=bridge comment=defconf interface=ether1
add bridge=bridge comment=defconf interface=wlan1
/ip address
add address=192.168.88.1/24 comment=defconf interface=bridge network=\
    192.168.88.0
add address=192.168.99.122/24 comment=defconf interface=bridge network=\
    192.168.99.0
