import socket
import time
from datetime import datetime
import statistics

msgFromClient       = "Hi UDP SERVER, ini samuel"
bytesToSend         = str.encode(msgFromClient) #message to byte
serverAddressPort   = ("localhost", 12006)
bufferSize          = 1024 #The amount of memory allotted for processing

# Create a UDP socket at client side
UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

data=[]
for i in range (0,99):
    # Send to server using created UDP socket
    time_before_send = datetime.now()
    UDPClientSocket.sendto(bytesToSend, serverAddressPort)
    msgFromServer = UDPClientSocket.recvfrom(bufferSize)
    msg = msgFromServer[0].decode('utf-8')
    UDPClientSocket.settimeout(10.0)
    print(msg)

    time_after_send = datetime.now()
    delay_time = str(time_after_send-time_before_send).split(":")[2]
    print(float(delay_time)*1000)
    data.append(float(delay_time)*1000)
    time.sleep(0.2)

print("")
print("Delay max : ", max(data))
print("Delay min : ", min(data))
print("Rata-rata : ", sum(data)/len(data))
print("Standar Deviasi : ", statistics.stdev(data))
