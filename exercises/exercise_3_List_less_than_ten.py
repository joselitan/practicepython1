a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
for x in a:
    if x > 5:
        print(x)

b=[]
for x in a:
    if x > 5:
        b.append(x)
print(b)

print([x for x in a if x > 5])


d = int(input("enter a number: "))
print([x for x in a if x < d])
