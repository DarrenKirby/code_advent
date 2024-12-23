lines = open("./advent/input8.txt") do file
    readlines(file)
end

function count_raw_string(s)
    l = length(s)
end

function count_escaped_string(s)
    s = eval(Meta.parse(s))
    l = length(s)
end

diff = 0
for line in lines
    diff += count_raw_string(line) - count_escaped_string(line)
end

println(diff)

# part 2
cnt = 0
for line in lines
    cnt += (2 + count(r"\\\\", line) + count("\"", line))
end

println(cnt)
