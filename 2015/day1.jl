data = open("./input/day1.txt") do file
    read(file, String)
end
length(data)

let floor = 0
    let pos  = 0

        for char in split(data, "")
            pos += 1
            if char == "("
                floor += 1
            elseif char == ")"
                floor -= 1
            end
            if floor == -1
                println(pos)
                break
            end
        end

        println(floor)
    end
end

