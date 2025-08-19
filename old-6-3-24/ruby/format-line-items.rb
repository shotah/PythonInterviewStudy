# 3. Format Line Items
# Print invoice line items in this format:
# "1x Widget @ $19.99 = $19.99"

# ruby
# Copy
# Edit
# puts "Hello, my name is #{name} and I am #{age} years old."
# puts "The sum of 5 and 3 is #{5 + 3}."

items = [
  { name: "Widget", qty: 1, price: "19.99" },
  { name: "Gadget", qty: 2, price: "9.99" },
]

# TODO: Print each line in correct format using string interpolation
items.each do |item|
    # cast to float! 
    # or use BigDecimal. 
  puts "#{item[:qty]}x Widget @ $#{item[:price]} = $#{item[:qty] * item[:price].to_f }"
end

# 1x Widget @ $19.99 = $19.99
# 2x Widget @ $9.99 = $19.98