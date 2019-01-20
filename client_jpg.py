import socket

IP = '127.0.0.1'
PORT = 60000

my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

my_socket.connect((IP, PORT))

BigC = open("recieved-screen.jpg", "wb")
d = 0

# number of paclets
CountC = my_socket.recv(4096)
numOfChunks = 8192 # 4096
tillC = CountC.decode('utf8')
tillCC = int(tillC)
print("Receiving packets will start now if file exists.")
# print(
#   "Timeout is 15 seconds so please wait for timeout at the end.")
while tillCC != 0:
    ClientBData = my_socket.recv(numOfChunks)
    dataS = BigC.write(ClientBData)
    d += 1
    print("Received packet number:" + str(d))
    tillCC = tillCC - 1
print(
    "New Received file closed. Check contents in your directory.")
BigC.close()

# with open(file_name, 'wb') as file:
#     while True:
#         data = my_socket.recv(1024)
#         if data == 'Transferring succeeded'.encode('utf-8'):
#             print(data)
#             break
#         # write data to a file
#         file.write(data)
#     file.close()

my_socket.close()
