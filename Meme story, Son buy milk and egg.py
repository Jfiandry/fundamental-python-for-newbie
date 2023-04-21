"""
First code trial using if
"""
print("mom giving instruction to son to buy a bottle of milk")
print("Son answer, Ok")
print("Son go to the shop")

milk_available = input("is the milk available? (yes/no)")

if milk_available == "yes":
    print("Son is checking the price, enough")
    egg_available = input("is the egg available? (yes/no)")
    if egg_available == "yes":
        print("Son is checking the egg stock qty in the shop, enough stock")
        print("son buy one bottle of milk and 6 egg")
    else:
        print("son buy one bottle of milk")
else:
    print("Son cancel buying the milk")

print("son go home")
print("son give the result to mom")
print("finish")
