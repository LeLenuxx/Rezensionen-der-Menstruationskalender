from google_play_scraper import Sort, reviews
from nltk.tokenize import RegexpTokenizer

# apps is a list of the programmatic names of the apps (like a unique name for the playstore back end), while apps_names has the plain text names
apps = [
    "com.clue.android",
    "org.iggymedia.periodtracker",
    "com.brc.PeriodTrackerDiary",
    "com.wachanga.womancalendar",
    "com.popularapp.periodcalendar",
]
apps_names = ["Clue", "Flo", "Myperiodcalendar", "Clover", "P.C"]

# Parameters for script
review_count = 50 # Number of reviews to display

result, continuation_token = reviews(
    apps[1], # Which app to look at
    lang="de",  # List only german results
    sort=Sort.NEWEST,  # defaults to Sort.NEWEST
    count=review_count,  # Output 3 reviews
    filter_score_with=5,  # defaults to None(means all score)
)
for k in range (len(result)):
    text = result[k]['content']
    print(result[k]['content'])
    print()

