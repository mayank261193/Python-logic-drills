#Find the most expensive item in a price dictionary
Dictionary=[{"item":"Apple","Price":80},{"item":"Mango","Price":90},{"item":"Grapes","Price":100}]
Expensive=list(filter(lambda x:x["Price"]==max(x["Price"] for x in Dictionary),Dictionary))
print(f"Expensive:{Expensive}")
