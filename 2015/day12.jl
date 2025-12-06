data = open("./input/day12.txt") do file
    read(file, String)
end

let sum = 0
    for m in eachmatch(r"-?\d+", data)
        sum += parse(Int, m.match)
    end
    println(sum)
end

