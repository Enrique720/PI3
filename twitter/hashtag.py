
import tweepy
import csv
import pandas as pd
import wget
####input your credentials here
consumer_key = "eYyvdAokGZI089xU1MIwQtzON"
consumer_secret = "9R9n5vB76Q1x57fpFuiLlgSFAKizN6NoY5NZDAW5O8acNPMGvN"
access_token = "1259734035422724096-XuxXZiC6GAiIWiWItm5mGSDSr5FbTG"
access_token_secret = "XKoXbah03fpBdJGMyimX3QRF8jPTnmn8GBnFSMt0SdtMz"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth,wait_on_rate_limit=True)

# Open/Create a file to append data
csvFile = open('ua.csv', 'a')
#Use csv Writer
csvWriter = csv.writer(csvFile)
media_files = set()
for tweet in tweepy.Cursor(api.search,q="#cusco",count=100,
                           lang="en",
                           since="2017-04-03").items():
    
    media = tweet.entities.get('media', [])
    if(len(media) > 0):
        media_files.add(media[0]['media_url'])
    print (tweet.created_at, tweet.text)
    csvWriter.writerow([tweet.created_at, tweet.text.encode('utf-8')])

for media_file in media_files:
    wget.download(media_file)