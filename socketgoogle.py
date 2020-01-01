#!/usr/bin/python
#utf-8
import sys
import socket
host = 'blias.com'
port = 80
try:
    remote_ip = socket.gethostbyname( host )
    print(remote_ip)
except socket.gaierror:
    #could not resolve
    print('Hostname could not be resolved. Exiting')
    sys.exit()
    print('Ip address of '+  host+  ' is '+  remote_ip)