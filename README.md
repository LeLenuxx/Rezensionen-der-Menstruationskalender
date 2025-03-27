# Methodology notes

## For you to look at
* What kind of analysis can you do with NLTK: https://www.nltk.org/
* Think about keyword search/keyword analysis
. Do word frequency analysis
. Look at random sample of comments with frequently used words

## Scripts
Below you will find the use of each scripts

### Script: app-search.py
Run this one to find the apps in the store, it works like the search bar except using it you can find the app-id that you need to look up reviews.
the app-id is some sort of unique identifier, and you cannot guess it (as you can see if you compare the name of the apps to the app-ids in the reviews.py script)

### Script: reviews.py
This one returns 'review_count' reviews (you can set that number) for the app you want (just change the number in the apps list at line 17).
By default it returns 1 review, it picks the newest review.
This script is useful because you can look at how the review dict is organized.

### tokenizer.py
This sketch shows the snippet to separate a string into individual words using nltk.
The example text is a random review.

### Script: average-wordcount.py
This one actually implements the actual analysis.

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

