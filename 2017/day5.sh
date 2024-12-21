#!/usr/bin/bash

# Part 1
FILE=./input/input5.txt

instr=()
while IFS= read -r line; do
    instr+=("$line")
done < "$FILE"

steps=0
idx=0
while true
do
    i=${instr[$idx]}
    # We've broken out of the array
    if [[ $i == "" ]]; then
        break
    fi

    (( instr[$idx]++ ))
    idx=$(( idx + i ))
    (( steps++ ))
    #echo "idx: ${idx}, i: ${i} steps: ${steps}"
done

echo $steps

# Part 2
# This took about 20 minutes to converge on a quad-core
# 2.40GHz processor. I also wasted another 20 minutes
# because I thought for sure it was an infinite loop haha
instr=()
while IFS= read -r line; do
    instr+=("$line")
done < "$FILE"

steps=0
idx=0
while true
do
    i=${instr[$idx]}
    # We've broken out of the array
    if [[ $i == "" ]]; then
        break
    fi
    # Determine jump size
    if [ $i -ge 3 ]; then
        (( instr[$idx]-- ))
    else
        (( instr[$idx]++ ))
    fi

    idx=$(( idx + i ))
    (( steps++ ))
    #echo "idx: ${idx}, i: ${i} steps: ${steps}"
done

echo $steps

