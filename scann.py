import socket

s = socket.socket()
s.settimeout(3)

port = input("port num: ")

try:
	s.connect(('192.168.0.13',int(port)))
	print(s.recv(1024))
	s.close()
except Exception as e:
	print(">>>scan error:",e)


