# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import twitter
import time

apiTest = twitter.Api(consumer_key="1CEG7toKr7Pigoq6OvKgFSybk",
consumer_secret="pP6c8XczuH7MRCwuRwNabIonAE3jdyktO2uEcEK4ySk2GMKVup",
access_token_key="3196604737-bFLkOLlM8bhcgYqU0C63oqGC6V0eFA7ad2zpAvK",
access_token_secret="nSlpj0ZdrpRA8NinYpuEWEz4Ya11BHYPZFq3TE3i2Sy7h")

statuses = apiTest.GetUserTimeline(screen_name='evilphill62')


print [s.text for s in statuses]


#print(apiTest.VerifyCredentials())

#while (True):
#    stream = apiTest.GetStreamFilter(None, ['hello'])
#    try:
#        print(stream.next())
#        print "success"
#    except:
#        print ("No posts")
#()
#    time.sleep(3)
#api.GetStreamFilter(locations=["2.1,41.1,2.3,41.5"])
#{'locations': '2.1,41.1,2.3,41.5'}
count = 0
data = {}
for tweet in apiTest.GetStreamFilter(track = ["hi"]):#,locations=["54.9,35.9,56.6,39.5"]):
    if tweet.get("coordinates") != None:
        print tweet.get("coordinates")
        print str(count) + "\n"
        count+=1
        print str(count) + "\n"
#    if count == 3:
#        break
