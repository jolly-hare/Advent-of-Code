import os
import shutil
import requests

year_num = "2022"
day_num = "6"

url = f'https://adventofcode.com/{year_num}/day/{day_num}/input'
cookie = {'session': 'SESSION cookie'}
header = {'User-Agent': 'repo, version, your contact details'}
if len(day_num) == 1:
    day_zeroed = "0" + day_num
else:
    day_zeroed = day_num
if not os.path.exists(day_zeroed):
    os.mkdir(day_zeroed)
    print(f'new directory created for day {day_zeroed}')
    inputfile = os.path.join(day_zeroed, day_zeroed + '.input')
    examplefile = os.path.join(day_zeroed, day_zeroed + '.example')
    solutionfile = os.path.join(day_zeroed, day_zeroed + '.py')
    if not os.path.exists(examplefile):
        with open(examplefile, 'x') as f:
            pass
        print(f'new empty example file created as: {examplefile}')
    if not os.path.exists(solutionfile):
        with open('aoc_template.py') as f:
            tmp = f.read()
            tmp2 = tmp.replace("$0X", day_zeroed)
        with open(solutionfile, "w") as f2:
            f2.write(tmp2)
            print(f'new solution template file created as: {solutionfile}')
    if not os.path.exists(inputfile):
        resp = requests.get(url=url, cookies=cookie, headers=header)
        with open(f"{inputfile}", 'w') as f:
            f.write(resp.text.strip("\n"))
            print(f'downloaded input data for day {day_zeroed}')
else:
    print("that day's directory exists, skipping")
