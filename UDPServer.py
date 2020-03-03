import socket 

localIP     = "localhost"
localPort   = 12006
bufferSize  = 1024 

msgFromServer       = "Hi client :)"
bytesToSend         = str.encode(msgFromServer) #message to byte

# Create a datagram socket
UDPServerSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind to address and ip for set up connection
UDPServerSocket.bind((localIP, localPort))
print("Hello this is Samuel(UDP) listening")

# Listen for incoming datagrams
while(True):
    bytesAddressPair = UDPServerSocket.recvfrom(bufferSize)
    # The size of data that is sent by server
    message = bytesAddressPair[0]
    address = bytesAddressPair[1]
    clientMsg = message.decode('utf-8')
    clientIP  = "Client IP Address:{}".format(address)
    print(clientMsg)
    print(clientIP)

    # Sending a reply to client
    UDPServerSocket.sendto(bytesToSend, address)
