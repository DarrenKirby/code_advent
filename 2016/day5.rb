require 'digest'

input = "reyedfim"


# Part 1

passwd = ""
(0..).each do |n|
    s = "#{input}#{n}"
    md5 = Digest::MD5.hexdigest(s)
    if md5[0..4] == "00000"
        passwd += md5[5]
        puts("found one: #{md5}")
    end
    if passwd.size == 8
        puts(passwd)
        break
    end
end

# Part 2

passwd = ['_', '_', '_', '_', '_', '_', '_', '_']
(0..).each do |n|
    s = "#{input}#{n}"
    md5 = Digest::MD5.hexdigest(s)
    if md5[0..4] == "00000"
        pos = md5[5]
        digit = md5[6]
        if pos in '0'..'7'
            if passwd[pos.to_i] == '_'
                passwd[pos.to_i] = digit
                puts("found one: #{md5}")
            else
                next
            end
        end
    end
    unless passwd.include?('_')
        puts(passwd.join)
        exit
    end
end
