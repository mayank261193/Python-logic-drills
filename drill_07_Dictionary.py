#Build a dictionary of word lengths from a sentence
Sentence= "Mayank is a good boy"
List=Sentence.split()
Dictionary={s:len(s) for s in List}
print(Dictionary)
