import socket
import sys
import time

s = socket.socket()
host = input(str("Please enter the host name of the serve :"))
port = 8080
s.connect((host,port))
print("Connect to the chat server")

while 1:
    incoming_massage = s.recv(1024)
    incoming_massage = incoming_massage.decode()
    print("Server:", incoming_massage)
    print("")
    massage = input(str(">>>"))
    massage = massage.encode()
    s.send(massage)
    print("massage has been sent..")
    print("")

