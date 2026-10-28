grade = int(input("0-100 arası bal daxil edin: "))

if grade < 0:
    print("Yanlış bal")
else:
    if grade > 100:
        print("Yanlış bal")
    else:
        if grade >= 91:
            print("A (Əla)")
        else:
            if grade >= 81:
                print("B")
            else:
                if grade >= 71:
                    print("C")
                else:
                    if grade >= 61:
                        print("D")
                    else:
                        if grade >= 51:
                            print("E")
                        else:
                            print("F")