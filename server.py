import socket
import sys
import time

s = socket.socket()
host = socket.gethostname()
print("server will start on host:",host)
port = 8080
s.bind((host,port))
print("")
print("server done binding to host and port successfully")
print("")
print("server is waiting for incomming connections ")
print("")
s.listen()
conn,addr = s.accept()
print(addr,"Has connected to the server and is now online...")
print("")


while 1:
    massage = input(str(">>>"))
    massage = massage.encode()
    conn.send(massage)
    print("massage has been sent..")
    print("")
    incoming_massage = conn.recv(1024)
    incoming_massage = incoming_massage.decode()
    print("Client:", incoming_massage)
    print("")