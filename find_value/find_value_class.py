import os
import re
import xlwt


# 主程序在最后
class MyTool:

    def __init__(self, path_log, min_max_unit):
        """ 初始化属性"""
        self.path_log = path_log
        self.min_max_unit = min_max_unit
        self.start_normal = '\n\d{1,}.'
        self.start_define = 'TEST'
        self.middle_normal = '[\s\S]*?'
        self.end_define = 'completed'
        self.fail_define = '\)  --- \[Failed]'
        self.slash = '\\'
        self.re_get_step_text = f"{self.start_normal}{self.start_define}{self.middle_normal}{self.end_define}"

    def bulid_xls_by_xlwt(self, file_name, is_ini):
        self.xlsx_name = f'{self.path_log}{self.slash}{file_name}.xls'
        try:
            os.remove(self.xlsx_name)
            print('删除文件成功，重新创建')
        except:
            pass
        print(f'新建文件')
        self.book = xlwt.Workbook(encoding='utf-8')
        self.sheet = self.book.add_sheet('Sheet', cell_overwrite_ok=True)
        self.sheet.col(0).width = 20 * 256
        # self.book.save(self.xlsx_name)
        if is_ini:
            self.sheet.write(0, 0, 'SN')
        else:
            pass

    def get_item_value_unit(self, item_text):
        try:
            item_value_unit = re.search(r'.\d{1,}.\d{1,}.[A-Za-z%]+', item_text).group()
        except:
            item_value_unit = re.search(r'.\d{1,}.[A-Za-z%]+', item_text).group()
        return item_value_unit

    def get_item_value_no_unit(self, item_text):  # 在没有.的时候确保传值进来，value在最后一个数字
        try:
            item_value_unit = re.search(r'.\d{1,}.\d{1,}.', item_text).group()
        except:
            item_value_unit = re.findall(r'.\d+.', item_text)[-1]
        return float(item_value_unit)

    def get_step_name(self, step_text):  # 传值进来，第一行含有\n和数字
        try:
            step_name = re.search(r'\n\d+[\s\S]*?\n', step_text).group()
        except:
            return None
        return step_name

    def get_step_num(self, step_text):
        try:
            step_num = re.search(r'\d+', step_text).group()
        except:
            return int(-1)
        return int(step_num)

    def get_step_text(self, content):
        try:
            step_lists = re.findall(self.re_get_step_text, content)
        except:
            return None
        return step_lists

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

    def find_fail(self, content):
        try:
            find_fail = re.search(self.fail_define, content).group()
        except:
            return None
        return find_fail

    def find_fail_value(self, is_add, test_list, item):
        item_value = None
        step_name = None
        if item == 'PER':
            item = 'PER   '
        try:
            item_value_text = re.search(f'\n{item}[\s\S]*?Failed]\n', test_list).group()
            try:
                item_value_text.index('(,)')
            except:
                if self.min_max_unit[2]:
                    item_value = self.get_item_value_unit(item_value_text)
                else:
                    item_value = self.get_item_value_no_unit(item_value_text)
                step_name = self.get_step_name(test_list)
                is_add = True
        except:
            pass
        return is_add, step_name, item_value

    def find_all_value(self, is_add, test_list, item):
        item_value = None
        step_name = None
        if item == 'PER':
            item = 'PER   '
        try:
            item_value_text = re.search(f'\n{item}[\s\S]*?\n', test_list).group()
            if self.min_max_unit[2]:
                item_value = self.get_item_value_unit(item_value_text)
            else:
                item_value = self.get_item_value_no_unit(item_value_text)
            step_name = self.get_step_name(test_list)
            is_add = True
        except:
            pass
        return is_add, step_name, item_value

    def find_value(self, is_add, test_list, item):
        item_value = None
        item_num = None
        if item == 'PER':
            item = 'PER   '
        try:
            num = re.search(r'\d+', test_list).group()
            num = int(num)
            if 5 <= num <= 31:
                item_value_text = re.search(f'\n{item}[\s\S]*?\n', test_list).group()
                item_value = re.search(r'.\d{1,}.\d{1,} [dBpm%]+', item_value_text).group()
                item_num = re.search(r'\d+[\s\S]*?\n', test_list).group()
                is_add = True
            else:
                pass
            # print(item_value_text)
        except:
            pass
        return is_add, item_num, item_value

    def main_find_fail(self, re_lists):
        self.re_lists = re_lists
        first_list_num = 1
        path_lists = self.get_path_lists()
        self.bulid_xls_by_xlwt(file_name='test_build', is_ini=False)
        for pa_li_num in range(0, len(path_lists), 1):
            try:
                path_lists[pa_li_num].index('.txt')
                content = self.get_content(file_name_txt=path_lists[pa_li_num])
                find_fail = self.find_fail(content)
                if find_fail:
                    file_name = re.search(r'FOC[\s\S]{8}_[\s\S]*?txt', path_lists[pa_li_num]).group().split('.txt')[0]
                    num_in = 2
                else:
                    continue
                test_lists = self.get_step_text(content)
                sn = re.search(r'FOC[\s\S]{8}', file_name).group()
                for te_li_num in range(0, len(test_lists), 1):
                    test_list = test_lists[te_li_num]
                    num_now = self.get_step_num(step_text=test_list)
                    if self.min_max_unit[0] <= num_now <= self.min_max_unit[1]:
                        pass
                    else:
                        continue
                    is_add = False
                    re_li_num_in = 0
                    for re_li_num in range(0, len(self.re_lists), 1):
                        is_add, step_name, item_value = \
                            self.find_fail_value(is_add, test_list, self.re_lists[re_li_num])
                        if item_value:
                            self.sheet.write(first_list_num + re_li_num_in, num_in, item_value)
                            self.sheet.write(first_list_num - 1, num_in, step_name)
                            self.sheet.write(first_list_num + re_li_num_in, 1, self.re_lists[re_li_num])
                            self.sheet.write(first_list_num + re_li_num_in, 0, sn)
                            re_li_num_in += 1
                    if is_add:
                        num_in += 1
                first_list_num += len(self.re_lists) + 2
                print(f"完成{file_name}")
            except:
                pass
        self.book.save(self.xlsx_name)

    def main_find_one_item_all_value(self, item_name):
        first_list_num = 1
        self.bulid_xls_by_xlwt(file_name='test_build', is_ini=False)
        path_lists = self.get_path_lists()
        for pa_li_num in range(0, len(path_lists), 1):
            try:
                path_lists[pa_li_num].index('.txt')
                content = self.get_content(file_name_txt=path_lists[pa_li_num])
                num_in = 2
                file_name = re.search(r'FOC[\s\S]{8}_[\s\S]*?txt', path_lists[pa_li_num]).group().split('.txt')[0]
                test_lists = self.get_step_text(content)
                sn = re.search(r'FOC[\s\S]{8}', file_name).group()
                for te_li_num in range(0, len(test_lists), 1):
                    test_list = test_lists[te_li_num]
                    num_now = self.get_step_num(step_text=test_list)
                    if self.min_max_unit[0] <= num_now <= self.min_max_unit[1]:
                        pass
                    else:
                        continue
                    is_add = False
                    is_add, step_name, item_value = self.find_all_value(is_add, test_list, item_name)
                    if item_value:
                        self.sheet.write(0, num_in, step_name)
                        self.sheet.write(first_list_num, 0, file_name)
                        self.sheet.write(first_list_num, 1, sn)
                        self.sheet.write(first_list_num, num_in, item_value)
                    if is_add:
                        num_in += 1
                first_list_num += 1
            except Exception as e:
                pass
        self.book.save(self.xlsx_name)
        print('已完成查找')

    def main_find_all_value(self, re_lists):
        self.re_lists = re_lists
        path_lists = self.get_path_lists()
        self.bulid_xls_by_xlwt(file_name='test_build', is_ini=False)
        first_list_num = 1
        for pa_li_num in range(0, len(path_lists), 1):
            try:
                path_lists[pa_li_num].index('.txt')
                content = self.get_content(file_name_txt=path_lists[pa_li_num])
                file_name = re.search(r'FOC[\s\S]{8}_[\s\S]*?txt', path_lists[pa_li_num]).group().split('.txt')[0]
                sn = re.search(r'FOC[\s\S]{8}', file_name).group()
                test_lists = self.get_step_text(content)
                num_in = 2
                for te_li_num in range(0, len(test_lists), 1):
                    test_list = test_lists[te_li_num]
                    num_now = self.get_step_num(step_text=test_list)
                    if self.min_max_unit[0] <= num_now <= self.min_max_unit[1]:
                        pass
                    else:
                        continue
                    is_add = False
                    for re_list_num in range(0, len(self.re_lists), 1):
                        is_add, step_name, item_value = \
                            self.find_all_value(is_add, test_list, self.re_lists[re_list_num])
                        if item_value:
                            self.sheet.write(first_list_num + re_list_num, num_in, item_value)
                            self.sheet.write(0, num_in, step_name)
                            self.sheet.write(first_list_num + re_list_num, 2, self.re_lists[re_list_num])
                    if is_add:
                        num_in += 1
                print(f"完成{file_name}")
                self.sheet.write_merge(first_list_num, first_list_num + len(self.re_lists) - 1, 0, 0, file_name)
                self.sheet.write_merge(first_list_num, first_list_num + len(self.re_lists) - 1, 1, 1, sn)
                first_list_num += len(self.re_lists) + 1
            except:
                pass
        self.book.save(self.xlsx_name)


"""
    ['EVM_DB_ALL', 'EVM_DB_AVG_S1 ', 'FREQ_ERROR_AVG ', 'LO_LEAKAGE_VSA1','POWER_AVG_DBM', 'PER', 'RSSI_RX1', 'RSSI_RX2']
"""
# log路径
path_log = r'E:\0420\20230420\pine_5g'
# item名称，多个文件的多个项目
item_name = ['LO_LEAKAGE_VSA1']
# 测试项[最大值,最小值,True/False]，当最大值等于最小值时，只抓一项。第三项控制是否带单位
min_max_unit = [50, 120, False]
# 多个文件的同一项
item_find_all_value = 'EVM_DB_AVG_S1'
j = MyTool(path_log=path_log, min_max_unit=min_max_unit)

j.main_find_fail(item_name) # 多个文件的多个项目，找fail项的值，
# j.main_find_one_item_all_value(item_find_all_value)  # 多个文件的同一项，生成一个文件。传入字符串
# j.main_find_all_value(item_name)  # 多个文件的多个项目，生成一个文件。传入列表
