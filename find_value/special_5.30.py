import os
import re
import xlwt


# 主程序在最后
class MyTool:

    def __init__(self, path_log, min_max_unit):
        """ 初始化属性"""
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
        self.style_green = xlwt.easyxf('pattern: pattern solid, fore_colour green;')
        #  pattern: pattern solid, fore_colour  0x21 -->0x21 是一个表示浅粉色的 RGB 值
        self.style_center = xlwt.easyxf('align: horiz center, vert center;')
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

    def find_all_value_re_try(self, is_add, test_list, item):
        item_value = None
        item = self.special_item_handle(item)
        try:
            item_value_text = re.findall(f'\n{item}[\s\S]*?\n', test_list)[-1]
            if self.min_max_unit[2]:
                item_value = self.get_item_value_unit(item_value_text)
            else:
                item_value = self.get_item_value_no_unit(item_value_text)
            is_add = True
        except:
            pass

        return is_add, item_value

    def main_find_all_value(self, re_lists):
        self.re_lists = re_lists
        path_lists = self.get_path_lists()
        self.bulid_xls_by_xlwt(file_name=self.xls_name, is_ini=False)
        first_list_num = 2
        for pa_li_num in range(0, len(path_lists), 1):
            ss_list_num = 0
            is_add = False
            try:
                path_lists[pa_li_num].index(self.suffix)
                content = self.get_content(file_name_txt=path_lists[pa_li_num])
                file_name = re.search(self.re_file_name, path_lists[pa_li_num]).group().split('.')[0]
                sn = re.search(r'FOC[\s\S]{8}', file_name).group()
                uut = re.search(r'UUT[\s\S]{2}', file_name).group()
                is_green = False
                try:
                    file_name.index('PASS')
                    is_green = True
                except:
                    pass
                test_lists = self.get_step_text(content)
                num_in = 2
                for te_li_num in range(0, len(test_lists), 1):
                    test_list = test_lists[te_li_num]
                    num_now = self.get_step_num(step_text=test_list)
                    if self.min_max_unit[0] <= num_now <= self.min_max_unit[1]:
                        pass
                    else:
                        continue
                    for re_list_num in range(0, len(self.re_lists), 1):
                        is_add, step_name, item_value = \
                            self.find_all_value(is_add, test_list, self.re_lists[re_list_num])
                        if item_value:
                            if is_green:
                                self.sheet.write(first_list_num, re_list_num + 2 + ss_list_num, item_value, self.style_green)
                                self.sheet.write(first_list_num, 50, "PASS")
                            else:
                                self.sheet.write(first_list_num, re_list_num + 2 + ss_list_num, item_value)
                            self.sheet.write(0, num_in, step_name)
                            self.sheet.write(1, re_list_num + 2 + ss_list_num, self.re_lists[re_list_num])
                            self.sheet.write(first_list_num, 1, uut)
                            self.sheet.write(first_list_num, 0, sn)
                            # self.sheet.write(first_list_num, 51, file_name)
                        if is_add:
                            num_in += 1
                    ss_list_num += len(self.re_lists)
                if is_add:
                    first_list_num += 1

                print(f"完成{file_name}")

            except:
                pass
        self.book.save(self.xls_name)
        print('已完成查找')

    def main_find_all_value_fail(self, re_lists):
        self.re_lists = re_lists
        path_lists = self.get_path_lists()
        self.bulid_xls_by_xlwt(file_name=self.xls_name, is_ini=False)
        first_list_num = 2
        for pa_li_num in range(0, len(path_lists), 1):
            ss_list_num = 0
            is_add = False
            try:
                path_lists[pa_li_num].index(self.suffix)
                content = self.get_content(file_name_txt=path_lists[pa_li_num])
                file_name = re.search(self.re_file_name, path_lists[pa_li_num]).group().split('.')[0]
                sn = re.search(r'FOC[\s\S]{8}', file_name).group()
                uut = re.search(r'UUT[\s\S]{2}', file_name).group()
                test_lists = self.get_step_text(content)
                num_in = 2
                for te_li_num in range(0, len(test_lists), 1):
                    test_list = test_lists[te_li_num]
                    num_now = self.get_step_num(step_text=test_list)
                    if self.min_max_unit[0] <= num_now <= self.min_max_unit[1]:
                        pass
                    else:
                        continue
                    step_name = self.get_step_name(test_list)
                    test_list_re_trys = re.findall(r'Target Power[\s\S]*?Retry:', test_list)
                    for num_try in range(0, len(test_list_re_trys), 1):
                        for re_list_num in range(0, len(self.re_lists), 1):
                            is_add, item_value = \
                                self.find_all_value_re_try(is_add, test_list_re_trys[num_try],
                                                           self.re_lists[re_list_num])
                            if item_value:
                                self.sheet.write(first_list_num + num_try, re_list_num + 2 + ss_list_num, item_value)
                                self.sheet.write(0, num_in, step_name)
                                self.sheet.write(1, re_list_num + 2 + ss_list_num, self.re_lists[re_list_num])
                                self.sheet.write(first_list_num + num_try, 1, uut)
                                self.sheet.write(first_list_num + num_try, 0, sn)
                                # self.sheet.write(first_list_num, 51, file_name)
                            if is_add:
                                num_in += 1
                    ss_list_num += len(self.re_lists)
                if is_add:
                    first_list_num += 6
                print(f"完成{file_name}")

            except:
                pass
        self.book.save(self.xls_name)

        print('已完成查找')

    def main_find_all_value_all_pass_fail(self, re_lists):
        self.re_lists = re_lists
        path_lists = self.get_path_lists()
        self.bulid_xls_by_xlwt(file_name=self.xls_name, is_ini=False)
        first_list_num = 2
        for pa_li_num in range(0, len(path_lists), 1):
            ss_list_num = 0
            is_add = False
            try:
                path_lists[pa_li_num].index(self.suffix)
                content = self.get_content(file_name_txt=path_lists[pa_li_num])
                file_name = re.search(self.re_file_name, path_lists[pa_li_num]).group().split('.')[0]
                sn = re.search(r'FOC[\s\S]{8}', file_name).group()
                uut_name = re.search(r'PCBPM2[\s\S]*?~', file_name).group().split('~')[0].split('PCBPM2_')[1]
                time_data = re.search(r'202[\s\S]{5}', file_name).group()
                test_lists = self.get_step_text(content)
                num_in = 4
                start_has = 3
                self.sheet.write(first_list_num, 0, sn)
                self.sheet.write(first_list_num, 1, uut_name)
                self.sheet.write(first_list_num, 2, time_data)
                try:
                    file_name.index('PASS')
                    is_green = True
                    for te_li_num in range(0, len(test_lists), 1):
                        test_list = test_lists[te_li_num]
                        num_now = self.get_step_num(step_text=test_list)
                        if self.min_max_unit[0] <= num_now <= self.min_max_unit[1]:
                            pass
                        else:
                            continue
                        for re_list_num in range(0, len(self.re_lists), 1):
                            is_add, step_name, item_value = \
                                self.find_all_value(is_add, test_list, self.re_lists[re_list_num])
                            if item_value:
                                if is_green:
                                    self.sheet.write(first_list_num, re_list_num + start_has, item_value, self.style_green)
                                    self.sheet.write(first_list_num, 12, "PASS")
                                self.sheet.write(0, start_has, step_name)
                                self.sheet.write(1, re_list_num + start_has, self.re_lists[re_list_num])
                    first_list_num += 1
                except:
                    file_name.index('FAIL')
                    for te_li_num in range(0, len(test_lists), 1):
                        test_list = test_lists[te_li_num]
                        num_now = self.get_step_num(step_text=test_list)
                        if self.min_max_unit[0] <= num_now <= self.min_max_unit[1]:
                            pass
                        else:
                            continue
                        step_name = self.get_step_name(test_list)
                        test_list_re_trys = re.findall(r'Target Power[\s\S]*?Retry:', test_list)
                        for num_try in range(0, len(test_list_re_trys), 1):
                            self.sheet.write(first_list_num+num_try, 12, f"retry{num_try + 1}")
                            for re_list_num in range(0, len(self.re_lists), 1):
                                is_add, item_value = \
                                    self.find_all_value_re_try(is_add, test_list_re_trys[num_try], self.re_lists[re_list_num])
                                if item_value:
                                    self.sheet.write(first_list_num + num_try, re_list_num + start_has, item_value)
                                    self.sheet.write(0, num_in, step_name)
                                    self.sheet.write(1, re_list_num + start_has, self.re_lists[re_list_num])
                    if is_add:
                        self.sheet.write_merge(first_list_num, first_list_num + 4, 0, 0, sn, self.style_center)
                        self.sheet.write_merge(first_list_num, first_list_num + 4, 1, 1, uut_name, self.style_center)
                        self.sheet.write_merge(first_list_num, first_list_num + 4, 2, 2, time_data, self.style_center)
                        first_list_num += 5
                    else:
                        first_list_num += 1
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
path_log = r'F:\test_tool\dist\test_log'
min_max_unit = [180, 180, False]
item_name = ['MARGIN_DB_UP_A', 'MARGIN_DB_UP_B', 'MARGIN_DB_UP_C', 'MARGIN_DB_UP_D', 'MARGIN_DB_LO_A', 'MARGIN_DB_LO_B',
             'MARGIN_DB_LO_C', 'MARGIN_DB_LO_D']
item_find_all_value = 'Power'

j = MyTool(path_log=path_log, min_max_unit=min_max_unit)

# j.main_find_fail(item_name) # 多个文件的多个项目，找fail项的值
# j.main_find_one_item_all_value(item_find_all_value)  # 多个文件的同一项，生成一个文件。传入字符串
# j.main_find_all_value(item_name)  # 多个文件的多个项目，生成一个文件。传入列表，只会找到最后一个
# j.main_find_all_value_fail(item_name)  # 多个文件的多个项目，生成一个文件。传入列表,会去找retry
j.main_find_all_value_all_pass_fail(item_name) # 多个文件的多个项目，生成一个文件。传入列表，pass和fail的记录都找
