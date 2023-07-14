#----coding:utf-8-------
import os
import requests
from xlrd import open_workbook

#获取Excel文件数据
class ReadExcel:

    def get_xls(self, sheet_name,path):
        cls = []
        # 获取文件地址
        xlsPath = path
        # 打开文件
        file = open_workbook(xlsPath)
        # 根据sheetName获取sheet
        sheet = file.sheet_by_name(sheet_name)
        # 获取行
        nrows = sheet.nrows
        for i in range(nrows):
            if sheet.row_values(i)[0] != u'case_name':
                cls.append(sheet.row_values(i))
        return cls


    def xls_Tolist(self,sheet_name,path):
        re = ReadExcel()
        xls = re.get_xls(sheet_name=sheet_name,path=path)

        xls_data = []
        for num in range(1, len(xls)):
            caseName = int(xls[num][2])
            type = int(xls[num][5])
            d = {"bookid":caseName, "page":type}
            xls_data.append(d)
        return xls_data


excel = ReadExcel()
c = excel.xls_Tolist("结果", "/Users/songxiangsheng/Downloads/popo下载/noteblock_1096617_1678793158434.xlsx")
url = "https://tiku-system-manager-test.inner.youdao.com/editsys/textbook/question/listaudited"
cookie = {"shiro.sesssion":"cd7fe6b5-eae9-44b0-a6f3-99f8db99f3da"}
inf = []
url1 = "https://tiku-system-manager-test.inner.youdao.com/editsys/tbpage/updateOrder"

for z in c:
    v = []
    payload = {'textbookid': z['bookid'], 'pageno': z['page'], 'limit': 1, 'questionid':''}
    a = requests.post(url=url, data=payload, cookies=cookie).json()

    if a['code'] == 30000:
        print("cookie过期")
        break
    # print(a)
    for i in range(len(a['data']['list'])):
        v.append(a['data']['list'][i]['id'])
    inf.append(v)
for i in inf:
    for id in range(1, len(i)):
        z = {"questionId": i[id-1], "seq": id}
        shuju = requests.post(url= url1, data=z, cookies=cookie)
        print(shuju.text)



