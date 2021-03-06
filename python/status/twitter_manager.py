#-*-coding:utf-8-*-
import time

class TwitterManager(object):

    def __init__(self, tw):
        self._twitter = tw

        self._has_retweet = False
        self._has_follower = False
        self._hashtag_messages = []
        self._mention_messages = []

        self._tweet_messages = []
        self._tweet_hourly_messages = []
        self._last_tweet_time = 0.0
        self._last_hourly_message_time = time.time()

    def tweet(self, message):
        # FIXME ここは、すでにツイートしたかどうかだけ判断する
        # tweet 100times/1hour  1time/37.5sec
        if time.time() - self._last_tweet_time > 40.:
            if message in self._tweet_hourly_messages:
                print("一時間以内に投稿されたメッセージです。")
                return
            else:
                self._tweet_messages.append(message)
                self._tweet_hourly_messages.append(message)
                print(self._tweet_hourly_messages)
                self._last_tweet_time = time.time()

        if time.time() - self._last_hourly_message_time > 3600.:
            print("1時間前に追加したメッセージを削除")
            # print(self._tweet_hourly_messages)
            self._tweet_hourly_messages = []
            self._last_hourly_message_time = time.time()

    def update(self):
        last_retweet_time = 0.0
        last_follower_time = 0.0
        last_hashtag_time = 0.0
        last_mention_time = 0.0
        while True:
            # tweet
            # FIXME ここで、40秒ごとに最初のメッセージを抜いて、ツイートする
            tweet_messages = self._tweet_messages
            self._tweet_messages = []
            if len(tweet_messages):
                self._twitter.tweet(tweet_messages[0])

            # # RT 75times/15min
            # if time.time() - last_retweet_time > 20.:
            #     self._has_retweet = self._has_retweet or self._twitter.has_retweet()
            #     last_retweet_time = time.time()
            # # Follower 900times/15min
            # if time.time() - last_follower_time > 30.:
            #     self._has_follower = self._twitter.has_follower()
            #     last_follower_time = time.time()
            # # hash 180times/15min
            # if time.time() - last_hashtag_time > 30.:
            #     hashtags = self._twitter.get_hashtags("のれんさま")
            #     self._hashtag_messages.extend(hashtags)
            #     last_hashtag_time = time.time()
            # mention 75times/15min
            if time.time() - last_mention_time > 15.:
                timeline = self._twitter.get_mention_timeline()
                self._mention_messages.extend(timeline)
                last_mention_time = time.time()
            time.sleep(1.)

    def get_data(self):
        has_retweet = self._has_retweet
        has_follower = self._has_follower
        hashtag_messages = self._hashtag_messages
        mention_messages = self._mention_messages
        self._has_retweet = False
        self._has_follower = False
        self._hashtag_messages = []
        self._mention_messages = []

        return {
            "retweet": has_retweet,
            "follower": has_follower,
            "hashtag": len(hashtag_messages) > 0,
            "mentions": ",".join(mention_messages)
        }
