#/bin/bash
# @author: liuzhe
# @date: 2019-07-04

START_TIME=$(date "+%s")
#echo $START_TIME
COUNT=1
OCR_COUNT=0
OCRIR_COUNT=0
ASR_COUNT=0
SLIP_COUNT=0
CLICK_COUNT=0
WRITE_COUNT=0
TESTLOG=/data/youdao_test/testlog.txt
mkdir -p /data/youdao_test

#生成随机数
function rand() {
	min=$1
	max=$(($2 - $min + 1))
	num=$(date +%s%N)
	echo $(($num % $max + $min))
}

#OCR扫描
function ocr_test() {
	echo "--Run ocr testing" >> $TESTLOG
	len_onoff.sh on
	send_event camera press
	#扫描时间
	sleep 4
	send_event camera release
	len_onoff.sh off
	#抬笔至距离下次扫描等待时间
	sleep 15
	OCR_COUNT=$(expr $OCR_COUNT + 1)
}

#口算扫描 转速20
function math_test() {
	echo "--Run ocr testing" >> $TESTLOG
	len_onoff.sh on
	send_event camera press
	#扫描时间
	sleep 2
	send_event camera release
	len_onoff.sh off
	#抬笔至距离下次扫描等待时间
	sleep 4
	OCR_COUNT=$(expr $OCR_COUNT + 1)
}

#作文批改
function write_test() {
	echo "--Run write testing" >> $TESTLOG
	len_onoff.sh on
	send_event camera press
	#扫描时间
	sleep 6
	send_event camera release
	len_onoff.sh off
	#抬笔至距离下次扫描等待时间
	sleep 3
	#点击提交按钮
	send_event touch press 333 33
	send_event touch release
	sleep 4
	WRITE_COUNT=$(expr $WRITE_COUNT + 1)
}

# 点查
function ocrcc_test() {
	echo "--Run ocrIR testing" >> $TESTLOG
	len_onoff.sh on IR
	send_event camera press
	sleep 0.1
	send_event camera release
	len_onoff.sh off IR
	len_onoff.sh on
	sleep 0.2
	len_onoff.sh off
	#抬笔至距离下次扫描等待时间
	sleep 4
	OCRIR_COUNT=$(expr $OCRIR_COUNT + 1)
}
# 点读
function ocrcr_test() {
	echo "--Run ocrIR testing" >> $TESTLOG
	len_onoff.sh on IR
	send_event camera press
	sleep 0.2
	send_event camera release
	len_onoff.sh off IR
	len_onoff.sh on
	sleep 0.5
	len_onoff.sh off
	#抬笔至距离下次扫描等待时间
	sleep 15
	OCRIR_COUNT=$(expr $OCRIR_COUNT + 1)
}
# 点读跟读
function ocrir_test() {
	echo "--Run ocrIR testing" >> $TESTLOG
	len_onoff.sh on IR
	send_event camera press
	sleep 0.2
	send_event camera release
	len_onoff.sh off IR
	len_onoff.sh on
	sleep 0.5
	len_onoff.sh off
	#抬笔至距离下次扫描等待时间
	sleep 25
	OCRIR_COUNT=$(expr $OCRIR_COUNT + 1)
}


#滑屏，例子为从右向左滑动
function slip() {
	#slip_num=$(rand 5 10)
	slip_num=4
	echo "--Run slip testing " $slip_num " times" >> TESTLOG
	for i in `seq $slip_num ` ;do
		x1=$(rand 0 170)
		y1=$(rand 0 320)
		x2=$(rand 0 170)
		y2=$(rand 0 320)
		echo "--$i slip testing from " $x1 $y1 " to " $x2 $y2 >> $TESTLOG
		send_event touch press $x1 $y1
		send_event touch slip $x2 $y2
		send_event touch release
		sleep 1
	done
	SLIP_COUNT=$(expr $SLIP_COUNT + $slip_num)
}

#开启语音识别
function asr_test() {
	echo "--Run asr_test testing" >> $TESTLOG
	send_event asr press
	sleep $(rand 3 5)
	send_event asr release
	sleep $(rand 3 5)
	ASR_COUNT=$(expr $ASR_COUNT + 1)
}

#开始点击操作
function click() {
	click_num=$(rand 5 10)
	echo "--Run click testing " $click_num " times" >> TESTLOG
	for i in `seq $click_num ` ;do
		x=$(rand 0 170)
		y=$(rand 0 320)
		echo "--$i click testing click " $x $y >> $TESTLOG
		send_event touch press $x $y
		send_event touch release
		sleep 0.5
	done
		CLICK_COUNT=$(expr $CLICK_COUNT + $click_num)
}

function monkey_test() {
	last_num=$(date "+%N")
	#echo '123-1 456-2 78-3 90-4 ' ${last_num: -1}
	result1=$(echo 12 | grep ${last_num: -1})
	result2=$(echo 34 | grep ${last_num: -1})
	result3=$(echo 56 | grep ${last_num: -1})
	result4=$(echo 78 | grep ${last_num: -1})
	if [[ "$result1" != "" ]]; then
		asr_test
	elif [[ "$result2" != "" ]]; then
		ocr_test
	elif [[ "$result3" != "" ]]; then
		slip
	else
		click
	fi
}

#持续运行下面的命令
while [ true ]; do
	check_results=`ps -l | grep "YoudaoDictPen"`
	value=${check_results}
	result=$(echo $value | grep 'platform')
	if [[ "$result" != "" ]]; then
		#running_time=$($(date +%s) - $START_TIME)
		echo "$(date '+%Y%m%d-%H%M%S') QT is still alive " >> $TESTLOG
		if [[ $1 == 'ocr' ]];then
			echo 'Starting ' $COUNT 'unittests, Already : OCR ' $OCR_COUNT  >> $TESTLOG
			ocr_test
		elif [[ $1 == 'math' ]];then
			echo 'Starting ' $COUNT 'unittests, Already : ASR ' $MATH_COUNT  >> $TESTLOG
			math_test
		elif [[ $1 == 'asr' ]];then
			echo 'Starting ' $COUNT 'unittests, Already : ASR ' $ASR_COUNT  >> $TESTLOG
			asr_test
		elif [[ $1 == 'ocrir' ]];then
			echo 'Starting ' $COUNT 'unittests, Already : OCRIR ' $OCRIR_COUNT  >> $TESTLOG
			ocrir_test
		elif [[ $1 == 'ocrcc' ]];then
			echo 'Starting ' $COUNT 'unittests, Already : CLICK ' $CLICK_COUNT  >> $TESTLOG
			ocrcc_test
		elif [[ $1 == 'ocrcr' ]];then
			echo 'Starting ' $COUNT 'unittests, Already : CLICK ' $CLICK_COUNT  >> $TESTLOG
			ocrcr_test
		elif [[ $1 == 'write' ]];then
			echo 'Starting ' $COUNT 'unittests, Already : WRITE ' $WRITE_COUNT  >> $TESTLOG
			write_test
		else
			echo 'Starting ' $COUNT 'unittests, Already : OCR ' $OCR_COUNT ', ASR ' $ASR_COUNT ', SLIP ' $SLIP_COUNT ', CLICK ' $CLICK_COUNT ', WRITE ' $WRITE_COUNT ', OCRIR ' $OCRIR_COUNT >> $TESTLOG
			monkey_test
		fi
		COUNT=$(expr $COUNT + 1)
		#sleep 598
		sync
	else
		echo "$(date '+%Y%m%d-%H%M') QT is crash" >> $TESTLOG
		sync
		break
	fi
	
done

