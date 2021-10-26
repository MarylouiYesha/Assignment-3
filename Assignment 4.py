initial_money=int(input(" enter the amount of money you have:"))
apple_price=int(input(" enter price of apple:"))
apple_quantity=int(input(" how many apple/s?"))
if apple_quantity not in range (1,1000):
    print("invalid quantity, max quantity:1000")
apple_price *= apple_quantity
initial_money -= apple_price
total_change = initial_money
print(f"You can buy {apple_quantity} apple and your change is {total_change} pesos.")