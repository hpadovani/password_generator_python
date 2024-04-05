import random

lower = "abcdefghijklmnopqrstuvwyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWYZ"
numbers = "1234567890"
symbols = "[]{}\=+-_()*&ˆ%$#@!></"

all = lower+upper+numbers+symbols

length = 13

password = "".join(random.sample(all, length))
print("==="*20)
print("Your new password is {}".format(password))
print("==="*20)