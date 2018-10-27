#-*-coding:utf-8-*-
# https://qiita.com/bakira/items/00743d10ec42993f85eb
# https://su-gi-rx.com/archives/942#3_StreamListener
from requests_oauthlib import OAuth1Session
import json
import sys

TWEET_POST_URL = "https://api.twitter.com/1.1/statuses/update.json"
RETWEET_RETRIVE_URL = "https://api.twitter.com/1.1/statuses/retweets_of_me.json"
FOLOWER_RETRIVE_URL = "https://api.twitter.com/1.1/followers/list.json"
HASHTAG_RETRIVE_URL = "https://api.twitter.com/1.1/search/tweets.json"
MENTIONS_TIMELINE_URL = "https://api.twitter.com/1.1/statuses/mentions_timeline.json"

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

    def tweet(self, message):
        # 投稿できる上限は、3時間に300ツイートまで
        params = {"status": message}
        res = self._session.post(TWEET_POST_URL, params = params)
        print(res)
        if res.status_code == 200: #正常投稿出来た場合
            print("Success.")
            print("tweet:{}".format(message))
        else: #正常投稿出来なかった場合
            print("Failed. : %d"% res.status_code)

    def retweet_retrive(self):
        # 探索できる上限は、15分に75回まで
        params = {"count": 5} # 取得可能なツイート数上限は100Tweetまで
        res = self._session.get(RETWEET_RETRIVE_URL, params = params)
        if res.status_code == 200: #正常に通信ができた場合
            print("Success.")
            retweets = json.loads(res.text) #レスポンスからリツイートリストを取得
            for tweet in retweets: #リツイートリストをループ処理
                print(tweet['user']['name']+'::'+tweet['text'])
                print(tweet['created_at'])
                print('*******************************************')
        else: #正常に通信ができなかった場合
            print("Failed. : %d"% res.status_code)

    def follower_retrive(self):
        # 探索できる上限は、15分に15回まで
        params = {"user_id": 1053221484045336576, "count": 20} # 取得可能なユーザー数上限は200まで
        res = self._session.get(FOLOWER_RETRIVE_URL, params = params)
        if res.status_code == 200: #正常に通信ができた場合
            print("Success.")
            followers = json.loads(res.text) #レスポンスからリツイートリストを取得
            for user in followers['users']: #リツイートリストをループ処理
                print(user['name'])
                print(user['created_at'])
                print('*******************************************')
        else: #正常に通信ができなかった場合
            print("Failed. : %d"% res.status_code)


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
        reload(sys)
        sys.setdefaultencoding('utf-8')
        params = {"count": 100} # 取得可能なツイート上限は100まで
        react_text = {
            "何才": "おいらは500才じゃ",
            "だれ": "おいらはのれんさまじゃ",
            "たべもの": "おいらは鰹節が好きなんじゃ",
            "身長": "おいらは世界で一番大きい暖簾なんじゃ",
            "句を読んで": "閑けさや 街に染み入る 日本橋 どうじゃ？？名作じゃろ？？えっ？？聞いたことあるっじゃと？",
            "こんにちは": "こんにちは",
            "下品な言葉": "日本橋を歩くものは上品でないとな",
            "Hey,のれんさま": "おいらがみえるのか",
            "もうつくよ": "待ち合わせかのう",
        }
        res = self._session.get(MENTIONS_TIMELINE_URL , params = params)
        if res.status_code == 200: #正常に通信ができた場合
            print("Success.")
            timelines = json.loads(res.text) #レスポンスからリツイートリストを取得
            for tweet in timelines: #リツイートリストをループ処理
                for key in react_text:
                    if key in tweet['text']:
                        print(react_text[key])
                        print(tweet['user']['name']+'::'+tweet['text'])
                        print(tweet['created_at'])
                        print('*******************************************')
                    else:
                        print("よく聞こえなかったのう")
        else: #正常に通信ができなかった場合
            print("Failed. : %d"% res.status_code)
