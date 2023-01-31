#!/usr/bin/env ruby
# Script that output SENDER, RECEIVER and FLAGS
puts ARGV[0].scan(/from:(\+?\w+)|to:(\+?\w+)|flags:(-?\d:\d:-?\d:\d:-?\d)/).join(',')
