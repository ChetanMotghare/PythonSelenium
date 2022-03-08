#nested if else

num= int(input("Enter the number::  "))

if num>=0:
    if num ==0:
        print("Zero:: {}".format(num))
    else:
        print("Positve number:: {}".format(num))
else:
    print("Negative number:: {}".format(num))

