# This is the slow-ass, inefficient version that I originally
# wrote to solve part 1. It will notsolve part 2 before the
# heat-death of the universe.

function permutate(s)
    ns = ""
    l = length(s)
    ptr = 1
    while ptr <= l
        char = s[ptr]
        if ptr == l
            ns *= "1$char"
            ptr += 1
        elseif s[ptr] == s[ptr+1]
            if s[ptr] == s[ptr+2]
                # 3 in a row
                ns *= "3$char"
                ptr += 3
            else
                # 2 in a row
                ns *= "2$char"
                ptr += 2
            end
        else
            # one in a row
            ns *= "1$char"
            ptr += 1
        end
    end
    return ns
end

# So instead....
# Represent look-and-say sequences as a vector of (count, digit)
struct Block
    n::Int
    c::Char
end

function rle(s::String)
    out = Block[]
    i = 1
    while i <= length(s)
        c = s[i]
        j = i
        while j ≤ length(s) && s[j] == c
            j += 1
        end
        push!(out, Block(j-i, c))
        i = j
    end
    return out
end

function expand(blocks)
    out = Block[]
    for b in blocks
        # “n c” turns into the characters of n, then c
        digits = string(b.n)
        for ch in digits
            # count=1 for each digit of n
            push!(out, Block(1, ch))
        end
        push!(out, Block(1, b.c))
    end
    # merge adjacent blocks of same char
    merged = Block[]
    for b in out
        if !isempty(merged) && merged[end].c == b.c
            merged[end] = Block(merged[end].n + b.n, b.c)
        else
            push!(merged, b)
        end
    end
    return merged
end

function block_length(blocks)
    s = 0
    for b in blocks
        s += b.n
    end
    return s
end

# Part 1
let blocks = rle("1321131112")
    for _ in 1:40
        blocks = expand(blocks)
    end
    println(block_length(blocks))
end

# Part 1
let blocks = rle("1321131112")
    for _ in 1:50
        blocks = expand(blocks)
    end
    println(block_length(blocks))
end
