import random
uppercase_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lowercase_letter = uppercase_letters.lower()
digits = "0123456789"
symbols = "()[]{},;:.-_/\\?+*# "

upper, lower, nums, syms = True,True,True,True
all = ""

if upper:
    all = all +  uppercase_letters
elif lower:
    all = all + lowercase_letter
elif nums:
    all = digits
if syms:
    all = all + symbols

length = 20
amount = 1

for x in range(amount):
    password = "".join(random.sample(all,length))
    print(password)