from textblob import TextBlob 
import sys,tweepy
import matplotlib.pyplot as plt 					

# function to calculate percentage
def percentage(reac,num):
    return (100 * float(reac)/float(num))

# Provide unique credentials
consumer_key=''
consumer_secret=''
access_token=''
access_token_secret=''

auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)

api = tweepy.API(auth)

searchterm = input("Enter the search term or hashtag : ")
no_of_tweets  =int(input("Enter the number of tweets to be analyzed : "))

tweets =  tweepy.Cursor(api.search, q=searchterm).items(no_of_tweets)

positive,negative,neutral,polarity=0,0,0,0

for tweet in tweets:
    print(tweet.text)
    analysis = TextBlob(tweet.text)
    polarity+=analysis.sentiment.polarity

    if(analysis.sentiment.polarity == 0.00):
        neutral+=1
    if(analysis.sentiment.polarity < 0.00):
        negative+=1
    if(analysis.sentiment.polarity > 0.00):
        positive+=1

# calculating the percentage of positve, negative and neutral tweets
positive = percentage(positive,no_of_tweets)
negative = percentage(negative,no_of_tweets)
neutral = percentage(neutral,no_of_tweets)
polarity = percentage(polarity,no_of_tweets)

# printing the polarity value
print("people reaction on " + searchterm + " by analyzing " + str(no_of_tweets) + " tweets:")
if(polarity == 0):
    print("neutral ,polarity = ",polarity)
elif(polarity < 0):
    print("Negative, polarity = ",polarity)
elif(polarity > 0):
    print("positive, polarity = ",polarity)

# printing the percentage of positve, negative and neutral value
print("positive : ",positive)
print("negative : ",negative)
print("neutral : ",neutral)

# Representing the information in a pie chart
x=[positive,negative,neutral]
rec=["positive","negative","neutral"]
colors = ['green','red','yellow']
plt.pie(x,colors=colors,labels=rec,autopct="%1.1f%%")
plt.title("peple reaction on "+ searchterm +" by analyzing " + str(no_of_tweets) + " tweets ")
plt.show()
