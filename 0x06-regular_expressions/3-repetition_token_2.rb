#!/usr/bin/env ruby
# regular expression that will match these cases: 'htn, hbtn, hbttn, hbtttn'
puts ARGV[0].scan(/hbt{1,}n/).join