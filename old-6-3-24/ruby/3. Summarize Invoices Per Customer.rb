# 📊 3. Summarize Invoices Per Customer
# Given a list of invoices, show total amount due per customer.

# ruby
# Copy
# Edit
require 'bigdecimal'
require 'date'
invoices = [
  { customer: "Alice", total: "199.99" },
  { customer: "Bob", total: "35.00" },
  { customer: "Alice", total: "50.00" },
  { customer: "Carol", total: "75.50" },
  { customer: "Bob", total: "20.00" }
]

# TODO:
# - Group by customer
# - Sum totals
# - Print:
#   Alice owes $249.99
#   Bob owes $55.00
#   Carol owes $75.50

# grouped_items = invoices.each_with_object({}) do |item, hash|
#   total_decimal = BigDecimal(item[:total])
#   if hash.key?(item[:customer])
#     # If the item already exists, add to its quantity and total price
#     hash[item[:customer]][:total] += item[:total].to_f
#   else
#     # If it's a new item, add it to the hash
#     hash[item[:customer]] = {
#       customer: item[:customer],
#       total: total_decimal.to_f,
#     }
#   end
# end

# grouped_items.each { |i| puts "#{i[1][:customer]} owes $#{i[1][:total]}" }

grouped_totals = invoices.each_with_object(Hash.new { |h, k| h[k] = BigDecimal("0") }) do |invoice, hash|
  hash[invoice[:customer]] += BigDecimal(invoice[:total])
end

grouped_totals.each do |customer, total|
  puts "#{customer} owes $#{sprintf('%.2f', total)}"
end

puts Date.new("2022-04")

# Alice owes $249.99
# Bob owes $55.0
# Carol owes $75.5