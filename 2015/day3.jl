data = open("./input/day3.txt") do file
    read(file, String)
end

#  Part 1
function part_one(d)
    seen = Set()
    pos = [0,0]
    push!(seen, pos)

    for char in split(d, "")
        if char == "^"
            pos += [-1,0]
            push!(seen, pos)
        elseif char == ">"
            pos += [0,1]
            push!(seen, pos)
        elseif char == "<"
            pos += [0,-1]
            push!(seen, pos)
        elseif char == "v"
            pos += [1,0]
            push!(seen, pos)
        end
    end
    return seen
end
println(length(part_one(data)))

# Part 2
function part_two()
    seen = Set()
    santa = [0,0]
    robo_santa = [0,0]
    push!(seen, santa)

    santa_turn = true
    for char in split(data, "")
        if santa_turn
            if char == "^"
                santa += [-1,0]
                push!(seen, santa)
            elseif char == ">"
                santa += [0,1]
                push!(seen, santa)
            elseif char == "<"
                santa += [0,-1]
                push!(seen, santa)
            elseif char == "v"
                santa += [1,0]
                push!(seen, santa)
            end
            santa_turn = false
        else
            if char == "^"
                robo_santa += [-1,0]
                push!(seen, robo_santa)
            elseif char == ">"
                robo_santa += [0,1]
                push!(seen, robo_santa)
            elseif char == "<"
                robo_santa += [0,-1]
                push!(seen, robo_santa)
            elseif char == "v"
                robo_santa += [1,0]
                push!(seen, robo_santa)
            end
            santa_turn = true
        end
    end
    return seen
end
println(length(part_two()))
