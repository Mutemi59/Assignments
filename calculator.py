def getNmumber(title):
	while True:
		try:
			num = int(input(f"Enter the {title} number: "))
			return num
		except ValueError:
			print("Invalid input (enter numbers only)\n")



print("__________CALCULATOR__________\n")

num1 = getNmumber("first")
num2 = getNmumber("second")

operators = ["+", "-", "/", "*"]
operator = ""
while not operators.__contains__(operator):
	operator = input("Enter an operatiion +-/*; ")

result = 0
match operator:
	case "+":
		result = num1 + num2
	case "-":
		result = num1 - num2
	case "/":
		if num2 == 0:
			raise("Cannot divide by 0")
		else: result = num1 / num2
	case "*":
		result =num1 * num2
	case _:
		print("Invalid operator, try again!!")

print(f"{num1} {operator} {num2} = {result}")





