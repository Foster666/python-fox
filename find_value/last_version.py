import os
import re
import xlwt


# 主程序在最后
class MyTool:

    def __init__(self, path_log, min_max_unit):
        """ 初始化属性
        # 设置单元格样式，将文本居中显示
        style = xlwt.easyxf('align: horz center')

        # 合并第 1 行的前三列，并将文本居中显示
        worksheet.write_merge(0, 0, 0, 2, 'Merged Cells', style)

        # 写入数据到第 2 行第 1 列，并将文本居中显示
        worksheet.write(1, 0, 'Data in Row 2, Column 1', style)
        """
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

    def get_item_value_unit(self, item_text):  # :后的第一个数值
        item_text = item_text.split(':')[1]
        try:
            item_value_unit = re.search(r'.\d{1,}.\d{1,}\s*[A-Za-z%]+', item_text).group()
        except:
            item_value_unit = re.search(r'.\d{1,}\s*[A-Za-z%]+', item_text).group()
        item_value_unit = re.sub(r"\s+", " ", item_value_unit)
        return item_value_unit

    def get_item_value_no_unit(self, item_text):  # :后的第一个数值
        item_text = item_text.split(':')[1]
        try:
            item_value_unit = re.search(r'.\d{1,}.\d{1,}', item_text).group()
        except:
            item_value_unit = re.search(r'.\d+', item_text).group()
        return float(item_value_unit)

    def get_step_name(self, step_text):  # 第一行含有\n和数字
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
            find_fail = re.search(self.fail_file_define, content).group()
        except:
            return None
        return find_fail

    def special_item_handle(self, item):
        if item == self.special_items_per[0]:
            item = self.special_items_per[1]
        else:
            pass
        return item

    def find_fail_value(self, is_add, test_list, item):
        item_value = None
        step_name = None
        item = self.special_item_handle(item)
        try:
            item_value_text = re.findall(f'\n{item}[\s\S]*?{self.fail_item_define}\n', test_list)[-1]
            try:
                item_value_text.index(self.fail_value_index)
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
        item = self.special_item_handle(item)
        try:
            item_value_text = re.findall(f'\n{item}[\s\S]*?\n', test_list)[-1]
            if self.min_max_unit[2]:
                item_value = self.get_item_value_unit(item_value_text)
            else:
                item_value = self.get_item_value_no_unit(item_value_text)
            step_name = self.get_step_name(test_list)
            is_add = True
        except:
            pass

        return is_add, step_name, item_value

    def main_find_fail(self, re_lists):
        self.re_lists = re_lists
        first_list_num = 1
        path_lists = self.get_path_lists()
        self.bulid_xls_by_xlwt(file_name=self.xls_name, is_ini=False)
        for pa_li_num in range(0, len(path_lists), 1):
            try:
                path_lists[pa_li_num].index(self.suffix)
                content = self.get_content(file_name_txt=path_lists[pa_li_num])
                find_fail = self.find_fail(content)
                if find_fail:
                    file_name = re.search(self.re_file_name, path_lists[pa_li_num]).group().split('.')[0]
                    num_in = 2
                else:
                    continue
                test_lists = self.get_step_text(content)
                is_add_f = False
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
                            self.sheet.write(first_list_num + re_li_num, num_in, item_value)
                            self.sheet.write(first_list_num - 1, num_in, step_name)
                            self.sheet.write(first_list_num + re_li_num, 1, self.re_lists[re_li_num])
                            self.sheet.write(first_list_num + re_li_num, 0, sn)
                            re_li_num_in += 1
                        if is_add:
                            num_in += 1
                            is_add_f = True
                if is_add_f:
                    first_list_num += len(self.re_lists) + 2
                print(f"完成{file_name}")
            except:
                pass
        self.book.save(self.xls_name)
        print('已完成查找')

    def main_find_one_item_all_value(self, item_name):
        first_list_num = 1
        self.bulid_xls_by_xlwt(file_name=self.xls_name, is_ini=False)
        path_lists = self.get_path_lists()
        for pa_li_num in range(0, len(path_lists), 1):
            try:
                path_lists[pa_li_num].index(self.suffix)
                content = self.get_content(file_name_txt=path_lists[pa_li_num])
                num_in = 2
                file_name = re.search(self.re_file_name, path_lists[pa_li_num]).group().split('.')[0]
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
                print(f'完成{file_name}')
            except Exception as e:
                pass
        self.book.save(self.xls_name)
        print('已完成查找')

    def main_find_all_value(self, re_lists):
        self.re_lists = re_lists
        path_lists = self.get_path_lists()
        self.bulid_xls_by_xlwt(file_name=self.xls_name, is_ini=False)
        first_list_num = 1
        for pa_li_num in range(0, len(path_lists), 1):
            try:
                path_lists[pa_li_num].index(self.suffix)
                content = self.get_content(file_name_txt=path_lists[pa_li_num])
                file_name = re.search(self.re_file_name, path_lists[pa_li_num]).group().split('.')[0]
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
                            self.sheet.write(first_list_num + re_list_num, 1, self.re_lists[re_list_num])
                    if is_add:
                        num_in += 1
                self.sheet.write_merge(first_list_num, first_list_num + len(self.re_lists) - 1, 0, 0, file_name)
                # self.sheet.write_merge(first_list_num, first_list_num + len(self.re_lists) - 1, 2, 1, sn)
                first_list_num += len(self.re_lists) + 1
                print(f"完成{file_name}")
            except:
                pass
        self.book.save(self.xls_name)
        print('已完成查找')


"""
    可以具体情况修改：def __init__(self, path_log, min_max_unit):
    必填值：1.path_log（log路径）           2.min_max_unit（最小值，最大值，是否带单位）
    选填值：1.item_name（列表，可多填）      2.item_find_all_value（字符串，只填一项）
    
"""
# log路径
path_log = r'E:\test_log530'
min_max_unit = [180, 185, False]
item_name = ['MARGIN_DB_UP_A', 'MARGIN_DB_UP_B', 'MARGIN_DB_UP_C', 'MARGIN_DB_UP_D', 'MARGIN_DB_LO_A', 'MARGIN_DB_LO_B', 'MARGIN_DB_LO_C', 'MARGIN_DB_LO_D']
item_find_all_value = 'Power'

j = MyTool(path_log=path_log, min_max_unit=min_max_unit)

# j.main_find_fail(item_name) # 多个文件的多个项目，找fail项的值
# j.main_find_one_item_all_value(item_find_all_value)  # 多个文件的同一项，生成一个文件。传入字符串
j.main_find_all_value(item_name)  # 多个文件的多个项目，生成一个文件。传入列表
