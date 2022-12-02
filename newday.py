import os
import shutil
import requests

day_num = "1"

cookie = {'session': SESSION_COOKIE}
header = {"User-Agent": REPO, VERSION, EMAIL/USERNAME}
if len(day_num) == 1:
    day_zeroed = "0" + day_num
else:
    day_zeroed = day_num
if not os.path.exists(day_zeroed):
    os.mkdir(day_zeroed)
    shutil.copy('0X.example', os.path.join(day_zeroed, day_zeroed + '.example'))
    shutil.copy('empty.py', os.path.join(day_zeroed, day_zeroed + '.py'))
    resp = requests.get(f'https://adventofcode.com/2022/day/{str(day_num)}/input', cookies=cookie, headers=header)
    with open(f"{os.path.join(day_zeroed, day_zeroed + '.input')}", 'w') as f:
        f.write(resp.text.strip("\n"))
