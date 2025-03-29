# Methodisches Vorgehen

## For you to look at
* What kind of analysis can you do with NLTK: https://www.nltk.org/
* Think about keyword search/keyword analysis
. Do word frequency analysis
. Look at random sample of comments with frequently used words

## Skripte
Angefügt ist die Verwendung für die einzelnen Skripte

### Skript: app-search.py
Das Skript wird dafür verwendet, die Apps im Betriebssystem Play Store zu finden. Es kann mit der Suchleiste dort verglichen werden, wobei hier die App-ID als Ergebnis generiert wird, die gebraucht wird, um die Rezensione zu betrachten. 

### Skript: reviews.py
Das Skript generiert die 50 neusten Rezensionen pro App, die für Tabelle 4 in ihrer Anzahl auf mindestens die durchschnittliche Wortanzahl reduziert wurden.

### tokenizer.py
Bei der Tokenisation wird ein String zu individuellen Worten umgewandelt, damit die Wortanzahl im average-wordcount.py Skript generiert werden kann.

### Skript: average-wordcount.py
Das Skript generiert bei Eingabe der repräsentiven Nummer der App (0-4) in Zeile 17 die durchschnittliche Wortanzahl der Rezensionen pro Stern für Tabelle 3. 

#### review_list usage of list
review_list has all reviews crawled, it is a list of lists:

```
review_list[0] #lists all reviews with score of 1 (you cannot give an app 0 stars))
...
review_list[4] #lists all reviews with score of 5
```

```
review_list[0][0] # access first review with a score of 1
...
review_list[1][4] # access 5th review with a score of 2
```

