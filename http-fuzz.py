#!/usr/bin/env python

import socket
import sys 


packes = 100
 
try:

    while True:
        # open a connection to vulnserver
        s = socket.socket (socket.AF_INET, socket.SOCK_STREAM)
        s.connect ((sys.argv[1], int(sys.argv[2])))
        # receive the banner for vulnserver
        s.recv (1024)
        print "[*] Sending " + str(packes) + " As"
        # send the number of As to fuzz the HTER command
        s.send ("GET /" + "A" * packes + " HTTP/1.0\r\n")
        # receive the response from vulnserver
        s.recv (1024)
        # close the connection
        s.close ()
        # increase the number of As we send next time
        numAs += 100

except:
    # if we get to here then something happened to vulnserver because the connection is closed
    print "Socket closed after sending " + str(packes - 100) + " As"
