from tkinter import PhotoImage
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
import getpass
import os
import sys


def source_path(relative_path):
    if getattr(sys, 'frozen', False):
        base_path = sys._MEIPASS
    else:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)


cd = source_path('')
os.chdir(cd)

user = getpass.getuser()
app = ttk.Window(title="嵌入式智能硬件测试工具" + '   HardwareTestTools 1.4      ' + user + "欢迎使用！",  # 设置窗口的标题

                 themename="lumen",  # 设置主题  superhero 黑暗主题、litera经典主题
                 size=(950, 680),  # 窗口的大小
                 position=(100, 100),  # 窗口所在的位置
                 minsize=(0, 0),  # 窗口的最小宽高
                 maxsize=(1920, 1080),  # 窗口的最大宽高
                 resizable=(False, False),  # 设置窗口是否可以更改大小
                 alpha=1)  # 设置窗口的透明度(0.0完全透明）)
p1 = PhotoImage(file='hardware.png')
app.iconphoto(False, p1)
nb = ttk.Notebook()
nb.pack(
    side=LEFT,
    padx=(10, 10),
    expand=Y,
    fill=BOTH,
    anchor=N,
)
f0 = ttk.Frame()
nb.add(f0, text='首页')
GText = "词典笔二代"
product = ttk.Labelframe(f0, text='产品图示', padding=(5, 15))
product.place(relx=0.01, rely=0.03, width=910, height=210)
G2 = PhotoImage(file='dict2.png')
G3 = PhotoImage(file='dict3.png')
G4 = PhotoImage(file='X5.png')
G5 = PhotoImage(file='P5.png')
G6 = PhotoImage(file='apllo.png')
# ttk.Label(f0, text="产品：").place(x=10, y=20)
ttk.Label(f0, text=GText, image=G2).place(x=25, y=90, width=110, height=42)
ttk.Label(f0, text="词典笔二代").place(x=50, y=60)
ttk.Label(f0, text=GText, image=G3).place(x=150, y=90, width=110, height=42)
ttk.Label(f0, text="词典笔三代").place(x=170, y=60)
ttk.Label(f0, text=GText, image=G4).place(x=275, y=90, width=110, height=42)
ttk.Label(f0, text="词典笔X5").place(x=300, y=60)
ttk.Label(f0, text=GText, image=G5).place(x=460, y=90, width=110, height=42)
ttk.Label(f0, text="词典笔P5").place(x=490, y=60)
ttk.Label(f0, text=GText, image=G6).place(x=595, y=80, width=110, height=53)
ttk.Label(f0, text="阿波罗").place(x=635, y=60)
ttk.Label(f0, text="新品待添加。。。。").place(x=725, y=110)
f1 = ttk.Frame()
nb.add(f1, text='词典笔二代')
f2 = ttk.Frame()
nb.add(f2, text='词典笔三代')
f3 = ttk.Frame(nb)
nb.add(f3, text='词典笔X5')
f4 = ttk.Frame(nb)
nb.add(f4, text='词典笔P5')
f6 = ttk.Frame(nb)
nb.add(f6, text=' 阿 波 罗 ')
# f7 = ttk.Frame(nb)
# nb.add(f7, text='常用网址')
# f8 = ttk.Frame(nb)
# nb.add(f8, text='常用工具')
text = ttk.Text(app, )
text.place(x=505, y=290, width=425, height=380)
text.insert('end', "注意事项：\n\n" + '\n' + "欢迎您的使用！！" + '\n' + '\n' + "如果使用中遇到问题，请随时联系@wb.zhaojia01" + '\n' + '\n'
            + "工具使用教程：待录制。。。。。")

style = ttk.Style()
theme_names = style.theme_names()  # 以列表的形式返回多个主题名
theme_selection = ttk.Frame(app, )
theme_selection.place(relx=0.830, rely=0.0, width=150, height=26)
lbl = ttk.Label(app, text="主题切换:", font=("微软雅黑", 11), background='#99CCFF').place(relx=0.75, rely=0.0)
theme_cbo = ttk.Combobox(
    master=theme_selection,
    text=style.theme.name,
    values=theme_names,
)
theme_cbo.pack(fill=X, expand=YES, anchor=S)
theme_cbo.current(theme_names.index(style.theme.name))
# lbl.pack(side=RIGHT)
import dict2

dict2.abcde()
import dict3

dict3.d3()
import dict_coco

dict_coco.coco()
import dict_almond

dict_almond.almond()
import dict_apllo

dict_apllo.apllo()


def change_theme(event):
    theme_cbo_value = theme_cbo.get()
    style.theme_use(theme_cbo_value)
    theme_selected.configure(text=theme_cbo_value)
    theme_cbo.selection_clear()


theme_cbo.bind('<<ComboboxSelected>>', change_theme)
theme_selected = ttk.Label(
    master=theme_selection,
    text="litera",
    font="-size 24 -weight bold"
)
tishi = ttk.Labelframe(f0, text='支持设备列表', padding=(5, 15))
tishi.place(relx=0.01, rely=0.388, width=480, height=388)
ttk.Label(tishi, text="\n\n   词典笔二代：经典版、满分版、加强版、台湾版、日本版、北美版 \n\n   词典笔三代：3326标准版、3326专业版、3326极速版、\n\n "
                      "                    3566标准版、3566专业版（P3）、人教版\n\n   阿   波   "
                      "罗：阿波罗16G版、32G版本、64G版本、128G版本\n\n   其         它：词典笔X5、词典笔P5\n").pack(side='top', fill='x')
# tishi1 = ttk.Labelframe(f0, text='注意事项', padding=(5, 15))
# tishi1.place(relx=0.6, rely=0.595, width=300, height=190)
# ttk.Label(tishi1, text="待添加。。。").pack(fill=X, expand=YES, anchor=N)


app.mainloop()
