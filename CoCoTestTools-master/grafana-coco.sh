#! /bin/sh
# Record vital info of devices and send them to grafana database to be monitored
# When running offline, plz address these infos by using GraphicTool

mkdir /userdisk/testlog
# vendor_storage -r VENDOR_SN_ID -t string|awk '{print $2}'|head -n 1 > /userdata/testlog/device_sn
PiD=`ps | grep -w miniapp | grep -v grep | grep -v /bin/bash | grep miniapp | awk '{print $1}'`

url_begin='http://influxdb.inner.youdao.com/write?db=dictpen_test'
echo $SN > /userdisk/testlog/device_sn

delay=$2
if [ "" == "$delay" ]; then
	delay=10
fi

capture=$1
if [[ "$capture" != "full" ]]; then
	capture="partial"
fi

# Acquiring battery info: capacity, voltage, current
function batteryGrep(){
	cd /sys/class/power_supply/battery/
	current_now=`cat current_now`
	if [ ! -n "$current_now" ]; then
  battery_info="`date "+%Y%m%d|%H:%M:%S"`|capacity|`cat capacity`|voltage|`cat voltage_now`|current|0"
  else
  battery_info="`date "+%Y%m%d|%H:%M:%S"`|capacity|`cat capacity`|voltage|`cat voltage_now`|current|`cat current_now`"
  fi
	echo $battery_info
	echo $battery_info >> /userdisk/testlog/battery_info.log
}

# Upload battery info onto grafana.db
function batteryUpload(){
	curl -i -XPOST $url_begin --data-binary $(cat /userdisk/testlog/device_sn)',stuid='$(cat /userdisk/testlog/device_sn)' capacity='$(tail -n 1 /userdisk/testlog/battery_info.log|awk -F"|" '{print $4}')
	curl -i -XPOST $url_begin --data-binary $(cat /userdisk/testlog/device_sn)',stuid='$(cat /userdisk/testlog/device_sn)' voltage='$(tail -n 1 /userdisk/testlog/battery_info.log|awk -F"|" '{print $6}')
	curl -i -XPOST $url_begin --data-binary $(cat /userdisk/testlog/device_sn)',stuid='$(cat /userdisk/testlog/device_sn)' current='$(tail -n 1 /userdisk/testlog/battery_info.log|awk -F"|" '{print $8}')
}

# Acquiring temperature info: cpu_temp, gpu_tmp, battery_temp
function tempGrep(){
	cpu_temp=`cat /sys/class/thermal/thermal_zone0/temp`
	gpu_temp=`cat /sys/class/thermal/thermal_zone1/temp`
	gpu_temp=`expr ${gpu_temp} \* 10`
	battery_temp=`cat /sys/class/power_supply/battery/temp`
	battery_temp=`expr ${battery_temp} \* 1000`
	temp_info="`date "+%Y%m%d|%H:%M:%S"`|cpu_temp|$cpu_temp|gpu_temp|$gpu_temp|battery_temp|$battery_temp"
	echo $temp_info
	echo $temp_info >> /userdisk/testlog/temp_info.log
}

# Upload temperature info onto grafana.db
function tempUpload(){
	curl -i -XPOST $url_begin --data-binary $(cat /userdisk/testlog/device_sn)',stuid='$(cat /userdisk/testlog/device_sn)' cpu_temp='$(tail -n 1 /userdisk/testlog/temp_info.log|awk -F"|" '{print $4}')
	curl -i -XPOST $url_begin --data-binary $(cat /userdisk/testlog/device_sn)',stuid='$(cat /userdisk/testlog/device_sn)' gpu_temp='$(tail -n 1 /userdisk/testlog/temp_info.log|awk -F"|" '{print $6}')
	curl -i -XPOST $url_begin --data-binary $(cat /userdisk/testlog/device_sn)',stuid='$(cat /userdisk/testlog/device_sn)' battery_temp='$(tail -n 1 /userdisk/testlog/temp_info.log|awk -F"|" '{print $8}')
}

# Acquiring memory info: mem, buffers, swap
function memGrep(){
	#mem=`free|grep Mem`
	#swap=`free|grep Swap`
	MemAvailable=`cat /proc/meminfo | grep -w MemAvailable | awk '{print $2}'`	
	MemFree=`cat /proc/meminfo | grep -w MemFree | awk '{print $2}'`	
	Buffers=`cat /proc/meminfo | grep -w Buffers | awk '{print $2}'`	
	Cached=`cat /proc/meminfo | grep -w Cached | awk '{print $2}'`		
	SwapCached=`cat /proc/meminfo | grep -w SwapCached | awk '{print $2}'`
	mem_info="`date "+%Y%m%d|%H:%M:%S"`|MemAvailable|`echo ${MemAvailable}`|MemFree|`echo ${MemFree}`|Buffers|`echo ${Buffers}`|Cached|`echo ${Cached}`|SwapCached|`echo ${SwapCached}`"
	echo $mem_info
	echo $mem_info >> /userdisk/testlog/mem_info.log
}

function memMiniapp() {
	PID=`ps | grep -w miniapp | grep -v grep | grep -v /bin/bash | grep miniapp | awk '{print $1}'`
	VmHWM=`cat /proc/${PID}/status | grep VmHWM | awk '{print $2}'`
	VmRSS=`cat /proc/${PID}/status | grep VmRSS | awk '{print $2}'`
	mem_info="`date "+%Y%m%d|%H:%M:%S"`|miniapp|`echo ${PID}`|VmHWM|`echo ${VmHWM}`|VmRSS|`echo ${VmRSS}`"
	if [ $PID -ne $PiD ]
	then echo `date "+%Y%m%d|%H:%M:%S"`"左右发生崩溃，请查看日志！" >> /userdisk/core.log
	PiD=$PID
	fi
	echo $mem_info
	echo $mem_info >> /userdisk/testlog/mem_info_miniapp.log
}

function memResourceManager() {
	PID=`ps | grep -w ResourceManager | grep -v grep | grep -v /bin/bash | grep ResourceManager | awk '{print $1}'`
	VmHWM=`cat /proc/${PID}/status | grep VmHWM | awk '{print $2}'`
	VmRSS=`cat /proc/${PID}/status | grep VmRSS | awk '{print $2}'`
	mem_info="`date "+%Y%m%d|%H:%M:%S"`|ResourceManager|`echo ${PID}`|VmHWM|`echo ${VmHWM}`|VmRSS|`echo ${VmRSS}`"
	echo $mem_info
	echo $mem_info >> /userdisk/testlog/mem_info_ResourceManager.log
}

function memSoundPlayer() {
	PID=`ps | grep -w SoundPlayer | grep -v grep | grep -v /bin/bash | grep SoundPlayer | awk '{print $1}'`
	VmHWM=`cat /proc/${PID}/status | grep VmHWM | awk '{print $2}'`
	VmRSS=`cat /proc/${PID}/status | grep VmRSS | awk '{print $2}'`
	mem_info="`date "+%Y%m%d|%H:%M:%S"`|SoundPlayer|`echo ${PID}`|VmHWM|`echo ${VmHWM}`|VmRSS|`echo ${VmRSS}`"
	echo $mem_info
	echo $mem_info >> /userdisk/testlog/mem_info_SoundPlayer.log
}

function memSoundRecord() {
	PID=`ps | grep -w SoundRecord | grep -v grep | grep -v /bin/bash | grep SoundRecord | awk '{print $1}'`
	VmHWM=`cat /proc/${PID}/status | grep VmHWM | awk '{print $2}'`
	VmRSS=`cat /proc/${PID}/status | grep VmRSS | awk '{print $2}'`
	mem_info="`date "+%Y%m%d|%H:%M:%S"`|SoundRecord|`echo ${PID}`|VmHWM|`echo ${VmHWM}`|VmRSS|`echo ${VmRSS}`"
	echo $mem_info
	echo $mem_info >> /userdisk/testlog/mem_info_SoundRecord.log
}


# Upload memory info onth grafana.db
function memUpload(){
	curl -i -XPOST $url_begin --data-binary $(cat /userdisk/testlog/device_sn)',stuid='$(cat /userdisk/testlog/device_sn)' mem='$(tail -n 1 /userdisk/testlog/mem_info.log|awk -F"|" '{print $4}')
	curl -i -XPOST $url_begin --data-binary $(cat /userdisk/testlog/device_sn)',stuid='$(cat /userdisk/testlog/device_sn)' free='$(tail -n 1 /userdisk/testlog/mem_info.log|awk -F"|" '{print $6}')
	curl -i -XPOST $url_begin --data-binary $(cat /userdisk/testlog/device_sn)',stuid='$(cat /userdisk/testlog/device_sn)' buffers='$(tail -n 1 /userdisk/testlog/mem_info.log|awk -F"|" '{print $8}')
	curl -i -XPOST $url_begin --data-binary $(cat /userdisk/testlog/device_sn)',stuid='$(cat /userdisk/testlog/device_sn)' swap='$(tail -n 1 /userdisk/testlog/mem_info.log|awk -F"|" '{print $10}')
}

# Acquiring cpu info: usr, sys, idle
function cpuGrep(){
	cpu=`top -b -n 1 | grep CPU | head -n 1`
	usr=`echo $cpu|awk '{print $2}'`
	sys=`echo $cpu|awk '{print $4}'`
	idle=`echo $cpu|awk '{print $8}'`
	cpu_info="`date "+%Y%m%d|%H:%M:%S"`|usr|`echo ${usr%\%}`|sys|`echo ${sys%\%}`|idle|`echo ${idle%\%}`"
	echo $cpu_info
	echo $cpu_info >> /userdisk/testlog/cpu_info.log
}

# Upload cpu info onto grafana.db
function cpuUpload(){
	curl -i -XPOST $url_begin --data-binary $(cat /userdisk/testlog/device_sn)',stuid='$(cat /userdisk/testlog/device_sn)' usr='$(tail -n 1 /userdisk/testlog/cpu_info.log|awk -F"|" '{print $4}')
	curl -i -XPOST $url_begin --data-binary $(cat /userdisk/testlog/device_sn)',stuid='$(cat /userdisk/testlog/device_sn)' sys='$(tail -n 1 /userdisk/testlog/cpu_info.log|awk -F"|" '{print $6}')
	curl -i -XPOST $url_begin --data-binary $(cat /userdisk/testlog/device_sn)',stuid='$(cat /userdisk/testlog/device_sn)' idle='$(tail -n 1 /userdisk/testlog/cpu_info.log|awk -F"|" '{print $8}')
}

echo "Record $capture device info every $delay seconds"




###############################################################################################BSP log


function mem_run_uevent_monitor() {
	PID=`ps -w | grep -w run_uevent_monitor | grep -v grep | grep -v guardian_run | awk '{print $1}'`
	VmHWM=`cat /proc/${PID}/status | grep VmHWM | awk '{print $2}'`
	VmRSS=`cat /proc/${PID}/status | grep VmRSS | awk '{print $2}'`
	mem_info="`date "+%Y%m%d|%H:%M:%S"`|run_uevent_monitor|`echo ${PID}`|VmHWM|`echo ${VmHWM}`|VmRSS|`echo ${VmRSS}`"
	echo $mem_info
	echo $mem_info >> /userdisk/testlog/mem_info_run_uevent_monitor.log
}

function mem_run_input_event_monitor() {
	PID=`ps -w | grep -w run_input_event_monitor | grep -v grep | grep -v guardian_run | awk '{print $1}'`
	VmHWM=`cat /proc/${PID}/status | grep VmHWM | awk '{print $2}'`
	VmRSS=`cat /proc/${PID}/status | grep VmRSS | awk '{print $2}'`
	mem_info="`date "+%Y%m%d|%H:%M:%S"`|run_input_event_monitor|`echo ${PID}`|VmHWM|`echo ${VmHWM}`|VmRSS|`echo ${VmRSS}`"
	echo $mem_info
	echo $mem_info >> /userdisk/testlog/mem_info_run_input_event_monitor.log
}

function mem_runCapFrame() {
	PID=`ps | grep -w runCapFrame | grep -v grep | grep -v guardian_run | awk '{print $1}'`
	VmHWM=`cat /proc/${PID}/status | grep VmHWM | awk '{print $2}'`
	VmRSS=`cat /proc/${PID}/status | grep VmRSS | awk '{print $2}'`
	mem_info="`date "+%Y%m%d|%H:%M:%S"`|runCapFrame|`echo ${PID}`|VmHWM|`echo ${VmHWM}`|VmRSS|`echo ${VmRSS}`"
	echo $mem_info
	echo $mem_info >> /userdisk/testlog/mem_info_runCapFrame.log
}

function mem_runWpas() {
	PID=`ps | grep -w runWpas | grep -v grep | grep -v guardian_run | awk '{print $1}'`
	VmHWM=`cat /proc/${PID}/status | grep VmHWM | awk '{print $2}'`
	VmRSS=`cat /proc/${PID}/status | grep VmRSS | awk '{print $2}'`
	mem_info="`date "+%Y%m%d|%H:%M:%S"`|runWpas|`echo ${PID}`|VmHWM|`echo ${VmHWM}`|VmRSS|`echo ${VmRSS}`"
	echo $mem_info
	echo $mem_info >> /userdisk/testlog/mem_info_runWpas.log
}

function mem_runBluez() {
	PID=`ps | grep -w runBluez | grep -v grep | grep -v guardian_run | awk '{print $1}'`
	VmHWM=`cat /proc/${PID}/status | grep VmHWM | awk '{print $2}'`
	VmRSS=`cat /proc/${PID}/status | grep VmRSS | awk '{print $2}'`
	mem_info="`date "+%Y%m%d|%H:%M:%S"`|runBluez|`echo ${PID}`|VmHWM|`echo ${VmHWM}`|VmRSS|`echo ${VmRSS}`"
	echo $mem_info
	echo $mem_info >> /userdisk/testlog/mem_info_runBluez.log
}

function mem_runBlueAlsa() {
	PID=`ps | grep -w runBlueAlsa | grep -v grep | grep -v guardian_run | awk '{print $1}'`
	VmHWM=`cat /proc/${PID}/status | grep VmHWM | awk '{print $2}'`
	VmRSS=`cat /proc/${PID}/status | grep VmRSS | awk '{print $2}'`
	mem_info="`date "+%Y%m%d|%H:%M:%S"`|runBlueAlsa|`echo ${PID}`|VmHWM|`echo ${VmHWM}`|VmRSS|`echo ${VmRSS}`"
	echo $mem_info
	echo $mem_info >> /userdisk/testlog/mem_info_runBlueAlsa.log
}

function mem_runWifiMgr() {
	PID=`ps | grep -w runWifiMgr | grep -v grep | grep -v guardian_run | awk '{print $1}'`
	VmHWM=`cat /proc/${PID}/status | grep VmHWM | awk '{print $2}'`
	VmRSS=`cat /proc/${PID}/status | grep VmRSS | awk '{print $2}'`
	mem_info="`date "+%Y%m%d|%H:%M:%S"`|runWifiMgr|`echo ${PID}`|VmHWM|`echo ${VmHWM}`|VmRSS|`echo ${VmRSS}`"
	echo $mem_info
	echo $mem_info >> /userdisk/testlog/mem_info_runWifiMgr.log
}

function mem_runBtMgr() {
	PID=`ps | grep -w runBtMgr | grep -v grep | grep -v guardian_run | awk '{print $1}'`
	VmHWM=`cat /proc/${PID}/status | grep VmHWM | awk '{print $2}'`
	VmRSS=`cat /proc/${PID}/status | grep VmRSS | awk '{print $2}'`
	mem_info="`date "+%Y%m%d|%H:%M:%S"`|runBtMgr|`echo ${PID}`|VmHWM|`echo ${VmHWM}`|VmRSS|`echo ${VmRSS}`"
	echo $mem_info
	echo $mem_info >> /userdisk/testlog/mem_info_runBtMgr.log
}

function mem_runOtaMgr() {
	PID=`ps | grep -w runOtaMgr | grep -v grep | grep -v guardian_run | awk '{print $1}'`
	VmHWM=`cat /proc/${PID}/status | grep VmHWM | awk '{print $2}'`
	VmRSS=`cat /proc/${PID}/status | grep VmRSS | awk '{print $2}'`
	mem_info="`date "+%Y%m%d|%H:%M:%S"`|runOtaMgr|`echo ${PID}`|VmHWM|`echo ${VmHWM}`|VmRSS|`echo ${VmRSS}`"
	echo $mem_info
	echo $mem_info >> /userdisk/testlog/mem_info_runOtaMgr.log
}




while true;
do
	if [[ "$capture" == "full" ]]; then
		# Record full device info under stability-test scenario
		batteryGrep
		tempGrep
		memGrep
		memMiniapp
		memResourceManager
		memSoundPlayer
		memSoundRecord
		cpuGrep
		mem_run_uevent_monitor
		mem_run_input_event_monitor
		mem_runCapFrame
		mem_runWpas
		mem_runBluez
		mem_runBlueAlsa
		mem_runWifiMgr
		mem_runBtMgr
		mem_runOtaMgr
		batteryUpload
		tempUpload
		memUpload
		cpuUpload
	else
		# Record partial device info under consumption-test scenario
		batteryGrep
		tempGrep
		memGrep
		memMiniapp
		memResourceManager
		memSoundPlayer
		memSoundRecord
		cpuGrep
		mem_run_uevent_monitor
		mem_run_input_event_monitor
		mem_runCapFrame
		mem_runWpas
		mem_runBluez
		mem_runBlueAlsa
		mem_runWifiMgr
		mem_runBtMgr
		mem_runOtaMgr
	fi

	# Time between records
	echo "The gap between two records is $delay seconds..."
	sleep $delay
done
