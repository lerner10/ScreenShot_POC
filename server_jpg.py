import datetime
import os
import pickle
import socket
import time

import PIL.ImageGrab

IP = '0.0.0.0'
PORT = 60000

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_socket.bind((IP, PORT))

server_socket.listen(1)

print('Listening to new connection')
client_socket, client_address = server_socket.accept()

startTime = time.clock()
print('Starting time: {}'.format(datetime.datetime.now().time()))

im = PIL.ImageGrab.grab()
# im.save(r'screen.jpg')
# g = r'C:\PythonProjects\ScreenShot_POC\screen.jpg'
imageAsBytes = pickle.dumps(im)
c = 0
imageSize = len(imageAsBytes)  # number of packets
print("Image size in bytes: " + str(imageSize))
numOfBytesInChunk = 8192 # 4096
numOfChunks = int(imageSize / numOfBytesInChunk)
numOfChunks = numOfChunks + 1
numOfChunksStr = str(numOfChunks)
print("Number of chunks: " + numOfChunksStr)
numOfChunksStrEncoded = numOfChunksStr.encode('utf8')
client_socket.send(numOfChunksStrEncoded)

check = int(numOfChunks)
# GetRunS = open(g, "rb")
start = 0
end = numOfBytesInChunk
while check != 1:
    currentChunk = imageAsBytes[start:end]
    client_socket.send(currentChunk)
    start += numOfBytesInChunk
    end += numOfBytesInChunk
    c += 1
    check -= 1
    print("Sending packet number: {} with size of: {}".format(str(c), len(currentChunk)))
c += 1
currentChunk = imageAsBytes[start:]
print("Sending packet number: {} with size of: {}".format(str(c), len(currentChunk)))
client_socket.send(currentChunk)
print('End time: {}'.format(datetime.datetime.now().time()))

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


endTime = time.clock()
duration = endTime - startTime
print('Took time: {time}'.format(time=duration))

server_socket.close()
