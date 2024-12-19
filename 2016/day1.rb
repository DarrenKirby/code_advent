directions = IO.read("input.txt")
directions.chomp!.gsub!(",", "")
d_arr = directions.split(" ")

# Part 1

head_ptr = 0
pos = [0, 0]

def heading_ptr(turn, hp)
  delta = turn == 'L' ? -1 : 1
  (hp + delta) % 4
end

d_arr.each do |op|
    head_ptr = heading_ptr(op[0], head_ptr)
    case head_ptr
      when 0
        pos[0] -= op[1..-1].to_i
      when 1
        pos[1] += op[1..-1].to_i
      when 2
        pos[0] += op[1..-1].to_i
      when 3
        pos[1] -= op[1..-1].to_i
    end
end

puts(pos[0].abs + pos[1].abs)

# Part 2

head_ptr = 0
pos = [0, 0]
$visited = []

def check_if_visited(s)
  if $visited.include?(s)
    x, y = s.split(",").map(&:to_i)
    puts x.abs + y.abs
    exit
  else
    $visited << s
  end
end

def visit_line(old_x, old_y, new_x, new_y)
    if old_x == new_x
        start_y, end_y = old_y, new_y
        if start_y < end_y
            ((start_y + 1)..end_y).each { |y| check_if_visited("#{new_x},#{y}") }
        else
            (start_y - 1).downto(end_y).each { |y| check_if_visited("#{new_x},#{y}") }
        end
    else
        start_x, end_x = old_x, new_x
        if start_x < end_x
            ((start_x + 1)..end_x).each { |x| check_if_visited("#{x},#{new_y}") }
        else
            (start_x - 1).downto(end_x).each { |x| check_if_visited("#{x},#{new_y}") }
        end
    end
end

deltas = [
  [-1, 0],
  [0, 1],
  [1, 0],
  [0, -1]
]

d_arr.each do |op|
    old_pos = pos.dup
    head_ptr = heading_ptr(op[0], head_ptr)

    steps = op[1..-1].to_i
    dx, dy = deltas[head_ptr]
    pos[0] += dx * steps
    pos[1] += dy * steps

    visit_line(old_pos[0], old_pos[1], pos[0], pos[1])
end
