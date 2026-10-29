mebleg = float(input("Sifarişin məbləğini daxil edin: "))

yekun_mebleg = "Məbləğ mənfi ola bilməz!" if mebleg < 0 else (mebleg * 0.8 if mebleg >= 200 else (mebleg * 0.9 if mebleg >= 100 else mebleg))

print("Yekun məbləğ:", yekun_mebleg)

status = "Endirim qazandınız" if mebleg >= 100 else "Endirim yoxdur"
print("Status:", status)