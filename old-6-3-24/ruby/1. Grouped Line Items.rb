# 🧩 1. Grouped Line Items
# Given multiple purchases of the same item, group and total them.

require 'bigdecimal'

line_items = [
  { name: "Widget", qty: 1, price: "19.99" },
  { name: "Gadget", qty: 2, price: "9.99" },
  { name: "Widget", qty: 3, price: "19.99" }
]

# Use each_with_object to build a new hash
# A BigDecimal is used for the price to ensure accuracy
grouped_items = line_items.each_with_object({}) do |item, hash|
  price_decimal = BigDecimal(item[:price])
  if hash.key?(item[:name])
    # If the item already exists, add to its quantity and total price
    hash[item[:name]][:qty] += item[:qty]
    hash[item[:name]][:total_price] += item[:qty] * price_decimal
  else
    # If it's a new item, add it to the hash
    hash[item[:name]] = {
      name: item[:name],
      qty: item[:qty],
      price: price_decimal,
      total_price: item[:qty] * price_decimal
    }
  end
end

# Iterate through the new hash and print the formatted output
grouped_items.values.each do |item|
  puts "#{item[:qty]}x #{item[:name]} @ $#{'%.2f' % item[:price]} = $#{'%.2f' % item[:total_price]}"
end

# 4x Widget @ $19.99 = $79.96
# 2x Gadget @ $9.99 = $19.98