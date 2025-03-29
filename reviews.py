from google_play_scraper import Sort, reviews
from nltk.tokenize import RegexpTokenizer

tokenizer = RegexpTokenizer(r"\w+")

apps = [
    "com.popularapp.periodcalendar",
    "com.brc.PeriodTrackerDiary",
    "org.iggymedia.periodtracker",
    "com.wachanga.womancalendar",
    "com.clue.android",
]
apps_names = ["Perioden Kalender", "Mein Menstruations-Kalender", "Flo Zyklus-& Perioden-Kalender", "Perioden Kalender - Clover", "Clue Perioden Kalender", ]

review_count = 50 # Anzahl der generierten Rezensionen
score_filter = 3 # Welches Bewertungskriterium betrachtet wird (1-5 Sterne)
filter_length = 40 # Durchschnittliche Wortanzahl pro Bewertung und App

result, continuation_token = reviews(
    apps[2], # Welche App betrachtet wird
    country="de",
    lang="de",
    sort=Sort.NEWEST,  
    count=review_count,
    filter_score_with=score_filter,  
)

reviews_filtered = []
for k in range (len(result)):
    text = result[k]['content']
    tokens = tokenizer.tokenize(text)
    num_words = len(tokens)
    if (num_words >= filter_length):
        reviews_filtered.append(text)

for k in range(len(reviews_filtered)):
    print(reviews_filtered[k])
    print()



print(f"Number of reviews fetched total: {len(result)}")
print(f"Number of reviews above {filter_length} words: {len(reviews_filtered)}")
