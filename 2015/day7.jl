lines = open("./input/day7.txt") do file
    readlines(file)
end

cache = Dict()
wire = Dict()

for line in lines
    if line == ""
        continue
    end
    operands, dest = split(line, " -> ")
    wire[dest] = split(operands)
end

function calculate_signal(name)
    try
        n = parse(Int, name)
        return n
    catch ArgumentError
        nothing
    end

    if !haskey(cache, name)
        ops = wire[name]
        if length(ops) == 1
            result = calculate_signal(ops[1])
        else
            op = ops[end-1]
            if op == "AND"
                result = calculate_signal(ops[1]) & calculate_signal(ops[end])
            elseif op == "OR"
                result = calculate_signal(ops[1]) | calculate_signal(ops[end])
            elseif op == "NOT"
                result = ~calculate_signal(ops[end]) & 0xffff
            elseif op == "RSHIFT"
                result = calculate_signal(ops[1]) >> parse(Int, ops[end])
            elseif op == "LSHIFT"
                result = calculate_signal(ops[1]) << parse(Int, ops[end])
            else
                # Unknown op
                throw(UndefRefError())
            end
        end
        cache[name] = result
    end
    return cache[name]
end

a_signal = calculate_signal("a")
# Part 1
println(a_signal)
# Part 2
# Clear cache
empty!(cache)
# override b
wire["b"] = [string(a_signal)]
# run again
a_signal = calculate_signal("a")
println(a_signal)
