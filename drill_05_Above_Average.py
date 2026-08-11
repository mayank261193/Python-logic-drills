#Find the students who scored above the class average
Data=[{"name":"Mayank","marks":100},{"name":"Rahul","marks":80},{"name":"Asha","marks":90}]
Average=sum(s["marks"]for s in Data)/len(Data)
filter=list(filter(lambda x:x["marks"]>Average,Data))
print(filter)


