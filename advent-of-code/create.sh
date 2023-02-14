#!/bin/bash
CURRENT_DATE=$(date +%_d)
#CURRENT_DATE="${CURRENT_DATE## }"
CURRENT_DATE="25"
if [ -f "ex$CURRENT_DATE.py" ]; then
    echo -e "-- \x1B[33;1mDEMO\x1B[0m"
    cat input/e_ex$CURRENT_DATE.txt | python3 ex$CURRENT_DATE.py
    echo -e ""
    echo -e "-- \x1B[33;1mREAL\x1B[0m"
    cat input/ex$CURRENT_DATE.txt | python3 ex$CURRENT_DATE.py
else
    curl -b "session=<secret>" https://adventofcode.com/2022/day/$CURRENT_DATE/input > input/ex$CURRENT_DATE.txt
    cp base.py ex$CURRENT_DATE.py && code ex$CURRENT_DATE.py input/e_ex$CURRENT_DATE.txt
fi