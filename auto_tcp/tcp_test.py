import socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = '10.167.199.124'   # 监听所有网络接口
port = 8006        # 端口号
server_socket.bind((host, port))
server_socket.listen()
print('等待客户端连接')
while True:
    client_socket, addr = server_socket.accept()
    print(f"new client {addr}")
    while True:
        try:
            data = client_socket.recv(1024)
        except:
            print('收不到数据')
            break
        response = ""
        command = data.decode().strip()
        command.split(',')
        if len(command.split(",")) == 1 and command == "status":
            print('获取状态成功')
            response = "1,P;2,F;3,R;4,I;5,P;6,F;7,R;8,I;9,P;10,F;11,R;12,I;13,P;14,F;15,R\r\n"
        elif len(command.split(",")) == 3:
            print('获取SN，PN成功')
            response = "OK\r\n"
        elif len(command.split(",")) == 1 and command.startswith("cell"):
            print('取板成功')
            response = "OK\r\n"
        else:
            response = "REEOR\r\n"
        # 发送响应给客户端
        # client_socket.send(response.encode())
        try:
            client_socket.send(response.encode())
        except:
            print('连接断开')
            break
        # client_socket.close()
