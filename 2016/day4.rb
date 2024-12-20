lines = IO.readlines("input4.txt", chomp: true)
# Part 1

def count_letters(s)
  Hash[
    s.delete(' ')
     .split('')
     .group_by{ |c| c }
     .map{ |k, v| [k, v.size] }
     .sort_by{ |k, v| [-v, k] }
  ]
end

sum = 0
lines.each do |line|
    l = line.split("-")
    sect_id, c_sum = l.pop.split("[")
    encrypt_n = l.join
    my_c_sum = count_letters(encrypt_n).first(5).map(&:first).join
    if my_c_sum == c_sum[0..-2]
        sum += sect_id.to_i
    end
end

puts(sum)

# Part 2

lines.each do |line|
    l = line.split("-")
    sect_id, c_sum = l.pop.split("[")
    encrypt_n = l.join("-")

    shift = sect_id.to_i % 26
    msg = encrypt_n.tr(('a'..'z').to_a.join, ('a'..'z').to_a.rotate(shift).join).gsub("-"," ")
    if msg.include? 'northpole'
        puts("#{sect_id} #{msg}")
    end
end
