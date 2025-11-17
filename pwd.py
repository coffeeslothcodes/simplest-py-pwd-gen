import random
pwd = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*()-_][}{:,.?;'\|/"
len_pwd = int(input("Enter the length of the Password: "))
x = "".join(random.sample(pwd, len_pwd))
print("Your newly generated password is", x)