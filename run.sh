while true
do
	# won't terminate the loop even encoutering error
    date
	python ./nb/nbexp_bilibili.py
    python ./nb/nbexp_anilist.py
	sleep 15m
done
