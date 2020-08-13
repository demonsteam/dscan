#!/bin/python3
import sys 
import socket
import time
from datetime import datetime

if len(sys.argv) == 2:
    target = socket.gethostbyname(sys.argv[1])
else:
    print("""     Demons Ports Scanner
   	This tool has been designed by Demons Cyber Security Team
   Usage: 
       python dpscan.py <target ip>""")

    sys.exit()

#pretty banner

print("~" * 50)
print("   Demons Ports Scanner")
print("Scanning for open ports on : {0}".format(target))
print("Time started: "+str(datetime.now()))
print("~" * 50)

#ports scanner function 
current_time = time.time()
try:
    a = 0
    for port in range(0,1000):
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)#Address Family INET session 
            socket.setdefaulttimeout(1)
            result = s.connect_ex((target,port))
            if result == 0:
                ser = socket.getservbyport(port)
                print("port :({0}) service: ({1}) [tcp] state: open  ".format(port, ser))
                a+=1
    if a == 0:
        print("There is no open ports on :{0}".format(target))

#time calc

    now_time = time.time()
    time_taken = now_time - current_time
    print("~" * 50)
    print("\n All Ports Has been Scanned in : {0} sec".format(time_taken))

except KeyboardInterrupt: #keyboard Interrupt
    print("\nExiting program.")
    sys.exit()
except socket.gaierror: #sokcet session gaierror
    print("Hostname could not be resolved")
    sys.exit
except socket.error:
    print("there is no open ports on host"+target)
    sys.exit
