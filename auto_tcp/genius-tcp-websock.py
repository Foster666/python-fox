import socket
import websocket
import json
import requests
import urllib3
import ssl  # 关闭安全请求警告
from urllib3.exceptions import InsecureRequestWarning

ssl._create_default_https_context = ssl._create_unverified_context
urllib3.disable_warnings(InsecureRequestWarning)


class My_test():
    def __init__(self):
        self.ip = '10.167.219.56'

    def on_open(self, ws, list_need):
        # 发送数据
        data = {
            "action": f"{list_need[0]}",
            "mode": "PROD",
            "name": f"{list_need[1]}",
            "token": "genius",
            "user": "genius"
        }
        print(data)
        ws.send(json.dumps(data))
        print('4')
        return

    def on_message(self, ws, message):
        print("从服务器收到消息：", message)
        if message:
            ws.close()
        return

    def on_close(self, ws):
        # 关闭连接
        print('333333333')
        ws.close()
        print("WebSocket连接已关闭")
        return

    def on_error(self, ws, error):
        print("WebSocket发生错误：", error)
        return

    def run_test(self, cell_num=None, command=None):
        uut_now = "BDL_IOS:UUT00"
        sslopt = {"cert_reqs": ssl.CERT_NONE}
        list_need = [command, cell_num]
        ws = websocket.WebSocketApp(f"wss://10.167.219.56/ws/genius/bdl_ios",
                                    on_open=lambda ws: self.on_open(ws, list_need),
                                    on_message=self.on_message,
                                    on_close=self.on_close,
                                    on_error=self.on_error)
        ws.run_forever(sslopt=sslopt)
        print('1')
        ws.close()
        print('2')
        return

    def my_debug(self):
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        host = '10.167.219.130'
        port = 8006
        server_socket.bind((host, port))
        server_socket.listen()
        while True:
            print("等待客户端连接")
            client_socket, addr = server_socket.accept()
            print("[INFO] New client connected: {}".format(addr))
            while True:
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
                        self.run_test(command="Deposit Test", cell_num=x[0])
                        response = 'OK'
                    else:
                        print('received wrong command [{}] 111'.format(x))
                        response = 'ERROR'
                elif len(x) == 3:
                    print('读取SN成功,开启测试')
                    self.run_test(command="Start Test", cell_num=x[0])
                    response = 'OK'
                else:
                    print('received wrong command [{}]333'.format(x))
                    response = 'ERROR'
                response += "\r\n"
                try:
                    client_socket.send(response.encode())
                except Exception as e:
                    print(f"发送响应失败: {e}")
                    break
            # client_socket.close()


my_test = My_test()
my_test.my_debug()






