#! /bin/sh
# @author:Vincent
# @created:2021-06-10
# --------------------
# @version 1.0
# 1. ASR scenery - run asr recognition repeatedly
# 2. Quiz scenery - run quizing and answering repeatedly
# 3. Screen_on scenery - keep the main screen lights on

mkdir /data/testlog
touch /data/testlog/monkey.log
asr_count=0
quiz_count=0

function monkey_log(){
	echo $(date "+%Y%m%d|%H:%M:%S")\|$* >> /data/testlog/monkey.log
}

function click(){
	send_event touch press $1 $2
	send_event touch release
	sleep 1
}

function slip_to(){
	send_event touch press $1 $2
	send_event touch slip $3 $4
	send_event touch release
	sleep 1
}

function asr(){
	send_event menu press
	sleep 10
	send_event menu release
	sleep 10
}

function quiz(){
	click 207 197
	sleep 2
	click 431 34
	sleep 2
	click 207 104
	sleep 2
	slip_to 224 251 213 625
	sleep 2
	slip_to 219 255 264 545
	sleep 2
	click 223 465
	sleep 2
	click 180 233
	sleep 2
	click 255 584
	sleep 2
	click 156 585
	sleep 2
	click 206 478
	sleep 4
	click 240 249
	sleep 2
	click 242 251
	sleep 2
	click 237 270
	sleep 2
	click 235 269
	sleep 2
	click 244 253
	sleep 2
}

function speed(){
	click 81 577
	sleep 30
	click 159 573
	sleep 30
	click 232 565
	sleep 30
	click 325 566
	sleep 30
	click 409 579
	sleep 30
}

function screen_on(){
	click 250 40
	sleep 30
}

function back_home(){
	send_event menu press
	send_event menu release
	sleep 0.1
	send_event menu press
	send_event menu release
	sleep 3
	send_event menu press
	send_event menu release
	sleep 0.1
	send_event menu press
	send_event menu release
	sleep 2
}

function mix(){
	# Play music for 5 mins
	slip_to 117 356 414 360
	sleep 2
	playLoop=0
	while [[ $playLoop -lt 11 ]]; do
		playLoop=`expr $playLoop + 1`
		screen_on
	done
	
	# Run ASR test in Sound-Player for 5 mins
	click 175 625
	sleep 2
	click 175 625
	sleep 2
	click 175 625
	sleep 2
	asrLoop=0
	while [[ $asrLoop -lt 31 ]]; do
		asrLoop=`expr $asrLoop + 1`
		asr
	done
	
	# Run ASR tests in AI-Speaking-Practice for 5 mins
	back_home
	click 221 325
	sleep 2
	click 218 586
	sleep 2
	click 195 152
	sleep 30
	asrLoop2=0
	while [[ $asrLoop2 -lt 30 ]]; do
		asrLoop2=`expr $asrLoop2 + 1`
		asr
	done
	back_home
	click 213 578
	sleep 2

	# Answering puzzles in Level-Listening for 5 mins
	back_home
	answerLoop=0
	while [[ $answerLoop -lt 15 ]]; do
		answerLoop=`expr $answerLoop + 1`
		back_home
		quiz
	done

	# Keep the light on for 5 mins
	back_home
	lightLoop=0
	while [[ $lightLoop -lt 11 ]]; do
		lightLoop=`expr $lightLoop + 1`
		screen_on
	done
	slip_to 117 356 414 360
	sleep 2
	send_event pause press
	send_event pause release
	sleep 2
}


while [[ true ]]; do
	case $1 in
		# Run ASR tests in AI-Speaking-Practice
		asr)	
		asr
		monkey_log "asr test times: $asr_count"
		;;
		
		# Run answer tests in Level-Listening
		quiz)	
		back_home
		quiz
		quiz_count=`expr $quiz_count + 1`
		monkey_log "quiz test times: $quiz_count"
		;;
		
		# Keep the screen light on
		light)	
		screen_on
		;;
		
		# Run speed switching tests in Sound-Player
		speed)	
		back_home
		slip_to 117 356 414 360
		sleep 2
		click 430 618
		sleep 2
		slip_to 222 538 219 203
		sleep 2
		speed
		;;

		# Mixed scenarios where every active moves were tested
		mix)	
		back_home
		mix
		;;
		
		# Return the error info when using this script
		$*)
		echo "Wrong parameter - $*"
		echo "Acceptable paras includes: asr, quiz, light, speed, mix"
		exit 1
	esac
done

