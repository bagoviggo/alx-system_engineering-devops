#!/usr/bin/env ruby
# Script that output SENDER, RECEIVER and FLAGS
puts ARGV[0].scan(/(?<=from:|to:|flags:)[^\]]*/).join