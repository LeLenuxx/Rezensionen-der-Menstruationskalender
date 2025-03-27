from google_play_scraper import Sort, reviews
from nltk.tokenize import RegexpTokenizer
import numpy as np

# Create tokenizer, see docs and tokenizer.py for more info on how this works
tokenizer = RegexpTokenizer(r"\w+")

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
select_app = 0  # Which app to look at: 0 for Clue, 1 for Flo, etc.
review_count = 500  # Number of review to look at for each score (so total number of review crawled will be review_count * 5)

# Data arrays
review_list = []  # This list contains all reviews we crawled after the following loop


# Crawl reviews and store reviews depending on score, we will look at all reviews with 0 to 5 stars
for num_stars in range(1, 6):
    result, continuation_token = reviews(
        apps[select_app],  # Which app to look at
        lang="de",  # List only german results
        sort=Sort.NEWEST,  # defaults to Sort.NEWEST
        count=review_count,  # Output 3 reviews
        filter_score_with=num_stars,  # defaults to None(means all score)
    )

    content_list = []
    for resulting_review in result:
        content_list.append(resulting_review["content"])

    review_list.append(content_list)

# Looking at average number of words for each star amount
# here the num_stars is used as a list index, so 0 to 5, gives us 1 to 5 stars
num_words = 0  # number of words in a review
list_num_words = []  # number of words for each review, for each star amount
average_words = []
median_words = []
variance_words = []
std_dev_words = []

for num_stars in range(0, 5):
    list_num_words.append([])
    for review in review_list[num_stars]:
        tokens = tokenizer.tokenize(review)
        num_words = len(tokens)
        list_num_words[num_stars].append(num_words)
    average_words.append(np.average(list_num_words[num_stars]))
    median_words.append(np.median(list_num_words[num_stars]))
    variance_words.append(np.var(list_num_words[num_stars]))
    std_dev_words.append(np.std(list_num_words[num_stars]))


for k in range(1, 6):
    print(f"=== Reviews with {k} stars ===")
    print(f"Average wordcount for {k} stars: {average_words[k-1]}")
    print(f"Median wordcount for {k} stars: {median_words[k-1]}")
    print(f"Variance wordcount for {k} stars: {variance_words[k-1]}")
    print(f"Standard deviation wordcount for {k} stars: {std_dev_words[k-1]}")
    print()

