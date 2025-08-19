# 4. Discount Application
# Apply a 10% discount if subtotal exceeds $50

# ruby
# Copy
# Edit

require 'bigdecimal'


subtotal = BigDecimal("58.50")
discount = BigDecimal("0.10")
discount_price_bar = BigDecimal("50")

# TODO: Apply discount conditionally
# discounted_total = subtotal > discount_price_bar ? subtotal * (1 - discount) : subtotal

if subtotal > discount_price_bar
  discounted_total = subtotal - subtotal * discount
else
  discounted_total = subtotal
end

puts "Discounted Total: $#{sprintf('%.2f', discounted_total)}"

# Discounted Total: $52.65