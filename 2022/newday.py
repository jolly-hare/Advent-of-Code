import os
import shutil
import requests

day_num = "3"

cookie = {'session': 'SESSION'}
header = {"User-Agent": "user agent string - include repo, version, contact details"}
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
        with open('aoc_template.py') as f:
            tmp = f.read()
            tmp2 = tmp.replace("$0X", day_zeroed)
        with open(solutionfile, "w") as f2:
            f2.write(tmp2)
    if not os.path.exists(inputfile):
        resp = requests.get(f'https://adventofcode.com/2022/day/{str(day_num)}/input', cookies=cookie, headers=header)
        with open(f"{inputfile}", 'w') as f:
            f.write(resp.text.strip("\n"))
    else:
        print('input file exists, not requesting again')
else:
    print("that day's directory exists, skipping")
