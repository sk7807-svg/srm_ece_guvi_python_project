#Write a function to check given string is a palindrome or not
string = input("Enter a string : ")
reversed_string = ""
for str in string:
    reversed_string = str + reversed_string
print(reversed_string)
if (string==reversed_string):
    print("Palindrome")
else:
    print("Not a palindrome")