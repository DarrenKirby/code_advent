#!/usr/bin/bash

# Part 1
FILE=./input/input.txt
{
read input
} < $FILE

score=0

lastchar=""
for (( i=0; i<${#input}; i++ )); do
    if [[ $lastchar ==  ${input:i:1} ]]; then
        score=$(( score + $lastchar ))
    fi
    lastchar=${input:i:1}
done

# The array is 'circular', so last and first num go together
score=$(( score + $lastchar ))
echo $score

# Part 2
FILE=./input/input.txt
{
read input
} < $FILE

score=0

# offset = length / 2
offset=$(( ${#input} / 2 ))

for (( i=0; i<${#input}; i++ )); do
    offset_i=$(( i + offset ))
    if [[ $offset_i > ${#input} ]]; then
        offset_i=$(( offset_i - ${#input} ))
    fi
    if [[ ${input:i:1} ==  ${input:offset_i:1} ]]; then
        score=$(( score + ${input:i:1} ))
    fi
    lastchar=${input:i:1}
done

# The array is circular, so last number goes with 0 + offset
if [[ $lastchar == ${input:offset:1} ]]; then
    score=$(( score + $lastchar ))
fi

echo $score
