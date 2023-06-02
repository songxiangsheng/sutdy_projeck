# a = 1

# while a <= 9:
#
# 	b=1
# 	while b <= a:
# 		print("%d*%d=%-2d"%(a,b,a*b),end="  ")
# 		b+=1
# 	print("\n")
# 	a+=1import time
# a = ("dnia asd",223 )
# for b in a:
# 	print(b)
# a = ("adddddd  2 dFSAa")
# print(a.splitlines(2))
# print(a.split("2"))


# a = ['01.py','02.py','03.txt','04.rar']
# c = 0
# # for b in a:
#     c = b.rfind('.')
#     print(b[c:])
# findname = input("请输入你要找的文件")
# for b in a:
#     if findname == b:
#         c = 1
#         break
#     else:
#         c = 0
#
# if c == 1:
#     print("找到了")
# else:
#     print("没找到")
import random
# teachers = ['a','b','c','d','e','f','g','h']
# offers = [[],[],[]]
# index = 0
# while index < len(teachers):
#     for i in range(len(offers)):
#         offers[i].append(teachers[index])
#         index += 1
#         if index == 8:
#             break
# print(offers)
# c = 0
# while c < 100:
#     a = ['铁板','面','蒸饺']
#     b = random.randint(0,2)
#     c += 1
#     print(a[b])

# for name in teachers:
#     print(name)
#     index = random.randint(0,2)
#
#     offers[index].append(name)
#
#
#     #如果这个列表大于等于2 就
# print(offers)
# i = 1
# for room in offers:
#     # print(room)
#     print("办公室%d"%i)
#     for teachersname in room:
#         print(teachersname)
#     i+=1
#     print("-"*20)


# dict = {"lizhi":"lizhis","niangao":"niangao"}
# # print(dict)
# for pia in dict:
#     print(pia)
#
#
# def bubbleSort(arr):
#     n = len(arr)
#
#     # 遍历所有数组元素
#     for i in range(n):
#
#         # Last i elements are already in place
#         for j in range(0, n - i - 1):
#
#             if arr[j] > arr[j + 1]:
#                 arr[j], arr[j + 1] = arr[j + 1], arr[j]


# arr = [64, 34, 25, 12, 22, 11, 90]
#
# bubbleSort(arr)
#
# print("排序后的数组:")
# for i in range(len(arr)):
#     print("%d" % arr[i])
# a = list(range(10))

# print(a[0])
# print(a[-1])
# zd = a[0]
# zx = a[-1]
# for b in a:
#     if zd <= b:
#         pass
#     if zx >= b:
#         pass
# print(zd,zx)




import random


# b = 0
# c = []
# while b < 100:
#     a = random.randint(0, 2)
#     c.append(a)
#     b+=1
# print(c)
#
# def num():
#     n = 0
#     while True:
#         n += 1
#         yield n
# def is_odd(n):
#     return str(n) == str(n)[::-1]
#
# f = filter(is_odd,num())
# for i in f:
#     print(i)
#     if i >= 1000:
#         break
# def somking(a,b,c):
#     sbm = a+b+c
#     return  sbm
#     # print(sbm)
#
# b = somking(2,3,4)
# print(b)

#
# def a():#嵌套
#     pass
#     def b():
#         pass
#
# def printline():
#      print("-" * 30)
#
# def printline_2(n):
#     i = 0
#     while i <n:
#         printline()
#         i+=1
# a = int(input("请输入打印个数"))
# printline_2(a)

def maxs(a,b,c):
    res = a+b+c
    return res
# i = int(input("请输入第一个数"))
# k = int(input("请输入第二个数"))
# y = int(input("请输入第三个数"))
# da = maxs(i,k,y)
# print(da)
# def mean(a,b,c):
#     ea = maxs(a,b,c)
#     ca = ea/3
#     return ca
# # xiao = int(input("请输入除数"))
# a = mean(2,3,4)
# print( a)
# a = 100
# def test1():
#     # 如果在函数中修改全局变量，那么会产生异常
#     # 如果真的需要修改，那么可以在函数里面进行声明
#     global a
#     print(a)
#     a += 1
#     print(a)
# test1()






#展示功能列表给用户
def showinfo():
    print('-'*30)
    print("学生管理系统")
    print("1、添加学生相关信息")
    print("2、删除学生相关信息")
    print("3、修改学生相关信息")
    print("4、查询学生相关信息")
    print("5、退出系统")
    print('-'*30)

StudentInformation = {}
#添加信息
def add():

    a= input("请输入学生信息（姓名）：")
    b = input("请输入学生信息（年龄）：")
    c = input("请输入学生信息（性别）：")
    # StudentInformation.update({a:b,c})
    StudentInformation[a] = b,c
    print(type(StudentInformation[a]))
#删除姓名
def de(c):
    if c in StudentInformation:
        del StudentInformation[c]
        print("删除成功")
        print(StudentInformation)
    else:
        print("不存在此人")

#修改信息
def update(c):
    if c in StudentInformation:
        del StudentInformation[c]
        add()
        print(StudentInformation)
        return
    else:
        print("不存在此人")
#查询
def select(c):
    if c == "":
        for a in StudentInformation.keys():
            print("姓名：%s 性别：%s 年龄：%s" % (a, StudentInformation.get(a)[0], StudentInformation.get(a)[1]))
        return

    if c in StudentInformation:
        print("姓名：%s 性别：%s 年龄：%s"%(c, StudentInformation.get(c)[0], StudentInformation.get(c)[1]))
        return
    else:
        print("找不到")

def intoDT():#添加学生信息
    showinfo()
    while True:
        #获取用户选择的功能
        key = input("请选择相应功能：")
        try:
            key = int(key)
        except Exception:
            print("您输入的有误，请重新输入")
            continue

        #根据用户的选择执行相关功能呢个
        if key == 1:
            add()
            print("添加成功")
            print(StudentInformation)
        elif key == 2:
            c = input("请输入要删除人的姓名：")
            de(c)
        elif key == 3:
            c = input("请输入要修改的学生姓名：")
            update(c)
        elif key == 4:
            c = input("请输入要修改的学生姓名")
            select(c)
        elif key == 5:
            print("谢谢您的使用，下次再见")
            break
        else:
            print("您输入的有误，请重新输入")


# intoDT()

def bubbleSort(arr):
    n = len(arr)

    # 遍历所有数组元素
    for i in range(n):

        # Last i elements are already in place
        for j in range(0, n - i - 1):

            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


# arr = [64, 34, 25, 12, 22, 11, 90]

# a = bubbleSort(arr)
#
# print("排序后的数组:")
# for i in range(len(arr)):
#     print("%d" % arr[i])





# for a in range(7):
#     for b in range(0,7-a-1):
#          print(b)
    # if 7 > b+1:
    #     7,b+1,= b+1,7

    # print(a)



# def mp(a):
#     v = len(a)
#     for b in range(v):
#         for c in range(v-1):
#             if a[c] > a[c+1]:
#                 a[c], a[c+1] = a[c+1], a[c]
#             # for c in range(v - 1):
#             #     if a[1] > a[c + 1]:
#             #         a[1], a[c + 1] = a[c + 1], a[1]
#     print(a)
# a = [4,5,3,1,6,2,2,9]
# mp(a)
# print("排序后的数组:")
# for i in a:
#     print(i)

def test(aTemp):
    aTemp += 1
    print(aTemp)
# a = 100


def test2():
    name = input("姓名：")
    myid = input("id:")
    age = input("年龄")
    # return  name,myid,age
    info = {"name":name,"id":myid,"age":age}
    return info
# a,b,c = test2()
# print("姓名：%s id：%s 年龄：%s"%(a,b,c))
# tmpe = test2()
# print(tmpe.get("name"),tmpe.get("id"),tmpe.get("age"))
# def test111(a,b,c=200):
#     print(a)
#     print(b)
#     print(c)
# test111(22,11,c=1)
#
# def test1(a,c,b=111):
#     print(a)
#     print(b)
#     print(c)
# test1(22,33,b=1)

def dome(s):
    if s > 1:
        d = s + dome(s-1)
    else:
        d = 1
    return d
# a= dome(100)
# print(a)
#九九乘法表
# for c in range(1,10):
#     for j in range(1,c+1):
#             print(f'{j}x{c}={j*c}', end="   ")
#     print("\n")



#猜数字
# age = 21
# counter = 0
# for i in range(10):
#     print("-->counter:", counter)
#     if counter < 3:
#         guess_num = int(input("input your guess num:"))
#         if guess_num == age :
#             print("Congratulations! you got it.")
#             break  #break的作用是不往后执行了，跳出整个循环
#         elif guess_num < age:
#             print("Think smaller!")
#         else:
#             print("Think bigger...")
#     else:
#         yon = input("是否还继续猜(y/n)?")
#         if yon == 'y':
#             counter = 0
#             continue
#         else:
#             print("Bye")
#             break
#     counter += 1   # counter = counter + 1



#定义类 ：狗
class Dog:

    def __init__(self,newname,newweight,newcolor):
        self.weight = newweight
        self.color = newcolor
        self.name = newname

    #定义了一个方法
    def bark(self):
        print("汪汪汪..........")

    def run(self):
        print("狗在跑..........")
    def eat(self):
        print("吃东西..........")
        # 在方法中可以对属性进行修改
        self.weight += 5
    def printname(self):
        print("名字：%s"%self.name)

    def __str__(self):
        msg = "我的名字是%s"%self.name,"我的颜色是%s"%self.color,"我的高度是%s"%self.weight
        return msg


def test(temp):
    a = 2
    temp.printname()
#创建对象
xiaogou = Dog("fc",78,"白色")
print(xiaogou)
#调用小狗叫的方法
# xiaogou.bark()
# xiaogou.run()


#添加属性
# xiaogou.weight = 5
#
# xiaogou.color = "黄颜色"

#获取小狗的属性
# print(xiaogou.weight)
# print(xiaogou.color)
#调用吃方法，这个方法中会对weight这个属性进行修改,需要有调用在属性之后
# xiaogou.eat()
# print(xiaogou.weight)


# 能否直接需改属性
# xiaogou.weight += 5
# print(xiaogou.weight)


dh = Dog("lz",89,"黑色")
# print(dh.weight)
# print(dh.color)

c = 1
test(xiaogou)
test(dh)

