import tweepy


class TweetFlood:

    def __init__(self, flood, split_length=140, username="utkucanbykl"):

        self.flood = str(flood)
        self.split_length = split_length
        self.__api = None
        self.username = username

    def __split_tweet(self):

        split_flood = self.flood.split(" ")
        return [t for t in split_flood]

    def setAuth(self, consumer, consumer_secret, access, access_secret):

        try:
            auth = tweepy.OAuthHandler(consumer, consumer_secret)
            auth.set_access_token(access, access_secret)
            self.__api = tweepy.API(auth)

        except BaseException:
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

        if auth is None:
            raise BaseException("First set auth")
        count = 0
        for tweet in self.__tweet_array():
            try:
                if count > 0:
                    last_tweet = auth.user_timeline(screen_name=self.username, count=1)
                    auth.update_status(tweet, last_tweet[0].id)
                else:
                    auth.update_status(tweet)
                    count += 1
            except:
                return False
        return True

    def send_tweet_with_media(self, *media):

        if not media:
            raise BaseException("Add Media Path")

        auth = self.getAuth()

        if auth is None:
            raise BaseException("First set auth")
        media_ids = []
        count = 0
        for m in media:
            res = auth.media_upload(m)
            media_ids.append(res.media_id)

        for tweet in self.__tweet_array():
            try:
                if count > 0:
                    last_tweet = auth.user_timeline(screen_name=self.username, count=1)
                    auth.update_status(tweet, last_tweet[0].id)
                else:
                    auth.update_status(tweet, media_ids=media_ids)
                    count += 1
            except:
                return False
        return True
