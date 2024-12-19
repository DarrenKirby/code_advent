#!/usr/bin/bash

# Part 1
FILE=./input/input2.txt

checksum=0

while read -r line; do
    numbers=($line)

    largest=${numbers[0]}
    smallest=${numbers[0]}

    for num in "${numbers[@]}"; do
    if (( num > largest )); then
        largest=$num
    fi

    if (( num < smallest )); then
        smallest=$num
    fi
    done

    difference=$(( largest - smallest ))
    checksum=$(( checksum + difference ))

done < $FILE

echo $checksum

# Part 2

checksum=0

while read -r line; do
    numbers=($line)

    for f_num in "${numbers[@]}"; do
        for s_num in "${numbers[@]}"; do
            if (( $f_num == $s_num )); then
                continue
            else
                result=$(( f_num % s_num ))
                if (( result == 0 )); then
                    ans=$(( f_num / s_num ))
                    checksum=$(( checksum + ans ))
                    break
                fi
            fi
        done
    done
done < $FILE

echo $checksum

