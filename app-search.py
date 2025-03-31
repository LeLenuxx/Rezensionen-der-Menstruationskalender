from google_play_scraper import search

result = search(
    "com.popularapp.periodcalendar", 
    lang="de",  #
    n_hits=1  
)

print(result)
