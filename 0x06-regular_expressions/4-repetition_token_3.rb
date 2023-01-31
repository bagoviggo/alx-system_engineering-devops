#!/usr/bin/env ruby
# regular expression that will match these cases: 'htn, hbon, hbtn, hbttn, hbtttn'
puts ARGV[0].scan(/h.?t+n/).join
