#!/usr/bin/env ruby
#Regex that will match 'hbttn, hbtttn, hbttttn, hbtttttn'
puts ARGV[0].scan(/^h.t{2,5}n$/).join

