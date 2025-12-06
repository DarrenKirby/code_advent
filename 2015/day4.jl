using MD5

# Part 1
# actual key obscured
key = "iwrupvqb"
let counter = 1
    while true
        string_to_check = "$key$counter"
        if bytes2hex(md5(string_to_check))[1:5] == "00000"
            println(counter)
            break
        end
        counter += 1
    end
end

# Part 2
# actual key obscured
key = "iwrupvqb"
let counter = 1
    while true
        string_to_check = "$key$counter"
        if bytes2hex(md5(string_to_check))[1:6] == "000000"
            println(counter)
            break
        end
        counter += 1
    end
end
