character = (input("Enter a single character :"))
if character.isdigit():
    print(f"Digit")
elif character.isalpha():
    print(f"Alphabet")
elif character.isalnum():
    print("Invalid character")
else:
    print(f"Special character")
