# Drill 3: builds initials and a username from a messy full name.

full_name = "  asha   verma  "
birth_year = 1999

# YOUR CODE HERE
Clean=full_name.strip().title().split()
initials=Clean[0][0]+"."+Clean[1][0]+"."
username=Clean[0].lower()+str(birth_year)[2:4]
print(f"Initials: {initials}\nUsername: {username}")
# Expected:
# Initials: A.V.
# Username: asha99
