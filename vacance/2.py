print("Welcome to the tip calculator.")
TP = float(input("What was the total pill?\n"))
TipP = float(input("What percentage tip would you like to give 10 , 12 or 15?\n"))
PN = float(input("How many people to split the bill?\n"))
tip = (TP*(TipP/100))
res =(tip+TP)/PN
print("Each person should pay:  %.2f "%(res))