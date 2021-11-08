import math

def quan():
    apple= int(input("Enter apple quantity:"))
    orange= int(input("Enter orange quantity:"))
    return apple, orange

apple, orange =quan()

def price_fruits():
    applep=20
    orangep=25
    return applep,orangep

applep,orangep= price_fruits()

def total_aprices(apple,applep):
    return apple*applep

def total_oprices(orange,orangep):
    return orange*orangep

def grand_total(total_aprices,total_oprices):
    return total_aprices+total_oprices

    
print(f"The total amount is {grand_total(total_aprices, total_oprices)} pesos.")

