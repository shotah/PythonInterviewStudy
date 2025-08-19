# 1. Due Date Calculation
# Given an invoice date, add 30 days to calculate the due date.

require 'date'
require 'bigdecimal'

# Input
invoice_date = Date.parse("2025-08-01")

# TODO: Calculate due_date
due_date = invoice_date  + 30

# puts due_date.strftime("%Y-%m-%d")  # Should be "2025-08-31"
# # 2025-08-31
# puts Time.now
# puts Date.new(Time.now.year, Time.now.month, -1).day
# puts Date.new(Time.now.year, Time.now.month, 1)

# puts Date.new(Time.now.year, Time.now.month, 1) - Date.new(Time.now.year, Time.now.month, 20) 

def active_days(start_date, end_date)
  # TODO: move this out of the method to script level
  start_of_the_month = Date.new(Time.now.year, Time.now.month, 1)
  # Solution found on stack overflow
  # https://stackoverflow.com/questions/1489826/how-to-get-the-number-of-days-in-a-given-month-in-ruby-accounting-for-year
  end_of_the_month = Date.new(Time.now.year, Time.now.month, -1)
  
  # gaurd clause if user is no longer active
  if end_date != nil && end_date < start_of_the_month
     return 0
  end
  days_inactive = 0
  if start_date > start_of_the_month
    days_inactive += (start_date - start_of_the_month).abs
    puts days_inactive.to_i
  end
  if end_date != nil && end_date < end_of_the_month
    days_inactive += (end_date - end_of_the_month).abs
     puts days_inactive.to_i
  end
  return (end_of_the_month.day - days_inactive.to_i)
end

puts active_days(Date.new(Time.now.year, Time.now.month, 4), nil)

def monthly_charge(month, subscription, users)
  total = 0
  # May be nil
  # TODO: get fall back price if nil current
  place_holder_rate = BigDecimal("0")
  rate = subscription != nil && hash.key?(subscription[:monthly_price_in_cents]) ? BigDecimal(subscription[:monthly_price_in_cents]) : place_holder_rate
  #TODO: We do need to support historical calculations (previous dates) so if date is return flat rate.
  # source google search
  current_month = Date.strptime(month, "%Y-%m")
  days_in_month = BigDecimal(last_day_of_month(current_month).day)
  day_rate = rate / days_in_month
  # For each day of the month, identify which users had an active subscription on that day
  hours_total = users.reduce(0) do |sum, user|
    sum + active_days(user[:activated_on], user[:deactivated_on])
  end
  # Multiply the number of active users for the day by the daily rate to calculate the total for the day
  # Return the running total for the month at the end
  return sprintf('%.2f', BigDecimal(hours_total) * day_rate)
end

users=  [
    {
    id: 1,
    name: 'Employee #1',
    activated_on: Date.new(2019, 1, 1),
    deactivated_on: nil,
    customer_id: 1,
    },
    {
    id: 2,
    name: 'Employee #2',
    activated_on: Date.new(2019, 1, 1),
    deactivated_on: nil,
    customer_id: 1,
    },
]

subscription =     {
      id: 1,
      customer_id: 1,
      monthly_price_in_cents: 5000,
    }

puts monthly_charge('2020-12', subscription, users)