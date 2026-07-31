List=[("A",2),("B",5),("c",8),("D",1)]
Average=sum(item[1] for item in List)/len(List)
print("Initial_List:", List)
print("Average:", Average)
print("New list:",list(filter(lambda p:p[1]>Average,List)))
