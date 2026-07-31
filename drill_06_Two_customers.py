Pencil=["A","B","C"]
Eraser=["B","C","D"]
Set1=set(Pencil)
Set2=set(Eraser)
print("Both:",Set1&Set2)
print("only pencil:",Set1-Set2)
print("only eraser:",Set2-Set1)
