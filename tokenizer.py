from nltk.tokenize import RegexpTokenizer
tokenizer = RegexpTokenizer(r'\w+')
text = 'Eine tolle App, intuitiv zu bedienen und mit vielen interessanten Informationen. Ich nutze die Vollversion jetzt schon seit über einem Jahr, hat mich auch super durch die Schwangerschaft begleitet. Ich habe einen Verbesserungsvorschlag: ich fände es toll, wenn man die Schwangerschaft fest im Kalender hinterlegen kann 👍🏻'
tokens = tokenizer.tokenize(text)
print(tokens)
