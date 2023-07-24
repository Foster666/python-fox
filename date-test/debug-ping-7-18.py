import os
import re
import xlwt


# 主程序在最后
class MyTool:

    def __init__(self, path_log, min_max_unit):
        self.path_log = path_log
        self.min_max_unit = min_max_unit
        self.xls_name = 'test_build'  # xls 名称（可修修改）
        self.suffix = 'txt'  # 文件后缀（可修改）
        self.start_normal = '\n\d{1,}.'  # 片段开头(依情况可修改，一般不改)
        self.middle_normal = '[\s\S]*?'  # 任何字符
        self.slash = '\\'
        self.re_file_name = f'FOC[\s\S]*?{self.suffix}'  # 查找文件名称(依情况可修改，一般不改)
        self.special_items_per = ['PER', 'PER   ']  # 特殊项（依情况可修改）
        self.fail_file_define = '\)  --- \[Failed]'  # 失败文件都包含(找fail值修改)
        self.fail_item_define = 'x'  # fail的形式（找fail值修改）
        self.fail_value_index = '(,)'  # fail不包含（找fail值，依情况修改）
        # 自定义，开始结束  1（1,2,3,4 都是,依情况修改）
        # self.start_define = 'TEST'
        # self.end_define = 'completed'
        # 自定义，开始结束  2
        self.start_define = ' TX_VERIFY'
        self.end_define = 'Test Result'
        # 自定义，开始结束  3
        # self.start_define = ' RX_VERIFY'
        # self.end_define = 'Test Result'
        # 自定义，开始结束  4
        # self.start_define = ' RSSI_VERIFY'
        # self.end_define = 'Test Result'
        self.re_get_step_text = f"{self.start_normal}{self.start_define}{self.middle_normal}{self.end_define}"

    def bulid_xls_by_xlwt(self, file_name, is_ini):
        self.xls_name = f'{self.path_log}{self.slash}{file_name}.xls'
        try:
            os.remove(self.xls_name)
            print('删除文件成功，重新创建')
        except:
            pass
        self.book = xlwt.Workbook(encoding='utf-8')
        self.sheet = self.book.add_sheet('Sheet', cell_overwrite_ok=True)
        self.sheet.col(0).width = 20 * 256
        print(f'新建文件成功')
        # self.book.save(self.xls_name)
        if is_ini:
            self.sheet.write(0, 0, 'SN')
        else:
            pass

    def get_path_lists(self):
        path_lists = os.listdir(self.path_log)
        return path_lists

    def get_content(self, file_name_txt):
        try:
            file_name_all = f"{self.path_log}{self.slash}{file_name_txt}"
            f1 = open(file_name_all, 'r+', encoding='utf-8')
            content = f1.read()
            f1.close()
        except:
            return None
        return content

    def main_find(self, item_name):
        self.bulid_xls_by_xlwt(file_name=self.xls_name, is_ini=False)
        path_lists = self.get_path_lists()
        num_in = 1
        sn_list = []
        self.sheet.write(0, 0, "SN")
        for pa_li_num in range(0, len(path_lists), 1):
            try:
                path_lists[pa_li_num].index(self.suffix)
                content = self.get_content(file_name_txt=path_lists[pa_li_num])
                file_name = re.search(self.re_file_name, path_lists[pa_li_num]).group().split('.')[0]
                sn = re.search(r'FOC[\s\S]{8}', file_name).group()
                # find_str = re.search(r'\nLoading firmware into detected phys...\n\nbcm4908_eth-0[\s\S]*?Hit ESC key to stop autoboot:',content).group()
                find_str = re.search(r'Warning - bad CRC, using default environment',content).group()
                sn_list.append(sn)
                print(f'完成{file_name}')
            except Exception as e:
                pass
        sn_list = list(dict.fromkeys(sn_list))
        for sn in sn_list:
            self.sheet.write(num_in, 0, sn)
            num_in += 1
        self.book.save(self.xls_name)
        print('已完成查找')


# log路径
path_log = r'C:\Users\X2003899\PycharmProjects\about_work\learn\about_log\test_log-7-21'
min_max_unit = [180, 185, False]
item_name = ['MARGIN_DB_UP_A', 'MARGIN_DB_UP_B', 'MARGIN_DB_UP_C', 'MARGIN_DB_UP_D', 'MARGIN_DB_LO_A', 'MARGIN_DB_LO_B',
             'MARGIN_DB_LO_C', 'MARGIN_DB_LO_D']
item_find_value = 'Power'

j = MyTool(path_log=path_log, min_max_unit=min_max_unit)

j.main_find(item_name)
