#!/usr/bin/env bash

#Part 1
FILE=./input/input6.txt

while read -r line; do
    mem_banks=($line) # Split line into array
done < $FILE

seen=()
idx=0


while true; do
    # add current array values to seen
    curr_arr_vals_s=$(printf "%s-"  "${mem_banks[@]}")

    if [[ " ${seen[*]} " =~ [[:space:]]${curr_arr_vals_s}[[:space:]] ]]; then
        echo "${idx}"
        last_state=( ${mem_banks[@]} )
        break
    else
        seen+=( $curr_arr_vals_s )
    fi

    largest=${mem_banks[0]}
    largest_i=0

    # Find the largest value and its index
    for i in "${!mem_banks[@]}"; do
        if (( mem_banks[i] > largest )); then
            largest=${mem_banks[i]}
            largest_i=$i
        fi
    done

    # Reset the largest value to zero
    mem_banks[$largest_i]=0

    ci=$((largest_i + 1))
    # loop 'largest' times
    for j in $(seq $largest)
    do
        if [[ $ci == ${#mem_banks[@]} ]]; then
            ci=0
        fi
        (( mem_banks[$ci]++ ))
        (( ci++ ))

    done
    (( idx++ ))
done

# Part 2

mem_banks=( ${last_state[@]} )      #(0 14 13 12 11 10 8 8 6 6 5 3 3 2 1 10)

seen=()
idx=0


while true; do
    # add current array values to seen
    curr_arr_vals_s=$(printf "%s-"  "${mem_banks[@]}")

    if [[ " ${seen[*]} " =~ [[:space:]]${curr_arr_vals_s}[[:space:]] ]]; then
        echo "${idx}"
        echo "${mem_banks[@]}"
        exit
    else
        seen+=( $curr_arr_vals_s )
    fi

    largest=${mem_banks[0]}
    largest_i=0

    # Find the largest value and its index
    for x in "${!mem_banks[@]}"; do
        if (( mem_banks[x] > largest )); then
            largest=${mem_banks[x]}
            largest_i=$x
        fi
    done

    # Reset the largest value to zero
    mem_banks[$largest_i]=0

    ci=$((largest_i + 1))
    # loop 'largest' times
    for y in $(seq $largest)
    do
        if [[ $ci == ${#mem_banks[@]} ]]; then
            ci=0
        fi
        (( mem_banks[$ci]++ ))
        (( ci++ ))

    done
    (( idx++ ))
done

