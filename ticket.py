age = int(input("Yaşınızı daxil edin: "))

if age < 7:
    price = 0
    status = "ok"
else:
    if age > 65:
        price = 4
        status = "ok"
    else:
        is_student = input("Tələbəsinizmi? (bəli/xeyr): ")
        
        if is_student == "bəli":
            price = 5
            status = "ok"
        else:
            if is_student == "xeyr":
                price = 8
                status = "ok"
            else:
                status = "not ok"

if status == "not ok":
    print("Zəhmət olmasa düzgün yazın: bəli və ya xeyr")
else:
    print(f"Bilet qiyməti: {price} AZN")