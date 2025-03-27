from google_play_scraper import search

# With this script you can search for apps on the play store.
# Put the search terms here, and it will print the top 3 results by default

result = search(
    "Flo", # Enter a name here to search it in the google play store (works like the search bar in the app)
    lang="de",  # Look for english results
    n_hits=3  # Number of results
)

print(result)

#apps = ['com.clue.android', org.iggymedia.periodtracker, com.brc.PeriodTrackerDiary, com.wachanga.womancalendar, com.popularapp.periodcalendar]
#app_names = [Clue, Flo, Myperiodcalendar, Clover, P.C]