# # 多态
# class Anmial(object):
#     def brak(self):
#         print("啊啊啊啊。。。。。。")
#
# class Dog(Anmial):
#     def brak(self):
#         print("汪汪汪。。。。。")
#
# class Cat(Anmial):
#     def brak(self):
#         print("喵喵喵。。。")
#
# class Robot(object):
#     def brak(self):
#         print("嗡嗡嗡.。。。")
# def a(wap):
#     wap.brak()
# dog = Dog()
# cat =Cat()
# a(dog)
# a(cat)
# robot =Robot()
# a(robot)


# #作业， 设置五个类
# class Animal(object):
#     def __init__(self,name,color):
#         self.name = name
#         self.color = color
#
#     def __str__(self):
#         msg = "我的名字是%s" % self.name+"我的颜色是%s" % self.color
#         return msg
#
#     def eat(self):
#         v = "草"
#         return v
#     def bark(self):
#         v = "钰"
#         return v
#     def run(self):
#         v = "正常"
#         return v
#
#
# class Horse(Animal):
#     # def __str__(self):
#     #     msg = "我吃的是%s"%self.eat + "我%s叫"%self.bark + "我跑的%s"%self.run
#     #     return msg
#
#     def bark(self):
#         c = "嗷嗷"
#         print(c)
#
#     def run(self):
#         c = ("跑的快")
#         return c
#
#
# class Donkey(Animal):
#     def bark(self):
#         c = "咩咩"
#         print(c)
#
#     def run(self):
#         c = ("跑的慢")
#         return c
#
#
# class Hanxuebaoma(Horse):
#     def __init__(self, name,color):
#         self.name = name
#         self.color = color
#
#     def bark(self):
#         c = "哈哈"
#         print(c)
#
#
#
# class Mule(Horse,Donkey):
#     def bark(self):
#         c = "嘘嘘"
#         print(c)
#
#     def run(self):
#         c = "超级慢"
#         return c
#
# anmial = Animal("李智","黑色")
#
# house = Horse("年糕","白色")
# print(house)
# hanxu = Hanxuebaoma("lizhi","血红色")
# print(hanxu)

# class People(object):#类对象
#     address = "山东"#类属性
#     def __init__(self):#实例方法
#         self.name = "xiaoming"#实例属性
#         self.age = "18"#实例属性
#     #类方法，用来修改类属性
#     @classmethod
#     def setnewaddress(cls, newaddress):
#         cls.address = newaddress
#
# p=People()
# print(People.address)
# #print(People.name)不可以这么用 会报错因为不存在对象
# print(p.name)
# print(p.address)
# p.address="内蒙古"#并没有修改原来数据
# print(p.address)
# print(People.address)
# #调用类方法来修改类属性
# People.setnewaddress("广州")
# print(People.address)
#
#
# class Animal(object):
#     def __init__(self,name="马",color="白色"):
#         self.name = name
#         self.color = color
#
# try:
#     class House(Animal):
#         housenum = 0
#         def __init__(self,name,color=''):
#             super().__init__(name)
#             self.sehousenum()
#             # House.sehousenum()
#         @classmethod
#         def sehousenum(cls):
#             cls.housenum += 1
#
#     c = House("白龙吧")
#     print(c.name)
#     print(House.housenum)
#
#     c = House("敌鹿")
#     print(c.name)
#     print(House.housenum)
# except IOError:
#     print("cuole")
#
#
#
# try:
#     open('123.txt','r')
#     print('-----------')
# except IOError:
#     print("错了")
#
#
# try:
#     print(num)
# except (IOError, NameError) as errmsg:
#     print("错了?")
#     print(errmsg)
# import time
# try:
#     c = '/Users/songxiangsheng/Downloads/popdownload/nihao1.txt'
#     f = open(c)
#     while True:
#         line = f.readline()
#         if len(line) == 0:
#           break
#         time.sleep(2)
#         print(line)
# except NameError:
#     print("名字错了")
# else:#没有特殊情况下判断
#     print("没有异常")
# finally:#执行是否出错都执行
#     f.close()
#     print("关闭文件")

# #  抛出异常
# class Exception(object):
#     def __init__(self):
#         pass
# class Shot(Exception):
#     "定义异常类"
#     def __init__(self,length,atleast):
#         Exception.__init__(self)
#         self.length = length
#         self.atleast = atleast
# try:
#     s = input('请输入')
#     if len(s) < 3:
#         raise Shot(len(s),3)
# except EOFError:
#     print("你输入一了一个结束标记EOF")
# except (Shot,x):#x这个变量被绑定额错误的实例上
#     print('Shot:输入的长度是：%d,长度至少应该是：%d'%(x.lenth,x.atleast))
# else:
#     print("没有发生异常")



class MyException(Exception):

    def __init__(self):
        self.lenght = 1
        self.atleast = 1


class Shot(MyException):

    def __init__(self, lenght, atleast):

        super().__init__()

        self.length = lenght

        self.atleast = atleast

try:

    s = input('请输入：')

    if len(s) < 3:

        raise Shot(len(s), 3)

except EOFError:

    print("你输入了一个结束标记EOF")

except Shot as e:

    print(f'Shot: 输入的长度是 {e.lenght}，长度至少应该是 {e.atleast}')

else:

    print("没有发生异常")