
def square(x):
	return x * x

def main(): 

	#Simple print
	print("Hello World!")

	#Input then print
	# name = input()
	# print(f"Hello, {name}!")

	#Variable types

	print("Printing diffferent variable !!")
	i = 28
	print(f"i is {i}!")

	f = 2.8
	print(f"f is {f}!")

	b = True
	print(f"b is {b}!")

	n = None
	print(f"n is {n}!")


	#If statement

	x = -58

	if x > 0:
		print("x is +ive")
	elif x < 0:
		print("x is -ive")
	else:
		print("x is zero")


	#Sequence

	name = "Alice"

	coordinayes = (10.0, 20.0)  # Also calles as pytohn tuple

	names = ["John", "Ali", "Khawaja", "Bob"] #python List

	print(f"{names[0]} + {names[1]}")

	#Loop

	for name in names:
		print(name)

	#Dicitonaries

	ages = {"Alice": 22, "bob": 27 }

	ages["Charlie"] = 30
	ages["Alice"] += 1

	print(ages)

	#Functions


	for i in range(10):
		print("{} squared is {}".format(i, square(i))) # formating for old python verions 


if __name__ == "__main__":
	main()