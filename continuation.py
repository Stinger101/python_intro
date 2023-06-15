# this is a comment
"""
this is a multiline comment
it spans two lines
"""
a = 18
b = 20
print(a+b)
print( type(a) )
c = "18"
print(type(c))
d = int(c)
print(d)
print(type(d))
age = input("what is your age?")
print(age)
print(type(age))
age_int = float(age)
print(age_int+a)
str(a)
float(a)
int(age)


a = 1 # single equals sign is an assignment operator
1 + 1 # + is an addition operator
print(a == 2) # this compares whether value in a is equal to value 2
print("not equal to")
print(a != 2) # not equal to
print("less than")
print(a < 2) # less than
print(2 < a)
print("greater than")
print(a > 2)
print(2 > a)
print("less than or equal to")
q = 4
w = 4
e = 3
print(q <= w)
print(e <= w)
print(q <= e)
print("greater than or equal to")
print(q >= w)
print(q >= e)
print("and/or operator")
q = 4
w = 4
e = 3
print(q==w and q>e)
print(q==w or q>e)

print(q==w and q<e)
print(q==w or q<e)

print(q!=w and q<e)
print(q!=w or q<e)


print("if section")
age = 16
country = "Kenya"

# classes declaration, function declaration, if, for, while

if(age>=18 and country == "Kenya"):
    print("you can drive in Kenya")
elif(age >= 16 and country == "US"):
    print("you can drive in the US")
elif(age >= 16 and country == "Kenya"):
    print("Move to US, you can drive there")
else:
    print("you cannot drive")

print("Loops")
#DRY Dont repeat yourself
# print("Welcome Home")
# print("Welcome Home")
# print("Welcome Home")

counter = 0

while(counter == 0):
    print("Welcome Home")
    counter = counter+1 # to change bool exp to false
    # break

names = ["Ann","Peter","John"]
for name in names:
    print(name.lower())

for ns in names:
    print(ns.upper())

ages = [18,54,37,40]

for age in ages:
    print(age+5)
