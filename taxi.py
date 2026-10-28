distance = float(input("Məsafəni daxil edin (km): "))
hour = int(input("Saatı daxil edin (0-23): "))

price = 2 + (distance * 0.80)

if hour >= 23:
    price = price + (price * 0.20)
else:
    if hour <= 6:
        price = price + (price * 0.20)
    else:
        price = price

if price < 3:
    price = 3

print(f"Gediş haqqı: {price} AZN")