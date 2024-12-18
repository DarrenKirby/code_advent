# Part 1
lines = open("./advent/input5.txt") do file
    readlines(file)
end

nice = 0
for line in lines
    if occursin(r"ab|cd|pq|xy", line)
        continue
    end
    if length(collect(eachmatch(r"a|e|i|o|u", lie))) < 3
        continue
    end
    if length(collect(eachmatch(r"([a-zA-Z])\1", line))) < 1
        continue
    end
    nice +=1
end

println(nice)

# Part 2
lines = open("./advent/input5.txt") do file
    readlines(file)
end

nice = 0
for line in lines
    if length(collect(eachmatch(r"([a-zA-Z]{2}).*\1", line))) < 1
        continue
    end
    if length(collect(eachmatch(r"([a-zA-Z]).\1", line))) < 1
        continue
    end
    nice +=1
end

println(nice)
