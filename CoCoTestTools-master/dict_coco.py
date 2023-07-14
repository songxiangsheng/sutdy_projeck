import ttkbootstrap as ttk
import hardware1
from ttkbootstrap.constants import *
import devicesinfo


def coco():
    f3 = hardware1.f3
    operation = ttk.Labelframe(
        f3, text="常用操作", padding=10
    )
    # text = ttk.Text(f3, )
    # text.place(x=495, y=200, width=369, height=393)
    operation.place(relx=0.01, rely=0.03, width=480, height=210)
    ttk.Button(operation, text="设备信息", command=devicesinfo.devicesinfo.devicesInfo).place(relx=0.01, rely=0.01)
    ttk.Button(operation, text="设备状态", command=devicesinfo.devicesinfo.device_devicemem).place(relx=0.21, rely=0.01)
    ttk.Button(operation, text="提取日志", command=devicesinfo.devicesinfo.log).place(relx=0.41, rely=0.01)
    ttk.Button(operation, text="刷机模式", command=devicesinfo.devicesinfo.device_loader).place(relx=0.61, rely=0.01)
    ttk.Button(operation, text="重启设备", command=devicesinfo.devicesinfo.devicereboot).place(relx=0.81, rely=0.01)
    ttk.Button(operation, text="APP版本", command=devicesinfo.devicesinfo.deviceappid).place(relx=0.01, rely=0.25)
    ttk.Button(operation, text="查看进程", command=devicesinfo.devicesinfo.deviceprocess).place(relx=0.21, rely=0.25)
    ttk.Button(operation, text="关闭进程", command=devicesinfo.devicesinfo.deviceoffprocess).place(relx=0.41, rely=0.25)
    ttk.Button(operation, text="清除LOG", command=devicesinfo.devicesinfo.devicedellog).place(relx=0.61, rely=0.25)
    ttk.Button(operation, text="笔端VPN", command=devicesinfo.devicesinfo.device_coco_vpn).place(relx=0.81, rely=0.25)
    ttk.Button(operation, text="开启全部LOG", command=devicesinfo.devicesinfo.deviceopenalllog).place(relx=0.01, rely=0.49)
    ttk.Button(operation, text="执行Grafana", command=devicesinfo.devicesinfo.device_coco_grafana).place(relx=0.27,
                                                                                                       rely=0.49)
    ttk.Button(operation, text="USB调试常开", command=devicesinfo.devicesinfo.deviceUSBTS).place(relx=0.52, rely=0.49)
    ttk.Button(operation, text="稳定性制图", command=devicesinfo.devicesinfo.device_Graphic).place(relx=0.78, rely=0.49)
    # ttk.Button(operation, text="设备信息", command=dict3).place(relx=0.61,rely=0.49)
    # ttk.Button(operation, text="设备信息", command=dict3).place(relx=0.81,rely=0.49)
    other = ttk.Labelframe(f3, text="其它")
    other.place(relx=0.532, rely=0.03, width=425, height=210)
    ttk.Button(other, text="内存填充", command=devicesinfo.devicesinfo.device_Fillmemory).place(relx=0.05, rely=0.01)
    ttk.Button(other, text="内存查询", command=devicesinfo.devicesinfo.device_catmemory).place(relx=0.30, rely=0.01)
    ttk.Button(other, text="无线连接", command=devicesinfo.devicesinfo.device_Wirelessconnection).place(relx=0.55,
                                                                                                    rely=0.01)
    ttk.Button(other, text="断开连接", command=devicesinfo.devicesinfo.device_killconnection).place(relx=0.05, rely=0.25)
    ttk.Button(other, text="缩短休眠", command=devicesinfo.devicesinfo.device_coco_Shortensleep).place(relx=0.30, rely=0.25)
    ttk.Button(other, text="恢复休眠", command=devicesinfo.devicesinfo.device_coco_restoresleep).place(relx=0.55, rely=0.25)
    # # ttk.Button(other, text="APP测试服").place(relx=0.05, rely=0.49)
    # ttk.Button(other, text="资源测试服").place(relx=0.05, rely=0.49)
    # ttk.Button(other, text="教材测试服").place(relx=0.34, rely=0.49)
    # ttk.Button(other, text="退出测试服").place(relx=0.64, rely=0.49)

    test = '''专项测试：\n\n\n
        嵌入式智能硬件测试流程中专项测试需要用到的操作功能，包含：\n“稳定性、功耗、Recovery、资源热更新”的场景覆盖，"OTA""UI自\n动化"待添加。。。
专项case地址：https://confluence.inner.youdao.com/pages/\nviewpage.action?pageId=96125835'''
    special = ttk.Notebook(f3)
    special.place(relx=0.01, rely=0.398, width=480, height=382)
    special.add(ttk.Label(special, text=test), text="专项测试", sticky=NW)
    # special.add(ttk.Label(special,text=test))
    recov = ttk.Notebook(f3)
    special.add(recov, text="稳定性&功耗")
    ttk.Button(recov, text="步骤一：日志重定向", bootstyle=SUCCESS,
               command=devicesinfo.devicesinfo.device_OS_loguserdisk).pack(fill=X, pady=0)
    ttk.Label(recov, text="注意：稳定性前先执行“步骤一” ↑↑↑↑↑↑，待设备重启后再继续执行稳定性场景！！", font=("微软雅黑", 10), background='#EE82EE').pack(
        fill=Y, pady=0)
    ttk.Notebook(recov).pack(fill=Y, expand="yes")
    # ttk.Label(recov, text="").pack(fill=Y, pady=0)

    ttk.Button(recov, text="扫描稳定性", command=devicesinfo.devicesinfo.device_coco_ocr).place(relx=0.02,
                                                                                           rely=0.2, width=215)
    ttk.Button(recov, text="语音稳定性", command=devicesinfo.devicesinfo.device_coco_asr).place(relx=0.02,
                                                                                           rely=0.3, width=215)
    ttk.Button(recov, text="点查稳定性", command=devicesinfo.devicesinfo.device_coco_ocrd).place(relx=0.02,
                                                                                            rely=0.4, width=215)
    ttk.Button(recov, text="随机稳定性", command=devicesinfo.devicesinfo.device_coco_monkey).place(relx=0.02,
                                                                                              rely=0.5, width=215)
    ttk.Button(recov, text="写作稳定性", command=devicesinfo.devicesinfo.device_coco_ocrwrite).place(relx=0.02,
                                                                                                rely=0.6, width=215)
    ttk.Button(recov, text="口算稳定性", command=devicesinfo.devicesinfo.device_coco_ocrmath).place(relx=0.02,
                                                                                               rely=0.7, width=215)
    ttk.Button(recov, text="屏幕常亮", command=devicesinfo.devicesinfo.device_coco_click1).place(relx=0.02,
                                                                                             rely=0.8, width=215)
    ttk.Button(recov, text="息屏点亮", command=devicesinfo.devicesinfo.device_coco_click3).place(relx=0.02,
                                                                                             rely=0.9, width=215)
    ttk.Button(recov, text="休眠点亮", command=devicesinfo.devicesinfo.device_coco_click4).place(relx=0.53,
                                                                                             rely=0.2, width=215)
    recovo = ttk.Notebook(f3)
    special.add(recovo, text="Recovery")
    ttk.Notebook(recovo).pack(fill=Y, expand="yes")
    ttk.Button(recovo, text="破坏A分区", command=devicesinfo.devicesinfo.device_coco_delA).place(relx=0.02,
                                                                                             rely=0.02, width=215)
    ttk.Button(recovo, text="破坏B分区", command=devicesinfo.devicesinfo.device_coco_delB).place(relx=0.02,
                                                                                             rely=0.12, width=215)
    ttk.Button(recovo, text="当前A分区同时破坏AB分区", command=devicesinfo.devicesinfo.device_coco_AdelAB).place(relx=0.02,
                                                                                                       rely=0.22,
                                                                                                       width=215)
    ttk.Button(recovo, text="当前B分区同时破坏AB分区", command=devicesinfo.devicesinfo.device_coco_BdelAB).place(relx=0.02,
                                                                                                       rely=0.32,
                                                                                                       width=215)
    ttk.Button(recovo, text="破坏AbootBsystem",
               command=devicesinfo.devicesinfo.device_coco_delAbootBsystem).place(relx=0.02,
                                                                                  rely=0.52, width=215)
    ttk.Button(recovo, text="破坏AsystemBboot",
               command=devicesinfo.devicesinfo.device_coco_delAsystemBboot).place(relx=0.02,
                                                                                  rely=0.42, width=215)
    ttk.Button(recovo, text="填充applog", command=devicesinfo.devicesinfo.device_coco_Applog).place(relx=0.53,
                                                                                                  rely=0.52, width=215)
    ttk.Button(recovo, text="破坏A分区Boot后重启", command=devicesinfo.devicesinfo.device_coco_Aboot).place(relx=0.02,
                                                                                                     rely=0.62,
                                                                                                     width=215)
    ttk.Button(recovo, text="破坏A分区Boot后不重启", command=devicesinfo.devicesinfo.device_coco_AbootN).place(relx=0.02,
                                                                                                       rely=0.82,
                                                                                                       width=215)
    ttk.Button(recovo, text="破坏B分区Boot后重启", command=devicesinfo.devicesinfo.device_coco_Bboot).place(relx=0.02,
                                                                                                     rely=0.72,
                                                                                                     width=215)
    ttk.Button(recovo, text="破坏B分区Boot后不重启", command=devicesinfo.devicesinfo.device_coco_BbootN).place(relx=0.02,
                                                                                                       rely=0.92,
                                                                                                       width=215)
    ttk.Button(recovo, text="填充syslog", command=devicesinfo.devicesinfo.device_coco_Syslog).place(relx=0.53,
                                                                                                  rely=0.42, width=215)
    ttk.Button(recovo, text="填充DictData", command=devicesinfo.devicesinfo.device_coco_DictData).place(
        relx=0.53, rely=0.22, width=215)
    ttk.Button(recovo, text="删除WPA", command=devicesinfo.devicesinfo.device_coco_delWPA).place(
        relx=0.53, rely=0.32, width=215)
    ttk.Button(recovo, text="一键Recovery", command=devicesinfo.devicesinfo.device_coco_recoverymode).place(
        relx=0.53, rely=0.62, width=215)
    ttk.Button(recovo, text="分区恢复状态查询", command=devicesinfo.devicesinfo.device_coco_recoverymode).place(
        relx=0.53, rely=0.72, width=215)
    ttk.Button(recovo, text="破坏AB分区BOOT", command=devicesinfo.devicesinfo.device_coco_delABboot).place(
        relx=0.53, rely=0.02, width=215)
    ttk.Button(recovo, text="破坏AB分区system", command=devicesinfo.devicesinfo.device_coco_delABsystem).place(
        relx=0.53, rely=0.12, width=215)
    patch = ttk.Notebook(f3)
    special.add(patch, text="词典热更新")
    ttk.Button(patch, text="词典列表", command=devicesinfo.devicesinfo.device_coco_DictList).pack(fill=X, pady=0)
    ttk.Button(patch, text="删除单个词典", command=devicesinfo.devicesinfo.device_coco_delOneDict).pack(fill=X, pady=0)
    ttk.Button(patch, text="删除多个词典", command=devicesinfo.devicesinfo.device_coco_delNDict).pack(fill=X, pady=0)
    ttk.Button(patch, text="删除全部词典", command=devicesinfo.devicesinfo.device_coco_delallDict).pack(fill=X, pady=0)
    # ota = ttk.Notebook(f3)
    # special.add(ota, text="OTA")
    # ttk.Label(ota, text="待添加").pack()
    # uizid = ttk.Notebook(f3)
    # special.add(uizid, text="UI自动化")
    # ttk.Label(uizid, text="待添加").pack()

    # ************************************添加按钮
    # text1 = ttk.Text(f1, )
    # text1.place(x=495, y=200, width=369, height=393)
    # text2 = ttk.Text(f3, )
    # text2.place(x=495, y=200, width=369, height=393)
    # text3 = ttk.Text(f3, )
    # text3.place(x=495, y=200, width=369, height=393)
    # text4 = ttk.Text(f4, )
    # text4.place(x=495, y=200, width=369, height=393)
    # # text5 = ttk.Text(f5, )
    # # text5.place(x=450, y=0, width=350, height=490)
    # text6 = ttk.Text(f6, )
    # text6.place(x=495, y=200, width=369, height=393)
