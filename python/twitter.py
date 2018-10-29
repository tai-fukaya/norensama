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

        self.followers_count = 0


    def tweet(self, message):
        # 投稿できる上限は、3時間に300ツイートまで
        params = {"status": message}
        res = self._session.post(TWEET_POST_URL, params = params)
        print(res)
        if res.status_code == 200: #正常投稿出来た場合
            print("Tweet Success.")
            print("Text:{}".format(message))
        else: #正常投稿出来なかった場合
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
        if res.status_code == 200: #正常に通信ができた場合
            print("Success.")
            retweets = json.loads(res.text) #レスポンスからリツイートリストを取得
            for tweet in retweets: #リツイートリストをループ処理
                # print(tweet)
                print(tweet['user']['name']+'::'+tweet['text'])
                print(tweet['created_at'])
                print(tweet['retweet_count'])
                print('*******************************************')
        else: #正常に通信ができなかった場合
            print("Failed. : %d"% res.status_code)

    def follower_retrive(self):
        params = {"user_id": 1053221484045336576}
        res = self._session.get(USER_PROFILE_URL, params = params)
        if res.status_code == 200: #正常に通信ができた場合
            print("Success.")
            user = json.loads(res.text)
            print(user['followers_count'])
            if user['followers_count'] > self.followers_count:
                print("前回からフォロワー数が増えました。")
                self.followers_count = user['followers_count']
                return True

            elif user['followers_count'] < self.followers_count:
                print("前回からフォロワー数が減りました。")
                self.followers_count = user['followers_count']
                return False

            else:
                print("前回とフォロワー数が変わりません。")
                return False
        else:
            print("Failed. : %d"% res.status_code)
            return False


    def hashtag_retrive(self,hashtag):
        # 探索できる上限は、15分に180回まで
        params = {"q": "#" + hashtag, "count": 100} # 取得可能なツイート上限は100まで
        res = self._session.get(HASHTAG_RETRIVE_URL , params = params)
        if res.status_code == 200: #正常に通信ができた場合
            print("Success.")
            tweets = json.loads(res.text) #レスポンスからリツイートリストを取得
            for tweet in tweets['statuses']: #リツイートリストをループ処理
                print(tweet['user']['name']+'::'+tweet['text'])
                print(tweet['created_at'])
                print('*******************************************')
        else: #正常に通信ができなかった場合
            print("Failed. : %d"% res.status_code)

    def mentions_timeline(self):
        # reload(sys)
        # sys.setdefaultencoding('utf-8')
        params = {"count": 100} # 取得可能なツイート上限は100まで
        res = self._session.get(MENTIONS_TIMELINE_URL , params = params)
        if res.status_code == 200: #正常に通信ができた場合
            print("Success.")
            timelines = json.loads(res.text) #レスポンスからリツイートリストを取得
            for tweet in timelines: #リツイートリストをループ処理
                print(tweet['user']['name']+'::'+tweet['text'])
                print(tweet['created_at'])
                print('*******************************************')
                    # else:
                    #     print("よく聞こえなかったのう")
        else: #正常に通信ができなかった場合
            print("Failed. : %d"% res.status_code)
