email = input("Please input a mailaddress: ") #average.joe@test.com
email = email.split(".") #result: ["average", "joe@test", "com"]
first_name = email[0].capitalize() #Average
email = email[1].split("@") #joe@test --> ["joe", "test"]
last_name = email[0].capitalize()  #Joe
company = email[1].capitalize() #Test
print("Hello "+ first_name + " " + last_name)
print("You are working at ", company)
