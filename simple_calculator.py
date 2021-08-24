
num_1 = float(input("\nEnter first number: "))

opr = input("\nEnter math operator: ")

num_2 = float(input("\nEnter second number: "))

result = None


if num_1.is_integer(): 
    num_1 = int(num_1)

if num_2.is_integer(): 
    num_2 = int(num_2)


if opr == "+":
    result = num_1 + num_2
    print(f"\n{num_1} + {num_2} = {result}")
elif opr == "-":
    result = num_1 - num_2
    print(f"\n{num_1} - {num_2} = {result}")
elif opr == "/":
    result = num_1 / num_2
    print(f"\n{num_1} / {num_2} = {result}")
elif opr == "*":
    result = num_1 * num_2
    print(f"\n{num_1} * {num_2} = {result}") 
else:
    print("\nInvalid math operator")
