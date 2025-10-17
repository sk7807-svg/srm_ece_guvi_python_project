#Find factorial of a number using a loop
num = int(input("Enter a number : "))
factorial = 1
for f in range(1,num+1):
    factorial = factorial*f
    print(f"The factorial of {num} is{factorial} ")
