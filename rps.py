o1 = input("1-ci oyunçu (daş, qayçı, kağız): ")
o2 = input("2-ci oyunçu (daş, qayçı, kağız): ")

if o1 != "daş" and o1 != "qayçı" and o1 != "kağız":
    print("Belə seçim yoxdur")
else:
    if o2 != "daş" and o2 != "qayçı" and o2 != "kağız":
        print("Belə seçim yoxdur")
    else:
        if o1 == o2:
            print("Heç-heçə")
        else:
            if o1 == "daş" and o2 == "qayçı":
                print("1-ci oyunçu qalib gəldi!")
            else:
                if o1 == "qayçı" and o2 == "kağız":
                    print("1-ci oyunçu qalib gəldi!")
                else:
                    if o1 == "kağız" and o2 == "daş":
                        print("1-ci oyunçu qalib gəldi!")
                    else:
                        print("2-ci oyunçu qalib gəldi!")