products = [
    ("A", 55),
    ("B", 50),
    ("C", 12),
]
S= max(products,key=lambda x: x[1])
print("Expensive product:",S)
