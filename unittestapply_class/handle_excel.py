# -*- coding: utf-8 -*-
# @Time : 2020/6/19 3:41 下午
# @Author : zhl
# @File : handle_excel.py
# @Software: PyCharm
from  openpyxl import load_workbook
class HandleExcel:
    def __init__(self,file_path,sheet_name):
        self.wb=load_workbook(file_path)
        self.sh=self.wb[sheet_name]

    def read_title(self):
        titles = []  # 用来装第一行的列表
        # 遍历第一行数据
        for title in list(self.sh.rows)[0]:
            titles.append(title.value)  # 追加到titles列表中
        return titles
    def read_all_datas(self):
        all_datas = []  # 用来装所有的测试数据的列表
        titles=self.read_title()
        for item in list(self.sh.rows)[1:]:  # 遍历行
            values = []
            for val in item:
                values.append(val.value)  # 获取的值追加到列表
            res = dict(zip(titles, values))  # zip将第一行和每其他数据打包成字典
            #res["check"] = eval(res["check"])  # 将check的字符串，转换为字典对象。
            all_datas.append(res)  # 追加到all_datas列表
        return all_datas
    def close_file(self):
        self.wb.close()
if __name__ == '__main__':
    import os
    file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'unittest_excel_class.xlsx')  # 应用os包中的函数得到excel所在路径
    ex=HandleExcel(file_path,'regist')
    cases =ex.read_all_datas()
    ex.close_file()
    for case in cases:
        print(case)