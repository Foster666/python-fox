import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = '10.167.199.124'
port = 8888
server_socket.bind((host, port))
server_socket.listen()
while True:
    print("等待客户端连接")
    client_socket, addr = server_socket.accept()
    print("[INFO] New client connected: {}".format(addr))

    while True:
        try:
            data = client_socket.recv(1024)
            if not data:
                print(f"客户端 {addr} 断开连接")
                break
            command = data.decode().strip()
            response = ""
            x = command.split(',')
            if len(x) == 1:
                if x[0] == 'status':
                    print(f'获取状态成功')
                    response = "1,P;2,F;3,R;4,I;5,P;6,F;7,R;8,I;9,P;10,F;11,R;12,I;13,P;14,F;15,R"
                elif x[0].startswith('cell'):
                    print('取板成功')
                    response = 'OK'
                else:
                    print('received wrong command [{}] 1'.format(x))
                    response = 'ERROR'
            elif len(x) == 3:
                print('读取SN成功')
                response = 'OK'
            else:
                print('received wrong command [{}]3'.format(x))
                response = 'ERROR'
            response += "\r\n"
            try:
                sock_err = client_socket.getsockopt(socket.SOL_SOCKET, socket.SO_ERROR)
                if sock_err == 0:
                    print('连接已建立')
                    while True:
                        try:
                            client_socket.send(response.encode())
                            break
                        except Exception as e:
                            print(f"发送响应失败: {e}")
                else:
                    print('连接失败')
                    break
            except Exception as e:
                print(f"获取socket错误信息失败: {e}")
                break
        except ConnectionResetError as e:
            print(f"客户端 {addr} 异常断开连接: {e}")
            break
    client_socket.close()
