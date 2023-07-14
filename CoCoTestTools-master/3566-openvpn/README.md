1.修改auth.txt的内容为你的vpn用户名和密码，第一行是用户名，第二行是密码
2.adb push * /data/
3.adb shell insmod /data/tun.ko  # 这行命令每次开机仅需要执行一次
4.adb shell chmod +x /data/openvpn
5.adb shell /data/openvpn /data/youdao-vpn.ovpn &
