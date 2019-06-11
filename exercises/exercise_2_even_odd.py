num = int(input("Enter number: "))
check = int(input("Give a number to divide by: "))
if num % 4 == 0:
    print("Number {} is multiple of 4".format(str(num)))
elif num % 2 == 0:
    print("Number {} is even".format(str(num)))
else:
    print("Number {} is odd".format(str(num)))

if num % check == 0:
    print("Number {} divides evenly by {}".format(str(num), str(check)))
else:
    print("Number {} is odd".format(str(num)))

# num = int(input("give me a number to check: "))
# check = int(input("give me a number to divide by: "))
#
# if num % 4 == 0:
#     print(num, "is a multiple of 4")
# elif num % 2 == 0:
#     print(num, "is an even number")
# else:
#     print(num, "is an odd number")
#
# if num % check == 0:
#     print(num, "divides evenly by", check)
# else:
#     print(num, "does not divide evenly by", check)