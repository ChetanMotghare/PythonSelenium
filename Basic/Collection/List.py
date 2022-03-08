#List --> order

fruits = ["Apple","cherry","Banana","kiwi","mango"]

print(fruits)
print(fruits[2])
print(fruits[1:2])

for i in range(1,10):
      fruits.insert(i,input("Enter fruit name :: "))
print(fruits)