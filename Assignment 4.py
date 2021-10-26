initial_money=float(input(" Enter the amount of money you have:"))
apple_price=float(input(" Enter price of apple:"))

total_apples= int(initial_money // apple_price)
total_change=initial_money%apple_price
print(f"You can buy {total_apples} apple and your change is {total_change} pesos.")