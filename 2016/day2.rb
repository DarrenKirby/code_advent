directions = IO.readlines("input2.txt", chomp: true)

kp = [['1','2','3'],
      ['4','5','6'],
      ['7','8','9']]
i = 1
j = 1

m = {
    'R' => {:i => 0, :j => 1},
    'L' => {:i => 0, :j => -1},
    'D' => {:i => 1, :j => 0},
    'U' => {:i => -1, :j => 0}
}

code =[]
key = '5'
directions.each do |line|
    line.each_char do |c|
        if i + m[c][:i] < 0 or i + m[c][:i] > 2 or
           j + m[c][:j] < 0 or j + m[c][:j] > 2
           # no-op
        else
            i += m[c][:i]
            j += m[c][:j]
            key = kp[i][j]
        end
    end
    code << key
end

puts("Part 1")
puts("#{code}")

# Part 2
kp = [['x', 'x', '1', 'x', 'x'],
      ['x', '2', '3', '4', 'x'],
      ['5', '6', '7', '8', '9'],
      ['x', 'A', 'B', 'C', 'x'],
      ['x', 'x', 'D', 'x', 'x'],
     ]

i = 2
j = 0

code =[]
key = '5'

directions.each do |line|
    line.each_char do |c|
        new_i = i + m[c][:i]
        new_j = j + m[c][:j]
        if new_i < 0 or i + m[c][:i] > 4 or
           new_j < 0 or j + m[c][:j] > 4 or
           kp[new_i][new_j] == 'x'
           # no-op
        else
            i += m[c][:i]
            j += m[c][:j]
            key = kp[i][j]
        end
    end
    code << key
end

puts("Part 2")
puts("#{code}")
