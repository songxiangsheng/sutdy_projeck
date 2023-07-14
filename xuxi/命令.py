import subprocess
import tkinter as tk
def run_command():
    command = "mount -o remount,rw /; rm -rf /oem/YoudaoDictPen; mkdir /tmp/other; mount /dev/block/by-name/system_b /tmp/other/; rm -rf /tmp/other/oem/YoudaoDictPen/output/; sync"
    subprocess.call(command, shell=True)


c=run_command()
def run_command1():
    # 命令代码

    root = tk.Tk()

    button = tk.Button(root, text=c, command=run_command1())
    button.pack()

    root.mainloop()
