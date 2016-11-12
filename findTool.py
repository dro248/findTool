#! /usr/bin/python2

# searches /usr/bin/ for a tool matching the description of argv[1]
import sys
import subprocess



class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

# TODO: not implemented yet (coloring search term within header)
def find_str(s, char):
    index = 0
    if char in s:
        c = char[0]
        for ch in s:
            if ch == c:
                if s[index:index+len(char)] == char:
                    return index
            index += 1
    return -1


def headerify(header, search_term):
	return bcolors.BOLD + bcolors.OKGREEN + header + bcolors.ENDC


# lengthens all results_list strings to the longest one
def norm1(list):
	MAX_WORD = max(results_list, key=len)
	MAX_LEN = len(MAX_WORD)
	for i in range(0, len(list)):
		if len(list[i]) < MAX_LEN:
			diff = MAX_LEN - len(list[i])
			list[i] = list[i] + diff*" "
	return list
###################

if len(sys.argv) < 2:
    exit()


PARAM = sys.argv[1]

# CHECK: sanitize string
if PARAM.find(';') != -1:
	print "ERROR: Dangerous character found (';')"
	exit()

cmd = "ls /usr/bin/ | grep " + PARAM

try:
	raw_results = subprocess.check_output(cmd, shell=True)
	results_list = raw_results.split('\n')
	results_list.remove('')
except:
	exit()

# Normalize length of each word (with longest word)
results_list = norm1(results_list)

# Print Results
for item in results_list:
	try:
	    mycmd = "whatis " + item
	    item_def = subprocess.check_output(mycmd, shell=True)
	    print headerify(item, PARAM), bcolors.FAIL + item_def[:-1] + bcolors.ENDC
	except:
		continue