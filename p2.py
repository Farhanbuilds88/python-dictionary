#Assignment
restaurant_menu={
    "burger":250,
    "pizza":800,
    "fries":150,
    "sandwich":200
}

print(restaurant_menu)
print(restaurant_menu["pizza"])

restaurant_menu["pasta"]=500
print(restaurant_menu)

restaurant_menu["burger"]=300
print(restaurant_menu)

restaurant_menu.pop("fries")
print(restaurant_menu)

print(restaurant_menu.keys())
print(restaurant_menu.values())
print(restaurant_menu.items())

if "burger" in restaurant_menu:
    print("it is available")
if "fries" in restaurant_menu:
    print("also available")

print(len(restaurant_menu))

for item, price in restaurant_menu.items():
    print(item,":",price)