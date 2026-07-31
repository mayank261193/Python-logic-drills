products = [
    ("A", 55),
    ("B", 50),
    ("C", 12),
]
S= sorted(products, key=lambda x: x[1])
print("Products sorted by price:",S)
