weight = float(input("Çamadanın çəkisini daxil edin (kq): "))
ticket_type = input("Bilet növünü daxil edin (econom/business): ")

if weight > 32:
    print("32 kq-dan ağır çamadan heç bir biletlə qəbul edilmir.")
else:
    if ticket_type == "econom":
        if weight <= 23:
            print("Pulsuz")
        else:
            print("30 AZN əlavə ödəniş")
    else:
        if ticket_type == "business":
            if weight <= 32:
                print("Pulsuz")
        else:
            print("Yanlış bilet növü daxil edildi.")