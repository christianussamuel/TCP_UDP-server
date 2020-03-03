import socket
import sys

#create a UDP Socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server_address = ('localhost', 12012)
message = 'This is the message. it will be repeated'
bytestosend = str.encode(message)

try:
    #send data
    print( 'sending "%s"' %bytestosend)
    sent = sock.sendto(bytestosend, server_address)

    #receive response
    print( 'waiting to receive')
    data, server = sock.recvfrom(4096)
    print( 'received "%s"' % data)
except:
    sock.close()

