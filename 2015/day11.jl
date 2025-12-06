
function next_pass(s::String)
    chars = collect(s)  # Vector{Char}
    i = length(chars)

    while i > 0
        if chars[i] == 'z'
            chars[i] = 'a'
            i -= 1
        else
            chars[i] = Char(chars[i] + 1)
            return String(chars)
        end
    end

    # overflow case (zzzzzzzz -> aaaaaaaa)
    return String(chars)
end

function check_valid(s::String)
    if occursin("i", s) || occursin("o", s) || occursin("l", s)
        return false
    end
    re = r"(.)\1.*(?!\1)(.)\2"
    if !occursin(re, s)
        return false
    end
    for i in range(1, length(s) - 2)
        char1 = s[i]
        if s[i+1] == char1 + 1 && s[i+2] == char1 + 2 
            return true
        end
    end
    return false
end

# part 1
let passwd = "vzbxkghb"
    while check_valid(passwd) == false
        passwd = next_pass(passwd)
    end
    println(passwd)
end

# part 2
let passwd = "vzbxxzaa"
    while check_valid(passwd) == false
        passwd = next_pass(passwd)
    end
    println(passwd)
end
