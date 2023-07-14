# import re
# import requests
#
# f = requests.get('https://www.douyu.com/')
# imlist = re.findall(r'src="(.*?\.(jpg|png))"',f.text)
# s ='/Users/songxiangsheng/Downloads/前端/tupian/tupian.txt'
# with open(s, 'w') as f:
#     for imgurl in imlist:
#
#         zs = ''.join(imgurl[0])
#         print('正在下载%s'%imgurl[0])
#         f.write(zs)
#         f.write('\n')
#
#
#
#
# pattern = r'^scr=.*\.(jpg|png)$'
#
# text = 'scr=image.jpg'
#
# match = re.match(pattern, text)
#
# if match:
#     print('匹配成功')
# else:
#     print('匹配失败')


#!/usr/bin/python
import re
line = "Cats are smarter than dogs"
matchObj = re.match( r'(.*) are (.*?) .*', line, re.M|re.I)
if matchObj:
    print("matchObj.group() : ", matchObj.group())
    print ("matchObj.group(1) : ", matchObj.group(1))
    print ("matchObj.group(2) : ", matchObj.group(2))
else:
    print("No match!!")