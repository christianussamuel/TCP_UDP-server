import socket
import sys

#create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

#bind the socket to the port
server_add = ('localhost', 12012)
print('Starting up on %s port %s ' % server_add)
sock.bind(server_add)
while True:
    print('\nwaiting to receiver message')
    data, address = sock.recvfrom(4096)

    print('received %s bytes from %s' % (len(data), address))
    print(data)

    if data:
        sent = sock.sendto(data,address)
        print('sent %s bytes back to %s' %(sent,address))
