mobile_prices={
    "iphone":180000,
    "samsung":150000,
    "oppo":70000,
    "vivo":65000,
    "realme":60000
}
print(mobile_prices)
print(mobile_prices["samsung"])
mobile_prices["oneplus"]=120000
print(mobile_prices)

mobile_prices["oppo"]=75000
print(mobile_prices)

mobile_prices.pop("vivo")
print(mobile_prices)

for item, price in mobile_prices.items():
    print(item," :",price)
print(max(mobile_prices))

total_sum=sum(mobile_prices.values())
print(total_sum)
count=len(mobile_prices)
average=total_sum/count
print("the average of all the phone is :",average)
print("the mobiles whic price is greater then 140000")
for item, price in mobile_prices.items():
    if price>140000:
        print(item," ")

mobile = input("Enter mobile name: ").lower()

if mobile in mobile_prices:
    print("Price is", mobile_prices[mobile])
else:
    print("Mobile not found")