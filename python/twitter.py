#-*-coding:utf-8-*-
# https://qiita.com/bakira/items/00743d10ec42993f85eb
# https://su-gi-rx.com/archives/942#3_StreamListener
from requests_oauthlib import OAuth1Session
import json
import sys

TWEET_POST_URL = "https://api.twitter.com/1.1/statuses/update.json"
TWEET_DELETE_URL = "https://api.twitter.com/1.1/statuses/destroy/"
RETWEET_RETRIVE_URL = "https://api.twitter.com/1.1/statuses/retweets_of_me.json"
USER_PROFILE_URL = "https://api.twitter.com/1.1/users/show.json"
HASHTAG_RETRIVE_URL = "https://api.twitter.com/1.1/search/tweets.json"
MENTIONS_TIMELINE_URL = "https://api.twitter.com/1.1/statuses/mentions_timeline.json"
MY_TIMELINE_URL = "https://api.twitter.com/1.1/statuses/user_timeline.json"


class Twitter(object):

    def __init__(self, config):
        self.consumer_key = config.get("consumer_key")
        self.consumer_secret = config.get("consumer_secret")
        self.access_token = config.get("access_token")
        self.access_token_secret = config.get("access_token_secret")

        self._session = OAuth1Session(
            self.consumer_key,self.consumer_secret,
            self.access_token, self.access_token_secret
        )

        self.old_retweet_count = 0
        self.old_followers_count = 0
        self.old_message = ""
        self.old_mentions_created_at = ""
        self.old_hashtag_created_at = ""


    def tweet(self, message):
        # 投稿できる上限は、3時間に300ツイートまで
        if self.old_message == message:
            print("前回と同じ内容はつぶやけません。")
            return
        params = {"status": message}
        res = self._session.post(TWEET_POST_URL, params = params)
        if res.status_code == 200:
            print("Text:{}".format(message))
            self.old_message = message
        else:
            print("Tweet Failed. : %d"% res.status_code)

    def destroy_tweet(self,count):
        timelines_params ={'count' : count}
        timelines_res = self._session.get(MY_TIMELINE_URL, params = timelines_params)
        if timelines_res.status_code == 200:
            timeline = json.loads(timelines_res.text)
            for tweet in timeline:
                print(tweet['user']['name']+'::'+tweet['text'])
                print(tweet['id'])
                destroy_params ={'id' : tweet['id']}
                destroy_res = self._session.post(TWEET_DELETE_URL + str(tweet['id']) + ".json", params = destroy_params)
                print('----------------------------------------------------')
        else:
            print("削除できるツイートがありません。 : %d"% res.status_code)

    def retweet_retrive(self):
        # 探索できる上限は、15分に75回まで
        params = {"count": 100} # 取得可能なツイート数上限は100Tweetまで
        res = self._session.get(RETWEET_RETRIVE_URL, params = params)
        self.retweet_count = 0
        if res.status_code == 200:
            print("Success.")
            retweets = json.loads(res.text)
            for tweet in retweets:
                print(tweet['user']['name']+'::'+tweet['text'])
                print(tweet['created_at'])
                print(("リツイート総数" + str(tweet['created_at']))
                print('*******************************************')
                self.retweet_count += int(tweet['retweet_count'])
            if self.retweet_count > self.old_retweet_count:
                diff_count = self.retweet_count - self.old_retweet_count
                print("リツイートの数が" + str(diff_count) + "増えました")
                self.old_retweet_count = self.retweet_count
            elif self.retweet_count < self.old_retweet_count:
                diff_count = self.retweet_count - self.old_retweet_count
                print("リツイートの数が" + str(diff_count) + "減りました")
                self.old_retweet_count = self.retweet_count
            else:
                print("リツイートの数は変わっていません")
                diff_count = self.retweet_count - self.old_retweet_count
            return diff_count
        else: #正常に通信ができなかった場合
            print("Failed. : %d"% res.status_code)

    def follower_retrive(self):
        params = {"user_id": 1053221484045336576}
        res = self._session.get(USER_PROFILE_URL, params = params)
        if res.status_code == 200:
            print("Success.")
            user = json.loads(res.text)
            print(user['followers_count'])
            if user['followers_count'] > self.old_followers_count:
                print("前回からフォロワー数が増えました。")
                diff_count = user['followers_count'] - self.old_followers_count
                self.old_followers_count = user['followers_count']

            elif user['followers_count'] < self.old_followers_count:
                print("前回からフォロワー数が減りました。")
                diff_count = user['followers_count'] - self.old_followers_count
                self.old_followers_count = user['followers_count']

            else:
                print("前回とフォロワー数が変わりません。")
                diff_count = user['followers_count'] - self.old_followers_countg
            return diff_count

        else:
            print("Failed. : %d"% res.status_code)


    def hashtag_retrive(self,hashtag):
        # 探索できる上限は、15分に180回まで
        params = {"q": "#" + hashtag, "count": 100} # 取得可能なツイート上限は100まで
        res = self._session.get(HASHTAG_RETRIVE_URL , params = params)
        hashtag_tweet_list = []
        if res.status_code == 200:
            print("Success.")
            tweets = json.loads(res.text)
            for tweet in tweets['statuses']:
                if self.old_hashtag_created_at == tweet['created_at']:
                    return hashtag_tweet_list
                print(tweet['user']['name']+'::'+tweet['text'])
                print(tweet['created_at'])
                print('*******************************************')
                hashtag_tweet_list.append(tweet['text'])
            self.old_hashtag_created_at = tweets['statuses'][0]['created_at']
            return hashtag_tweet_list
        else:
            print("Failed. : %d"% res.status_code)

    def mentions_timeline(self):
        # 探索できる上限は、15分に75回まで
        params = {"count": 100} # 取得可能なツイート上限は100まで
        res = self._session.get(MENTIONS_TIMELINE_URL , params = params)
        mention_tweet_list = []
        if res.status_code == 200:
            timelines = json.loads(res.text)
            for tweet in timelines:
                if self.old_mentions_created_at == tweet['created_at']:
                    return mention_tweet_list
                print(tweet['user']['name']+'::'+tweet['text'])
                print(tweet['created_at'])
                print('*******************************************')
                mention_tweet_list.append(tweet['text'])
            self.old_mentions_created_at = timelines[0]['created_at']
            return mention_tweet_list
        else:
            print("Failed. : %d"% res.status_code)
