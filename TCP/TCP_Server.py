#import socket module
import socket

def Server():
    #membuat TCP/IP SOCKET
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)#SOCK_STREAM untuk TCP
    #declare host dan port
    serverHost = "127.0.0.1"
    serverPort = 8080
    print("starting up from " ,"Host : ",serverHost, ", port : ",serverPort)
    #.bind, associate socket dengan server Host dan port
    sock.bind((serverHost, serverPort))
    #.listen mendengarkan client (jumlah bisa diatur)
    sock.listen(5)
    # 2 client dapat langsung terkoneksi dengan mengatur jumlah listen
    # diatas, contoh 5

    while True:
        #menunggu koneksi
        print("waiting for connection")
        connection, client_address = sock.accept()
        #accept() menerima dan membuka koneksi antara server dengan client
        try:
            print("connection from", str(client_address))
            #recv menerima pesan
            message = connection.recv(1024).decode('utf-8')#1024 total buffer
            #print pesan yang diterima
            print("received : ", message)
            if message:
                print("sending data back to the client", connection.sendall(message))
            else:
                print("no more data from", client_address)
                break
        except Exception:
            print("close")


if(__name__ == '__main__'):
    Server()
        

