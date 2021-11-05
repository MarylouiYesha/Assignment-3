def howMany(money, cost):
  return money // cost
def getChange(money, cost):
  return money % cost

cash = float(input("Enter the amount of money you have:"))
price = float(input("Enter the price of apples:"))

print(f"You can buy {howMany(cash,price)} apple and your change is {getChange(cash,price):.2f} pesos.")