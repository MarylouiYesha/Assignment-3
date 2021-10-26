initial_money=float(input(" Enter the amount of money you have:"))
apple_price=float(input(" Enter price of apple:"))
while initial_money < apple_price:
   print("Invalid price")
   apple_price=float(input(" Enter price of apple:"))

apple_quantity=int(input(" How many apple/s?"))

while apple_quantity >100:
   print("Invalid quantity max quantity:100")
   apple_quantity =int(input("How many apple/s?"))

apple_price *= apple_quantity
initial_money -= apple_price

while initial_money <apple_price:
   print("Invalid quantity:")
   apple_quantity=int(input("How many apples?"))

total_change=initial_money
print(f"You can buy {apple_quantity} apple and your change is {total_change} pesos.")