data = open("./advent/input.txt") do file
    read(file, String)
end
length(data)

floor = 0
pos = 0

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
