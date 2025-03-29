from google_play_scraper import Sort, reviews
from nltk.tokenize import RegexpTokenizer
import numpy as np

tokenizer = RegexpTokenizer(r"\w+")

apps = [
    "com.popularapp.periodcalendar",
    "com.brc.PeriodTrackerDiary",
    "org.iggymedia.periodtracker",
    "com.wachanga.womancalendar",
    "com.clue.android",
]
apps_names = ["Perioden Kalender", "Mein Menstruations-Kalender", "Flo Zyklus-& Perioden-Kalender", "Perioden Kalender - Clover", "Clue Perioden Kalender", ]


select_app = 4  # Welche App betrachtet wird
review_count = 500  # Gesamtzahl der betrachteten Rezensionen für Ergebnis der duschnittlichen Wortanzahl
review_list = [] 

for num_stars in range(1, 6):
    result, continuation_token = reviews(
        apps[select_app], 
        country="de",
        lang="de",  
        sort=Sort.NEWEST, 
        count=review_count,
        filter_score_with=num_stars, 
    )

    content_list = []
    for resulting_review in result:
        content_list.append(resulting_review["content"])

    review_list.append(content_list)


num_words = 0  
list_num_words = [] 
average_words = [] # Durchschnittliche Wortanzahl

for num_stars in range(0, 5):
    list_num_words.append([])
    for review in review_list[num_stars]:
        if review != None:
            tokens = tokenizer.tokenize(review)
            num_words = len(tokens)
        else:
            num_stars = 0
        list_num_words[num_stars].append(num_words)
    average_words.append(np.average(list_num_words[num_stars]))


for k in range(1, 6):
    print(f"=== Reviews with {k} stars ===")
    print(f"Average wordcount for {k} stars: {average_words[k-1]}")


