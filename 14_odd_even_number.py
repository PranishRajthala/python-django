# odd number
# even nuber = any number % 2 ==0

number = input("enter our number")
num = int(number)

remainder = num %2
if remainder == 0:
    print("even number")
elif remainder !=0:
    print("odd number")