#!/bin/python3
import sys #system functions and command line
import socket 
from datetime import datetime
from optparse import *

#demons team listener and port scanner
parser = OptionParser("""

Demons Scanner 

This tool has been designed to scan the open ports on the target

This tool has been designed by Demons Cyber Security Team

Usage:
 
python3 dscan.py -s <ip address>

python3 dscan.py --scan <ip address>

-h or --help for more information
    """)

#ports scanner
parser.add_option("-s","--scan",dest="target",help="to scan the hostname") #how to use scanner
#our listener 

(options,args) = parser.parse_args()
if options.target == None:
   print(parser.usage)
   exit(0)
else:
    print("{0}".format(options.target))
print("-" * 50)
print("Scanning for open ports on : "+target)
print("Time started: "+str(datetime.now()))
print("-" * 50)

try:
	for port in range(0,1000):
		    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		    socket.setdefaulttimeout(1)
		    result = s.connect_ex((target,port))
		    if result == 0:
				     print("port {} is open ".format(port))
			
except KeyboardInterrupt:
	   print("\nExiting program.")
	   sys.exit()
except socket.gaierror:
	    print("Hostname could not be resolved")
	    sys.exit
except socket.error:
	   print("there is no open ports on host"+target)
	   sys.exit
