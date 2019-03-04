import music as mb

BASE_URL = "http://musicbrainz.org/ws/2/"
ARTIST_URL = BASE_URL + "artist/"

query_type = {  "simple": {},
                "atr": {"inc": "aliases+tags+ratings"},
                "aliases": {"inc": "aliases"},
                "releases": {"inc": "releases"}}

# Question 1: How many bands named "First Aid Kit"?
results = mb.query_by_name(ARTIST_URL, query_type["simple"], "First Aid Kit")
    # pretty_print(results)
count = 0

for artist in results["artists"]:

    if artist["name"] == "First Aid Kit":
            count += 1

print("There are {0} bands named First Aid Kit".format(count))        

    # Question 2: Begin_area name for Queen?
results = mb.query_by_name(ARTIST_URL, query_type["simple"], "Queen")

Queen = results["artists"][0]

print("The begin-area name for Queen is " + Queen["begin-area"]["name"])

    # Question 3: Spanish alias for The Beatles?
results = mb.query_by_name(ARTIST_URL, query_type["simple"], "The Beatles")

for alias in results["artists"][0]["aliases"]:
    if alias["locale"] == "es":
        print("The Spanish alias for The Beatles is " + alias["name"])

    # Question 4: Nirvana disambiguation?
results = mb.query_by_name(ARTIST_URL, query_type["simple"], "Nirvana")

print("The disambiguation for Nirvana is " + results["artists"][0]["disambiguation"])

    # Question 5: Where was One Direction formed?
results = mb.query_by_name(ARTIST_URL, query_type["simple"], "One Direction")

print("One Direction was formed in " + results["artists"][0]["life-span"]["begin"])





