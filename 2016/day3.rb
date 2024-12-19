tri = IO.readlines("input3.txt", chomp: true)

# Part 1
a = []
tri.each do |t|
    ma = []
    t.split.each { |c| ma << c.to_i }
    a << ma
end

good = 0
a.each do |side|
    s = side.max
    n1, n2 = side.min(2)
    if n1 + n2 > s
        good +=1
    end
end

puts(good)

# part 2

a = []
while tri != []
    z = tri.pop
    y = tri.pop
    x = tri.pop
    za = []; ya = []; xa = []
    z.split.each { |c| za << c.to_i }
    y.split.each { |c| ya << c.to_i }
    x.split.each { |c| xa << c.to_i }
    (0..2).each do |idx|
        a << [za[idx], ya[idx], xa[idx]]
    end
end

good = 0
a.each do |side|
    s = side.max
    n1, n2 = side.min(2)
    if n1 + n2 > s
        good +=1
    end
end

puts(good)
