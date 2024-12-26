print("Here, \nYou will be able to alter your name in alphabetic way")

string = input("First, \nEnter your name: ")
string2 = ""

for i in string:
    string2 = i + string2

print("\n\nYour new name is: ", string2)