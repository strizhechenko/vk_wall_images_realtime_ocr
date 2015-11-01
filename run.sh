#!/opt/local/bin/bash

export PATH=$PATH:/opt/local/bin/

link2text() {
	wget -q "$1" -O input.jpg
	tesseract input.jpg output -l eng -psm 6 2>/dev/null
	tr -d ' ' < output.txt
}

python -u vk_wall_monitor.py | while read line; do
	printf "\a"
	out="$(link2text "$line")"
	echo "$out"
	echo "$out" | pbcopy
	echo "tell application \"System Events\" to keystroke \"$out\"" | osascript
done
