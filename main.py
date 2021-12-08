rating = input("Do you want to rate netflix? ")
should_continue = True
while should_continue:
    if rating.lower() == "yes":
        print("Welcome to the netflix rater! ")
        break
else:
    should_continue = False
num = 0
import sys
try:
    num = int(input("By how many stars do you want rate Netflix out of 5? "))
except:
    print("[Error] - Invalid input")
    sys.exit
if num <=5:
    for i in range(1, num +1):
        print("*")
else:
    print("Sorry, only a maximum of 5 stars are allowed. ")

