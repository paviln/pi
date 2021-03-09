import socket

message=""
HOST, PORT = "192.168.1.220", 11000
sock= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((HOST, PORT))

while message !="KILL":
   message = raw_input("Message: ")
   message = message + "<EOF>"
   sock.send(message)
sock.close