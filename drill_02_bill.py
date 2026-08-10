# Drill 2: splits a restaurant bill with a tip.
B=2847
N=4
Tip=(10/100)*B
Total=B+Tip
Average=Total/4
print(f"Total with tip:{Total}\nEach pays:{round(Average,2)}\nEach pays(whole rupees):{int(Average)}")



# YOUR CODE HERE
# Expected:
# Total with tip: 3131.7
# Each pays: 782.93
# Each pays (whole rupees): 782
