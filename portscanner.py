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

#get host (return ip value of host address/url)
hostip = gethostbyname(host)

#for each number alias port in range(x, y), do the following
for port in range(min_port, max_port):
    try:
        #call scan_host function and take host and port arguments from scan_host function below
        response = scan_host(host, port)

        #if scan_host value is 0 print "Port <number>: Open"
        if response == 0:
            print("[*] Port %d: Open" % (port))
    #if error, pass and continue to execute
    except Exception, e:
        pass

def scan_host(host, port, r_code = 1):
    try:
        #initiate sockets
        s = socket(AF_INET, SOCK_STREAM)

        #execute connect function and capture connection result
        code = s.connect_ex((host, port))

        #set r_code to 0 if code value is 0 (if execution is successful code is set to 0)
        if code == 0:
            r_code = code
        s.close()

    #if error occurs pass and continue execution (r_code is still set to 1, when response variable receives it. Therefore it will not do anything)
    except Exception, e:
        pass

    return r_code
