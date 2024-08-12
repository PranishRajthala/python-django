first_num = input("enter first number")
a=int(first_num)
symbol = input("enter action you want to prefer")
second_num = input("enter second number")
b=int(second_num)
if symbol == "+":
    print(a+b)
elif symbol == "-":
    print(a-b)
elif symbol == '*':
    print(a*b)
elif symbol == '/':
    print(a/b)
