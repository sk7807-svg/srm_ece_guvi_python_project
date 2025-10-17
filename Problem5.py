#Check if the given number is prime or not 
num = int(input("Enter a number : "))
if  num <=1:
    print("Not prime")
else:
    for f in range(2,num):
        if num %f == 0:
            print("Not prime")
            break
    else:
            print("Prime")
