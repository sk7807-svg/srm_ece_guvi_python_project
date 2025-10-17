#Calculate total electricity bill based on units consumed

units = int(input("Enter total units of electricity used :"))

if(units <= 100):
    amount1 = units * 5
    print(f" Total bill = ₹{amount1}")
elif(units >= 101 and units <= 200):
    amount2 = units * 7
    print(f"Total bill = ₹{amount2}")
else:
    amount3 = units *10
    print(f"Total bill = ₹{amount3}")


 