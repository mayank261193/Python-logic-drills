#Remove duplicates from a list of names, and report how many were removed
Names=["Mayank","Asha","Rahul","Mayank"]
Initial_Length=len(Names)
Duplicates=set(Names)
Final_length=len(Duplicates)
print(f"Names:{Names}\nInitial Length:{Initial_Length}\nFinal length:{Final_length}\nNames_01:{Duplicates}\n")
#Using curly braces to remove duplicates
print("----------------------------------------------")
Remove={m for m in Names}
print(f"Names_02:{Remove}")

