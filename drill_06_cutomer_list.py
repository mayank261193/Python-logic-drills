#Given two lists of customers, report who bought both and who bought only one
A=["mayank","Rahul","Asha"]
B=["Rahul","Oswal","Asha"]
both=list(filter(lambda x:x in A,B))
print(f"Both:{both}")
onlyone=list(filter(lambda x:x ,set(A)^set(B)))
print(f"Only_one:{onlyone}")

