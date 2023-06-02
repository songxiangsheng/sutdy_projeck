#!/usr/bin/python
# -*- coding: UTF-8 -*-

# try:
#     fh = open("testfile", "w")
#     fh.write("这是一个测试文件，用于测试异常!!")
# except IOError:
#     print("Error: 没有找到文件或读取文件失败")
# else:
#     print("内容写入文件成功")
#     fh.close()
#
# try:
#     fh = open("testfile", "w")
#     try:
#         fh.write("这是一个测试文件，用于测试异常!!")
#     finally:
#         print( "关闭文件")
#         fh.close()
# except IOError:
#     print ("Error: 没有找到文件或读取文件失败")
# studentInfo = {
#     '张飞' :  18,
#     '赵云' :  17,
#     '许褚' :  16,
#     '典韦' :  18,
#     '关羽' :  19,
# }
#
# def  printAge(students) :
#     for student in students:
#         print(f'学生：{student} , 年龄 {studentInfo[student]}')
#
# printAge(['张飞', '典韦', '关羽'])
# printAge(['赵云'])

#
# import os
# os.makedirs()
# a=1
# b=2
# def func1():
#     if a==b:
#         print(a)
#     else:
#         print(b)
# import time
#
# before = time.time()
# func1()
# after = time.time()
#
# # print(f"调用func1，花费时间{after-before}")
# from datetime import datetime
# datetime.now()
# datetime.datetime()
# print(datetime.now().year)

# import os
# iTerm = r'/opt/homebrew/bin/wget http://mirrors.sohu.com/nginx/nginx-1.13.9.zip'
# os.system(iTerm)




# a = os.popen("ls")
# print(str(a.read()))
# print("下载完成")

# os.system("open -a iTerm .ls")
# from subprocess import Popen
# proc = Popen(
#         args='wget http://xxxxserver/xxxx.zip',
#         shell=True
#     )
#
# print ('让它下载，我们接下来做其他事情。。。。')
# print('主线程执行代码')

# # 从 threading 库中导入Thread类
# from threading import Thread
# from time import sleep
#
# # 定义一个函数，作为新线程执行的入口函数
# def threadFunc(arg1,arg2):
#     print('子线程 开始')
#     print(f'线程函数参数是：{arg1}, {arg2}')
#     sleep(5)
#     print('子线程 结束')
#
#
# # 创建 Thread 类的实例对象
# tad = Thread(
#     # target 参数 指定 新线程要执行的函数
#     # 注意，这里指定的函数对象只能写一个名字，不能后面加括号，
#     # 如果加括号就是直接在当前线程调用执行，而不是在新线程中执行了
#     target=threadFunc,
#
#     # 如果 新线程函数需要参数，在 args里面填入参数
#     # 注意参数是元组， 如果只有一个参数，后面要有逗号，像这样 args=('参数1',)
#     args=('参数1', '3')
# )
#
# # 执行start 方法，就会创建新线程，
# # 并且新线程会去执行入口函数里面的代码。
# # 这时候 这个进程 有两个线程了。
# tad.start()
#
# # 主线程的代码执行 子线程对象的join方法，
# # 就会等待子线程结束，才继续执行下面的代码
# tad.join()
# print('主线程结束')



# from threading import Thread,Lock
# from time import sleep
#
# bank = {
#     'byhy' : 0
# }
# avd = Lock()
# # 定义一个函数，作为新线程执行的入口函数
# def deposit(theadidx,amount):
#     avd.acquire()
#     balance =  bank['byhy']
#     # 执行一些任务，耗费了0.1秒
#     sleep(0.1)
#     bank['byhy']  = balance + amount
#     print(f'子线程 {theadidx} 结束')
#     avd.release()
# theadlist = []
# for idx in range(10):
#     thread = Thread(target = deposit,
#                     args = (idx,1)
#                     )
#     thread.start()
#     # 把线程对象都存储到 threadlist中
#     theadlist.append(thread)
#
# for thread in theadlist:
#     thread.join()
#
# print('主线程结束')
# print(f'最后我们的账号余额为 {bank["byhy"]}')


# import xlrd
#
# ba = xlrd.open_workbook("income.xlsx")
#
# print(f"包含表单数量 {ba.nsheets}")
# print(f"表单的名分别为: {ba.sheet_names()}")


# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
#
# # 创建 WebDriver 对象，指明使用chrome浏览器驱动
# wd = webdriver.Chrome(service=Service(r'chromedriver.exe'))
#
# # 调用WebDriver 对象的get方法 可以让浏览器打开指定网址
# wd.get('https://www.baidu.com')

# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from time import sleep
#
# # 创建 WebDriver 对象，指明使用chrome浏览器驱动
# # wd = webdriver.Chrome(service=Service(r'/Users/songxiangsheng/study_project/pythonProject/chromedriver'))
# wd = webdriver.Chrome()
#
# # 调用WebDriver 对象的get方法 可以让浏览器打开指定网址
# wd.get("https://luti.youdao.com")
# sleep(3)
# wd.quit()

#
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from time import sleep
#
# # 创建 WebDriver 对象
# wd = webdriver.Chrome()
#
# # 调用WebDriver 对象的get方法 可以让浏览器打开指定网址
# wd.get('https://www.baidu.com')
#
# # 根据id选择元素，返回的就是该元素对应的WebElement对象
# element = wd.find_element(By.ID, 'kw')
#
# # 通过该 WebElement对象，就可以对页面元素进行操作了
# # 比如输入字符串到 这个 输入框里
# element.send_keys('百度\n')
# sleep(5)
# wd.quit()

# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from time import sleep
# # 创建 WebDriver 实例对象，指明使用chrome浏览器驱动
# wd = webdriver.Chrome()
#
# # WebDriver 实例对象的get方法 可以让浏览器打开指定网址
# wd.get('https://cdn2.byhy.net/files/selenium/sample1.html')
#
# # 根据 class name 选择元素，返回的是 一个列表
# # 里面 都是class 属性值为 animal的元素对应的 WebElement对象
# elements = wd.find_elements(By.CLASS_NAME, 'animal')
#
# # 取出列表中的每个 WebElement对象，打印出其text属性的值
# # text属性就是该 WebElement对象对应的元素在网页中的文本内容
# for ua in elements:
#     print(ua.text)
# sleep(6)
# wd.quit()

# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from time import sleep
#
# wd = webdriver.Chrome()
# wd.implicitly_wait(10)
# wd.get('https://cdn2.byhy.net/files/selenium/sample1.html')

# # 根据 tag name 选择元素，返回的是 一个列表
# # 里面 都是 tag 名为 div 的元素对应的 WebElement对象
# elements = wd.find_elements(By.TAG_NAME, 'div')
#
#
# # 取出列表中的每个 WebElement对象，打印出其text属性的值
# # text属性就是该 WebElement对象对应的元素在网页中的文本内容
# for element in elements:
#     print(element.text)
# wd.get('https://www.byhy.net/_files/stock1.html')
#
# element = wd.find_element(By.ID, 'kw')
#
# element.send_keys('通讯\n')
#
#
# # 返回页面 ID为1 的元素
# element = wd.find_elements(By.ID,'2')
# # 打印该元素的文字内容
# print(element)
# wd.quit()
from selenium import webdriver
from selenium.webdriver.common.by import By

wd = webdriver.Chrome()
wd.implicitly_wait(10)

wd.get('https://cdn2.byhy.net/files/selenium/sample3.html')

# 点击打开新窗口的链接
link = wd.find_element(By.TAG_NAME, "a")
link.click()

# wd.title属性是当前窗口的标题栏 文本
print(wd.title)