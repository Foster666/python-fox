import socket
import time

host = '10.167.219.130'
port = 8006


client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    client_socket.connect((host, port))
except Exception as e:
    print(f'Error connecting to server: {e}')
    exit()

command = "status"
for i in range(1):
    try:
        client_socket.send(command.encode())
        response = client_socket.recv(1024).decode().strip()
        print(response)
    except Exception as e:
        print(f'Error sending/receiving data from server: {e}')
        break


print('sleep')
time.sleep(3)


for i in range(4):
    command = f"BDL_IOS:UUT0{i},FOC111,U58H"
    try:
        client_socket.send(command.encode())
        response = client_socket.recv(1024).decode().strip()
        print(response)
    except Exception as e:
        print(f'Error sending/receiving data from server: {e}')
        break
