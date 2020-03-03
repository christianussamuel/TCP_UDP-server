#import socket module
import socket

def Client():
    #TCP/IP Socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    #declare host dan port
    serverHost = "127.0.0.1"
    serverPort = 8080
    print("connecting to :", "Host : ", serverHost, ", Port : ", serverPort) 
    sock.connect((serverHost, serverPort))

    try:
        #send message
        message = "This is the message2, it will be repeated"
        print("sending ", str(message))
        #mengirim pesan dengan .sendall
        sock.sendall(message.encode('utf-8'))

        #mencari response
        amount_received = 0
        amount_expected = len(message)

        while amount_received < amount_expected:
            #pesan di decode
            data = sock.recv(1024).decode('utf-8')
            amount_received += len(data)
            print("received from server" , data)

    except Exception:
        print("close")
        sock.close()
            
        
    

if(__name__ == '__main__'):
    Client()
