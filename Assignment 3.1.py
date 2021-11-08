import math

def get_aquan():
    apple= int(input("Enter apple quantity:"))
    return apple

def get_oquan():
    orange= int(input("Enter orange quantity:"))
    return orange

acharge= 20* get_aquan()
ocharge= 25* get_oquan()

def total_price():
    overall= (acharge+ocharge)
    return overall

print(f"The total amount is {total_price()} pesos.")

total_price()
