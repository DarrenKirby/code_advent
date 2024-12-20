lines = IO.readlines("input6.txt", chomp: true)

def count_letters(s, asc=false)
  Hash[
    s.delete(' ')
     .split('')
     .group_by{ |c| c }
     .map{ |k, v| [k, v.size] }
     .sort_by{ |k, v| [ asc ? v : -v , k] }
  ]
end

strings = ["","","","","","","",""]

lines.each do |line|
    (0..7).each do |idx|
        strings[idx] += line[idx]
    end
end

msg = ""
strings.each do |str|
    msg << count_letters(str).first(1).map(&:first).join
end

puts(msg)

msg = ""
strings.each do |str|
    msg << count_letters(str, asc=true).first(1).map(&:first).join
end

puts(msg)
