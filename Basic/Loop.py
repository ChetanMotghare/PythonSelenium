#range(): to get value between the range

print(list(range(0,11)))

#odd numbers
print(list(range(-11,10,2)))

#while loop

i=1

while i<=10:
    print(i)
    i=i+1

#for loop

for i in range(1,11):
    print("For loop", i)

for i in range(6,61,6):
    print(i)

# slicing
name = "Chetan"
print("Slicing operation :: ",name[1:3])

#string operation

print(max(name))
print(min(name))
print(len(name))

# "in" and "not

print("C" in name)
print("Ch" not in name)