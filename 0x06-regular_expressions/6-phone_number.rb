#!/usr/bin/env ruby
# Regex that matches a 10 digit phone number
puts ARGV[0].scan(/^\d{10}$/).join
