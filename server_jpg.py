import socket
import PIL.ImageGrab
import time
import os
import datetime

IP = '0.0.0.0'
PORT = 60000

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_socket.bind((IP, PORT))

server_socket.listen(1)

client_socket, client_address = server_socket.accept()



print(datetime.datetime.now().time())

im = PIL.ImageGrab.grab()
im.save(r'C:\Users\AMIT\PycharmProjects\project\screen.jpg')


g = r'C:\Users\AMIT\PycharmProjects\project\screen.jpg'

c = 0
sizeS = os.stat(g)
sizeSS = sizeS.st_size  # number of packets
print("File size in bytes:" + str(sizeSS))
NumS = int(sizeSS / 4096)
NumS = NumS + 1
tillSS = str(NumS)
tillSSS = tillSS.encode('utf8')
client_socket.send(tillSSS)

check = int(NumS)
GetRunS = open(g, "rb")
while check != 0:
    RunS = GetRunS.read(4096)
    client_socket.send(RunS)
    c += 1
    check -= 1
    print("Packet number:" + str(c))
    print("Data sending in process:")
GetRunS.close()
print("Sent from Server - Get function")
print(datetime.datetime.now().time())




# path = r'C:\Users\AMIT\PycharmProjects\project\screen.jpg'
#
# with open(path, encoding="utf8", errors='ignore') as file:
#     temporal = 'temp'
#     while (temporal):
#         temporal = file.read(1024)
#         byte_temporal = temporal.encode('utf-8')
#         server_socket.sendto(byte_temporal, client_address)
#     byte_ending_message = 'Transferring succeeded'.encode('utf-8')
#     server_socket.sendto(byte_ending_message, client_address)

server_socket.close()