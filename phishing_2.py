mail = "1995otto.normalverbraucher@gmx.de"

for letter in mail:
    try:
        letter = int(letter)
        letter = str(letter)
        mail = mail.replace(letter, "")
    except:
        pass

print(mail)
