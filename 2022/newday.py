import os
import shutil
import requests

day_num = "3"
cookie = {'session': 'SESSION'}
header = {"User-Agent": "USER AGENT INFO - REPO VERSION EMAIL USERNAME"}
if len(day_num) == 1:
    day_zeroed = "0" + day_num
else:
    day_zeroed = day_num
if not os.path.exists(day_zeroed):
    os.mkdir(day_zeroed)
    inputfile = os.path.join(day_zeroed, day_zeroed + '.input')
    examplefile = os.path.join(day_zeroed, day_zeroed + '.example')
    solutionfile = os.path.join(day_zeroed, day_zeroed + '.py')
    if not os.path.exists(examplefile):
        shutil.copy('0X.example', examplefile)
    if not os.path.exists(solutionfile):
        shutil.copy('aoc_template.py', solutionfile)
    if not os.path.exists(inputfile):
        resp = requests.get(f'https://adventofcode.com/2022/day/{str(day_num)}/input', cookies=cookie, headers=header)
        with open(f"{inputfile}", 'w') as f:
            f.write(resp.text.strip("\n"))
    else:
        print('input file exists, not requesting again')
else:
    print("that day's directory exists, skipping")
