import os
import sys
import time

tmp_path = "tmp"

error_message = "Usage: python3 open.py filename persistance-time (suffix time with s for seconds m for minutes and h for hours)"

error = False

def exit():
	sys.exit(error_message)

#Check inputs
if len(sys.argv) == 1:
	exit()

if sys.argv[1] == "-h":
	exit()

file_name = sys.argv[1]

if os.path.isfile(file_name) != True:
	print("File not found ... ")
	exit()

persist_time = sys.argv[2]

try:
	persist_time_short = int(persist_time[:1])
	persist_time_suffix = str(persist_time[-1])
	if persist_time_suffix == "s":
		persist_time = persist_time_short
	elif persist_time_suffix == "m":
		persist_time = persist_time_short*60
	elif persist_time_suffix == "h":
		persist_time = persist_time_short*3600
	else:
		print("Please enter a valid time suffix")
		exit()
except:
	print("Please enter a valid time")
	exit()


if os.path.exists(tmp_path) != True:
	os.system("mkdir " + tmp_path)

open_time = time.time()

decrypt_string = "gpg -d -o "+tmp_path+"/"+file_name+".zip "+file_name
os.system(decrypt_string)

exit_cond = False

while exit_cond != True:
	if time.time() > open_time+persist_time:
		os.system("rm -rf "+tmp_path)
		exit_cond = True
	else:
		time.sleep(5)