import tweepy

class TweetFlood():

    def __init__(self, flood, split_length=140):

        self.flood = str(flood)
        self.split_length = split_length
        self.__api = None

    def __split_tweet(self):

        split_flood = self.flood.split(" ")
        return [t for t in split_flood]

    def setAuth(self, consumer, consumer_secret, access, access_secret):

        try:
            auth = tweepy.OAuthHandler(consumer, consumer_secret)
            auth.set_access_token(access, access_secret)
            self.__api = tweepy.API(auth)
        except:
            raise BaseException("import err")

    def getAuth(self):
        return self.__api

    def __tweet_array(self):

        all_tweet = self.__split_tweet()
        count = 0
        tweet = ""
        tweet_array = []
        for t in all_tweet:

            if count + len(t) + 1 <= self.split_length:
                tweet = tweet + " " + t
                count = len(tweet)
            elif len(t) <= self.split_length:
                tweet_array.append(tweet)
                count = len(t)
                tweet = t
        tweet_array.append(tweet)

        return tweet_array

    def send_tweet(self):

        auth = self.getAuth()

        if auth == None:
            raise BaseException("First set auth")

        for tweet in self.__tweet_array():
            try:
                auth.update_status(tweet)
            except:
                return False
        return True
