lines = IO.readlines("input7.txt", chomp: true)

count = 0

lines.each do |line|
    tls = nil
    matches = []
    # Remove matches, but collect them
    processed = line.gsub(/\[\w{1,}\]/) do |match|
        matches << match
        " "  # Return empty string to remove the match
    end
    #puts matches
    #puts processed
    if /(.)(?!\1)(.)\2\1/ =~ processed
        tls = true
    end
    matches.each do |match|
        if /(.)(?!\1)(.)\2\1/ =~ match
            tls = false
        end
    end
    #puts "All matches: #{matches.inspect}"
    #puts "Text with matches removed: #{processed}"
    if tls
        count += 1
    end
end


lines[0,100].each do |line|
    puts line
    m = /(.)(?!\1)(.)\1/.match(line)
    #puts m
    puts Regexp.last_match
    matches = []
    # Remove matches, but collect them
    processed = line.gsub(/\[\w{1,}\]/) do |match|
        matches << match
        " "  # Return empty string to remove the match
    end
end
#puts count
