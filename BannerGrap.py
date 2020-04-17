#!/usr/bin/python

import socket,sys

#Verifica se tem todos argumentos
if len(sys.argv) !=3:
    print("Modo de Uso: ./bannerUDP.py ip port")
    sys.exit(0)

IP=str(sys.argv[1])
port=int(sys.argv[2])

#Connect
tcp=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
tcp.connect((IP,port))

#Banner
banner=tcp.recv(1024)
print("Connected in port "+str(port))
print("Banner:",banner,"\n")
if port == 80:
	tcp.send("HEAD/ HTTP/1.0")
	resp=tcp.recv(2048)
	print resp

