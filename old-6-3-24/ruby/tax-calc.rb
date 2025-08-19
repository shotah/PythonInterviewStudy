require 'bigdecimal'

# Input
prices = ["19.99", "5.25", "12.75"]

# TODO: Convert to BigDecimal, sum, calculate tax and total
# subtotal = prices.map{ |price| BigDecimal(price)}.sum
subtotal = prices.reduce(BigDecimal("0")) { |sum, price| sum + BigDecimal(price) }
tax_rate = BigDecimal("0.085")
tax = subtotal * tax_rate
total = subtotal + tax

puts "Subtotal: $#{sprintf('%.2f', subtotal)}"
puts "Tax: $#{sprintf('%.2f', tax)}"
puts "Total: $#{sprintf('%.2f', total)}"

# Subtotal: $37.99
# Tax: $3.23
# Total: $41.22