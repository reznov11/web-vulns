#!/usr/bin/env python

import socket
import sys 


packes = 100
 
try:

    while True:
        s = socket.socket (socket.AF_INET, socket.SOCK_STREAM)
        s.connect ((sys.argv[1], int(sys.argv[2])))
        s.recv (1024)
        print "[*] Sending " + str(packes) + " As"
        s.send ("GET /" + "A" * packes + " HTTP/1.0\r\n")
        s.recv (1024)
        s.close ()
        numAs += 100

except:
    print "Socket closed after sending " + str(packes - 100) + " As"
