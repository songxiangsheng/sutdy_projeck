#!/bin/sh
cd /userdisk/dictpen_vpn/
if [ "`lsmod | grep test_kmod`" == "" ] ; then
	insmod ./test_kmod.ko
	insmod ./tun.ko
fi
export LD_LIBRARY_PATH=$(pwd)/libs:$LD_LIBRARY_PATH
nohup ./openvpn --config vpnclient.ovpn --auth-user-pass pass.txt >/dev/null 2>&1 &
