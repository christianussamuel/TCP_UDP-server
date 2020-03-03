import socket

udpip = 'localhost'
udpport = 5005
mes = 'hai'
bytesToSend = str.encode(mes)

print('udp target ip:', udpip)
print('udp target port:', udpport)
print('mes:', mes)

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.sendto(bytesToSend, (udpip, udpport))
