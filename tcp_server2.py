#fill in start

from socket import*
serverSocket = socket(AF_INET, SOCK_STREAM)
def main():
    while True:
        #import socket module
        serverSocket = socket(AF_INET, SOCK_STREAM)
        #prepare a server socket
        #declare host and port
        serverHost = "localhost" #computer iam using
        recvBuffer = 1024 #memory buffer that used
        serport = 12006 #declare port
        serverSocket.bind(("", serport))
        serverSocket.listen(1) #listen to one connection
        
        #fill in end
        while True :
            #establish connection
            print("ready")
            connectionSocket, addr = serverSocket.accept() #accept connection
            try:
                message = connectionSocket.recv(1024)#received message from client
                filename = message.split()[1]#split string into a list by separator
                f = open(filename[1:])
                outputdata = f.read() #read file
                connectionSocket.send(b'HTTP/1.1 200 OK\r\n\r\n') #Send http header line into socket
                for i in range(0, len(outputdata)):
                    connectionSocket.send(str.encode(outputdata[i]))
                connectionSocket.close()

            except Exception:
                connectionSocket.send(b'HTTP/1.1 200 OK\r\n\r\n')
                connectionSocket.send(str.encode("Samuel"))
                connectionSocket.close()           
        serverSocket.close()
                
        pass

if(__name__ == "__main__"):
    main()
