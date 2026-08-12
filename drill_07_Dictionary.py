#Build a dictionary of word lengths from a sentence
Sentence= "Mayank is a good boy"
List=Sentence.split()
Dictionary=[{"Name":s, "Length":len(s)} for s in List]
print(f"Dictionary:{Dictionary}")
