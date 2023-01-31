#!/usr/bin/env ruby
#Script matches a regular expression

output = ARGV[0].scan(/from:([^\]]*\b)|to:([^\]]*\b)|flags:([^\]]*\b)/).concat()
all = []
output.each do |i|
  all.concat(i)
end
all.select! {|i| i != nil}
puts all.join(",")
