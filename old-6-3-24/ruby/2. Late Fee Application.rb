#  2. Late Fee Application
# Apply a late fee if an invoice is past due.

# ruby
# Copy
# Edit
require 'date'
require 'bigdecimal'

invoice_date = Date.parse("2025-07-01")
today = Date.parse("2025-08-06")
due_days = 30
amount_due = BigDecimal("120.00")
late_fee = BigDecimal("15.00")

# TODO:
# - Check if today is past due
# - If so, add the late fee
# - Print "Total Due: $XXX.XX"

days_since_due = today - invoice_date
is_over_due =  days_since_due.to_i > due_days
total_due =  is_over_due ? amount_due.to_f + late_fee.to_f : amount_due.to_f

puts "Total Due: #{total_due}"

# Total Due: 135.0