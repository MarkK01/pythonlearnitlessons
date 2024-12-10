# Startup Financial Calculator

# Description
# You're an aspiring entrepreneur with a brilliant idea for a 
# new software-as-a-service (SaaS) startup.  Before pitching to investors,
# you need to create a financial model to project your costs, revenue,
# and break-even point.  Your task is to complete a Python script
# that calculates thees crucial financial metrics.

# 1. Caculate Total Starup Cost: Sum up the invidual startup costs
# (development, marketing, and equipment) to get the total inital
# investmetnt needed.

# 2. Project Monthly Revenue: Caluculate the expected monthly revenue 
# base on the number users in each subscription tier and their respective
# prices.

# 3. Calculate Monthly Operating Costs: Sum up all the monthly 
# recurring costs to determine your total monthly operating expeneses.

# 4. Determine Monthly Profit: Substract the monthly operating costs
# from the monthly revenue to find out how much profit (or loss)
# you're making each month.

# 5. Estimate Time to Break Even: Calculate how many months it will take
#  to recover your inintial investment based on your monthly profit.

# 6. Implement Sensistivity Analysis:  Create code that adjusts the number of
# users in each tier and recalculate all finacial metrics.  This will help 
# you understand how changes in user acquisition affect your projects.

# 7. Format and Display Results: Use f-string to format the results nicely 
# displaying currency value with commas and two decimal places, and rounding
# the break-even time to one decimal place.

# Startup Costs
dev_cost = 50000
marketing_cost = 20000
equipment_cost = 10000

# Subscription tiers
basic_tier_price = 9.99
pro_tier_price = 19.99
basic_tier_users = 1000
pro_tier_users = 500

# Monthly operating costs
server_cost = 1000
support_cost = 5000
misc_cost = 2000

# TODO: Calculate total startup costs
total_startup_costs = dev_cost + marketing_cost + equipment_cost

# TODO: Calculate monthly revenue
monthly_revenue = (basic_tier_price * basic_tier_users) + (pro_tier_price * pro_tier_users)

# TODO: Calculate monthly operating cost
monthly_operating_costs = server_cost + support_cost + misc_cost

# TODO: Calculate monthly profit
monthly_profit = monthly_revenue - monthly_operating_costs

# TODO: Caculate months to break even
months_to_break_even = total_startup_costs / monthly_profit

# TODO: Display results using formatted strings
print("Financial Projects:")
# User f-strings to display the results here
print(f"Total Startup Costs: ${total_startup_costs:,.2f}")
print(f"Monthly Revunue: ${monthly_revenue:,.2f}")
print(f"Monthly Operating Costs: ${monthly_operating_costs:,.2f}")
print(f"Monthly Profit: ${monthly_profit:,.2f}")
print(f"Months To Break Even: {months_to_break_even:,.1f}")


# Sensitivity analysis
print("\nSensitivity Analysis:")
# TODO: Adjust user numbers
basic_tier_users += 500
pro_tier_users += 200

# TODO: Reclculate metrics with new users numbers
new_monthly_revenue = (basic_tier_price * basic_tier_users) + (pro_tier_price * pro_tier_users)
new_monthly_profit = new_monthly_revenue - monthly_operating_costs
new_months_to_break_even = total_startup_costs / new_monthly_profit

# TODO: Display updated results
print("Updated Financial Projects:")
# User f-strings to display the updated results here
print(f"New Monthly Revenue: ${new_monthly_revenue:,.2f}")
print(f"New Monthly Profit: ${new_monthly_profit:,.2f}")
print(f"New Months To Break Even: {new_months_to_break_even:,.1f}")

# Calculate and Display The Impact of Changes
revenue_increase = new_monthly_revenue - monthly_revenue
profit_increase = new_monthly_profit - monthly_profit
break_even_improvement = months_to_break_even - new_months_to_break_even

print("\nImpact of User Increase")
print(f"Revenue Increase: ${revenue_increase:,.2f}")
print(f"Profit Increase: ${profit_increase:,.2f}")
print(f"Break-Even Time Reduction: {break_even_improvement:,.1f} months")