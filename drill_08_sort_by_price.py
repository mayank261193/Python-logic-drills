#Sort a list of (name, price) tuples by price
Tuple=[("mango",80),("apple",85),("tomato",90)]
sort=sorted(Tuple,key=lambda x:x[1],reverse=True)
print(sort)
