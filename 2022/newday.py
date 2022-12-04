import os
import shutil
import requests

day_num = "3"

cookie = {'session': '53616c7465645f5f5a1042cc185996f38cbee45ad106b68477257c0431043ab0f717899549dab741f633a39c654f9bdc03c75364140b53ca0a861dd99f44d972'}
header = {"User-Agent": "github.com/jolly-hare/Advent-of-Code-2022; version 1.0; contact twitter @ts_hare"}
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
