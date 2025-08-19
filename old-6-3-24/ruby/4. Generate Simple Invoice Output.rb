# 🧾 4. Generate Simple Invoice Output
# Given line items, tax rate, and optional discount, print a full invoice summary.

# ruby
# Copy
# Edit
require 'bigdecimal'

line_items = [
  { name: "Sticker", qty: 5, price: "1.99" },
  { name: "Shirt", qty: 2, price: "15.00" },
]
tax_rate = BigDecimal("0.085")
discount = BigDecimal("5.00") # flat discount

# TODO:
# - Calculate subtotal
# - Apply tax
# - Subtract discount
# - Print:
#   Subtotal: $XX.XX
#   Tax: $XX.XX
#   Discount: -$5.00
#   Total: $XX.XX


# Calculate all values using BigDecimal for precision
subtotal = line_items.reduce(BigDecimal("0")) { |sum, i| sum + (BigDecimal(i[:price]) * i[:qty]) }
tax = subtotal * tax_rate
total = subtotal + tax - discount

# Format and print the output using sprintf
puts "Subtotal: $#{sprintf('%.2f', subtotal)}"
puts "Tax:      $#{sprintf('%.2f', tax)}"
puts "Discount: -$#{sprintf('%.2f', discount)}"
puts "Total:    $#{sprintf('%.2f', total)}"

# Subtotal: $39.95
# Tax:      $3.40
# Discount: -$5.00
# Total:    $38.35