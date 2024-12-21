#!/usr/bin/bash

# Part 1
FILE=./input/input4.txt

good_pass=0

while read -r line; do
    n=`echo $line | tr " " "\n" | wc -l`
    nuniq=`echo $line | tr " " "\n" | sort | uniq | wc -l`
    if (( n == nuniq )); then
        good_pass=$(( good_pass + 1 ))
    fi
done < $FILE

echo $good_pass

# Part 2

good_pass=0
while read -r line; do
    arr=()
    for word in $line; do
        sortedword=$( fold -w1 <<< "$word" | sort | tr -d '\n' )
        arr+=("$sortedword")
    done
    n=`echo "${arr[@]}" | wc -w`
    nuniq=`echo "${arr[@]}" | tr ' ' '\n' | sort | uniq | wc -w`
    if (( n == nuniq )); then
        good_pass=$(( good_pass + 1 ))
    fi
done < $FILE

echo $good_pass

