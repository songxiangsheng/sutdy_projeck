# # 1剪刀   2石头  3布
# import random
# #电脑
# # a = int(input("电脑请输入"))
# i = 0
# while i < 5:
#     #玩家
#     a = random.randint(1,3)
#     b = int(input("玩家请输入"))
#     #赢
#     if (a == 3 and b == 1) or (a == 2 and b == 3) or (a == 1 and b == 2):
#         print("b赢了")
#     #输
#     elif (a == 3 and b == 2) or (a == 2 and b == 1) or (a == 1 and b == 3):
#         print("b输了")
#     #平局
#     elif a == b:
#         print("平局")
#     else:
#
#         print("你输入的无效")
#     i+=1
# print('结束了')



i = 0
j = 0
while i <= 100:

    if i%2 == 0:
        j+=i
    i += 1
print(j)


