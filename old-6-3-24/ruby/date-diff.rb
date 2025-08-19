# 5. Date Difference
# Given two dates, calculate how many days passed between them.

# ruby
# Copy
# Edit
require 'date'

start_date = Date.parse("2025-07-01")
end_date   = Date.parse("2025-08-06")
date_string = "2025-08"
date_object = Date.strptime(date_string, "%Y-%m")
puts date_object

# TODO: Days between?
days_between = end_date - start_date

puts "The type of 'days_between' is: #{days_between.class}"
# => The type of 'days_between' is: Rational

# puts due_date.strftime("%Y-%m-%d")  # Should be "2025-08-31"
puts "Days: #{days_between.to_i}"  # => 36

# The type of 'days_between' is: Rational
# Days: 36