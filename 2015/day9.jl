# Needed for 'permutations'
using Combinatorics

lines = open("./advent/input9.txt") do file
    readlines(file)
end

towns = Set()
distances = Dict()
for line in lines
    t1, _, t2, _, d = split(line)
    push!(towns, t1)
    push!(towns, t2)

    if !haskey(distances, t1)
        distances[t1] = Dict{String, Int}()
    end

    if !haskey(distances, t2)
        distances[t2] = Dict{String, Int}()
    end
    distances[t1][t2] = parse(Int, d)
    distances[t2][t1] = parse(Int, d)
end

perms = collect(permutations([towns...]))
shortest = 1000
longest = 0
for perm in perms
    d = 0
    for i in 1:7
        d += distances[perm[i]][perm[i+1]]
    end
    if d < shortest
        shortest = d
    end
    if d > longest
        longest = d
    end
end

println(shortest)
println(longest)
