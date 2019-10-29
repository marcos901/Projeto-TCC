import tweepy
import numpy as np
import csv
consumer_key = 'XXXXXXXXXXXXXXXXXXXXX'
consumer_secret = 'XXXXXXXXXXXXXXXXX'
access_token = 'XXXXXXXXXXXXXXXXXXXXXXXX'
access_token_secret = 'XXXXXXXXXXXXXXXXXXXXX'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

try:
    tweets_bozo = api.user_timeline(screen_name = 'jairbolsonaro',count = 200,include_rts = False)
except Exception:
    print('\n\n\nFoi impossível capturar os tweets!!!\n\n\n')
else:
    tweets_salvar = [[str(tweet.id_str), str(tweet.created_at), str(tweet.text)]  for tweet in tweets_bozo[:]]

    wtr = csv.writer(open ('jessica.csv', 'w', encoding="utf-8"), delimiter=',', lineterminator='\n')

    for x in tweets_salvar : 
        wtr.writerows([x])

        
print("Fim do código!!!")

