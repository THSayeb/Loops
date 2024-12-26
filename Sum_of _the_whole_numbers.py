print("Here, \nYou will be able to calculate the addition of whole number")
n = int(input("First, \nInput the range of your number "))
sum = 0

for i in range(1, n+1):
    sum = sum + i 
    print("Total = ", sum)
    