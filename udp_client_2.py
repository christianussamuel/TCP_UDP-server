import socket

udpip = 'localhost'
udpport = 5005

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

sock.bind((udpip, udpport))

while True:
    data,addr = sock.recvfrom(1024)
    print('rec mes', data)
