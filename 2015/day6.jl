lines = open("./input/day6.txt") do file
    readlines(file)
end

function process_line(l)
    a = []
    l = replace(l, "turn " => "", "through " => "")
    nl = split(l)
    push!(a, nl[1])
    fc = split(nl[2], ",")
    sc = split(nl[3], ",")
    # add 1 to each value for Julia 1-indexed arrays
    append!(a, [parse(Int, fc[1]) + 1, parse(Int, fc[2]) + 1])
    append!(a, [parse(Int, sc[1]) + 1, parse(Int, sc[2]) + 1])
end

# Part 1

ops = [process_line(line) for line in lines]
n = 1000

let grid = zeros(Int64, n, n)
    for op in ops
        if op[1] == "off"
            for i in op[2]:op[4]
                for j in op[3]:op[5]
                    grid[i,j] = 0
                end
            end
        elseif op[1] == "on"
            for i in op[2]:op[4]
                for j in op[3]:op[5]
                    grid[i,j] = 1
                end
            end
        elseif op[1] == "toggle"
            for i in op[2]:op[4]
                for j in op[3]:op[5]
                    if grid[i,j] == 0
                        grid[i,j] = 1
                    else
                        grid[i,j] = 0
                    end
                end
            end
        end
    end

    println(count(!iszero, grid))
end

# Part 2
ops = [process_line(line) for line in lines]
n = 1000

let grid = zeros(Int64, n, n)
    for op in ops
        if op[1] == "off"
            for i in op[2]:op[4]
                for j in op[3]:op[5]
                    if grid[i,j] == 0
                        continue
                    end
                    grid[i,j] -= 1
                end
            end
        elseif op[1] == "on"
            for i in op[2]:op[4]
                for j in op[3]:op[5]
                    grid[i,j] += 1
                end
            end
        elseif op[1] == "toggle"
            for i in op[2]:op[4]
                for j in op[3]:op[5]
                    grid[i,j] += 2
                end
            end
        end
    end

    println(sum(grid[:]))
end
