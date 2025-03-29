from google_play_scraper import Sort, reviews
from nltk.tokenize import RegexpTokenizer

apps = [
    "com.clue.android",
    "org.iggymedia.periodtracker",
    "com.brc.PeriodTrackerDiary",
    "com.wachanga.womancalendar",
    "com.popularapp.periodcalendar",
]
apps_names = ["Clue", "Flo", "Myperiodcalendar", "Clover", "P.C"]

review_count = 50 # Anzahl der generierten Rezensionen

result, continuation_token = reviews(
    apps[1], # Welche App betrachtet wird
    lang="de",
    sort=Sort.NEWEST,  
    count=review_count,
    filter_score_with=5,  # Welches Bewertungskriterium betrachtet wird (1-5 Sterne)
)
for k in range (len(result)):
    text = result[k]['content']
    print(result[k]['content'])
    print()

