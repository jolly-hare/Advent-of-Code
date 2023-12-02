# Advent-Of-Code-2023
My code for the Advent Of Code 2023 programming puzzles.


Advent Of Code (https://adventofcode.com/) is a registered trademark in the United States. All copyrights for puzzle content and input data are held by Eric Wastl, https://twitter.com/ericwastl and https://github.com/topaz.

# How to Use
1. Modify `newday.py`
    - define *your* AoC API session string in _"cookie"_
    - define *your* User-Agent string in _"header"_
    - define _"year_num"_ and _"day_num"_ for the desired year and day
3. Run `newday.py` within the directory where the new daily directories are to be created
    - creates a new directory for the defined day
    - creates dynamic `aoc_template.py` as `{dayX}.py`
    - creates an empty example file as `{dayX}.example`
    - downloads *your* data from AoC as `{dayX}.input`
4. Copy your example data into `{dayX}.example` and modify `{dayX}.py` to solve for the day's problem


# My Goal
Hoping to get at least 20 stars (1 star for solving each of two parts) of the 50 stars possible.

# My Status
Currently: 4 stars

Bulding from 2022, I'm starting 2023 with:

:heavy_check_mark: Template starter script to build from each day


:heavy_check_mark: A "new day" script that creates a directory, files, and gets puzzle input


&#9744; Have `new_day.py` autopopulate `X.example` and `X.py` with AoC problem page's example data and test answers


# Why
Starting with a mostly blank state because I need the practice. I'll try to post my daily solutions if I find the correct answer(s). In later days, I may spend some time cleaning up past solutions to more optimized or elegant alternate solutions.
