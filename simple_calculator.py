
num_1 = float(input("\nEnter first number: "))

opr = input("\nEnter math operator: ")

num_2 = float(input("\nEnter second number: "))

float_output = None

if opr == "+":
    float_output = num_1 + num_2
elif opr == "-":
    float_output = num_1 - num_2
elif opr == "/":
    float_output = num_1 / num_2
elif opr == "*":
    float_output = num_1 * num_2
else:
    print("\nInvalid math operator, exiting program")


if float_output:
    
    int_output = int(float_output)

    if int_output == float_output:
        result = int_output
    else:
        result = float_output

    print(f"\n{result}")
