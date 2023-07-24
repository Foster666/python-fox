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
        self.ip = '10.167.219.130'

    def get_con_status(self, list_need=None):
        headers = {'content-type': 'application/json'}
        url_get_status = f"https://{list_need[0]}/api/get-container-page/?station_name=/genius/{list_need[1]}&token=genius"
        containner_status = requests.get(url_get_status, headers=headers, verify=False).json()['payload']['data']
        uut_status = containner_status[f"{list_need[2]}:{list_need[3]}"]['status']
        print(f"当前UUT状态： {uut_status}")

    def get_last_status(self, ip=None):
        headers = {'content-type': 'application/json'}
        url = f"https://{ip}/api/get-station-page/?token=genius"
        station_page = requests.get(url, headers=headers, verify=False).json()['payload']['data']
        stations = list(station_page.keys())
        stations.remove('MONITOR')
        uut_status = {}
        output_str = ""
        self.contatiner_list = []
        for key_station in stations:
            url_get_status = f"https://{ip}/api/get-container-page/?station_name=/genius/{key_station.lower()}&token=genius"
            containner_status = requests.get(url_get_status, headers=headers, verify=False).json()['payload']['data']
            for key_uut in containner_status.keys():
                uut_num = key_uut[-2:]
                self.contatiner_list.append(key_uut)
                uut_status[uut_num] = containner_status[key_uut]['status']
        sorted_uut_status = sorted(uut_status.items(), key=lambda x: x[0], reverse=False)
        sorted_uut_status = dict(sorted_uut_status)
        for key, value in sorted_uut_status.items():
            if value == 'idle':
                sorted_uut_status[key] = 'I'
            elif value == 'run':
                sorted_uut_status[key] = 'R'
            elif value == 'fail' or value == 'stop':
                sorted_uut_status[key] = 'F'
            else:
                sorted_uut_status[key] = 'E'
        for key, value in sorted_uut_status.items():
            output_str += f"{key},{value};"
        output_str = output_str[: -1]
        return output_str, self.contatiner_list

    def on_open(self, ws, list_need):
        print("WebSocket连接已打开")
        # 发送数据
        data = {
            "action": f"{list_need[0]}",
            "mode": "PROD",
            "name": f"{list_need[1]}",
            "token": "genius",
            "user": "genius"
        }
        ws.send(json.dumps(data))
        print('开始测试')
        ws.close()

    def on_message(self, ws, message):
        print("从服务器收到消息：", message)

    def on_close(self, ws):
        # 关闭连接
        ws.close()
        print("WebSocket连接已关闭")

    def on_error(self, ws, error):
        print("WebSocket发生错误：", error)

    def run_test(self, cell_num=None, command=None):
        uut_now = None
        for uut in self.contatiner_list:
            if cell_num[-2:] in uut:
                uut_now = uut
        sslopt = {"cert_reqs": ssl.CERT_NONE}
        list_need = [command, uut_now]
        ws = websocket.WebSocketApp(f"wss://{self.ip}/ws/genius/{uut_now.split(':')[0].lower()}",
                                    on_open=lambda ws: self.on_open(ws, list_need),
                                    on_message=self.on_message,
                                    on_close=self.on_close,
                                    on_error=self.on_error)
        ws.run_forever(sslopt=sslopt)
        ws.close()

    def my_debug(self):
        output_str, self.contatiner_list = self.get_last_status(ip=self.ip)
        print(output_str)
        print(self.contatiner_list)
        self.run_test(cell_num="cell 02", command="Stop Test")
        output_str, self.contatiner_list = self.get_last_status(ip=self.ip)


my_test = My_test()
my_test.my_debug()


