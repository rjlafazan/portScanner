from socket import *
import sys, time
from datetime import datetime

#settings.. max port set to 5000 for dev purposes
host = ''
max_port = 5000
min_port = 1

#initiating program
try:
    host = raw_input("[*] Enter Target Host Address: ")
except KeyboardInterrupt: 
    print("\n\n[*] User Requested An Interrupt.")
    print("[*] Application Shutting Down.")
    sys.exit(1)

hostip = gethostbyname(host)


