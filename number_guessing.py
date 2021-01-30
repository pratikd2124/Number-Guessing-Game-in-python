import random
import math
lower_bound = int(input("Enter lower bound : "))
upper_bound = int(input("Enter upper bound : "))
n = math.log(upper_bound-lower_bound+1,2)
x = random.randint(lower_bound,upper_bound)
print("\n No. of guess left => ", round(n)) 
count = 0

while count < n:
    count +=1

    guess = int(input("Enter your prediction :"))

    if x == guess:
        print("Match found in just ",count," try")
        break
    elif x < guess:
        print("Go for lower")
    elif x > guess:
        print("Go for higher")

if count >= n:
    print("You ran out of your chances.Try again")