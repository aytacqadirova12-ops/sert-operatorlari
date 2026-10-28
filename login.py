correct_email = "jane@gmail.com"
correct_password = "12345"

email = input("Email daxil edin: ")
password = input("Şifrə daxil edin: ")

if email != correct_email:
    print("Hesab tapılmadı")
else:
    if password != correct_password:
        print("Şifrə yanlışdır")
    else:
        print("Xoş gəldiniz!")