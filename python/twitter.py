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
        self.old_mentions_created_at = ""
        self.old_hashtag_created_at = ""

    def tweet(self, message):
        # 投稿できる上限は、3時間に300ツイートまで
        params = {"status": message}
        res = self._session.post(TWEET_POST_URL, params = params)
        if res.status_code == 200:
            print("Text:{}".format(message))
        else:
            print("Tweet Failed. : %d, %s" % (res.status_code, message))

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

    def has_retweet(self):
        # 探索できる上限は、15分に75回まで
        params = {"count": 30} # 取得可能なツイート数上限は100Tweetまで
        res = self._session.get(RETWEET_RETRIVE_URL, params = params)
        self.retweet_count = 0
        ret = False
        if res.status_code == 200:
            print("RT Success.")
            retweets = json.loads(res.text)
            for tweet in retweets:
                self.retweet_count += int(tweet['retweet_count'])
            
            if self.retweet_count > self.old_retweet_count:
                diff_count = self.retweet_count - self.old_retweet_count
                print("リツイートの数が" + str(diff_count) + "増えました")
                self.old_retweet_count = self.retweet_count
                ret = True
            self.old_retweet_count = self.retweet_count
        else: #正常に通信ができなかった場合
            print("Retweet Failed. : %d"% res.status_code)
        return ret

    def has_follower(self):
        # 探索できる上限は、15分に900回まで
        params = {"user_id": 1053221484045336576}
        res = self._session.get(USER_PROFILE_URL, params = params)
        ret = False
        if res.status_code == 200:
            user = json.loads(res.text)
            followers_count = user.get("followers_count", 0)
            # print("フォロワー数" + str(user['followers_count']))
            if followers_count > self.old_followers_count:
                diff_count = followers_count - self.old_followers_count
                print("前回からフォロワー数が" + str(diff_count) + "増えました。")
                ret = True
            self.old_followers_count = followers_count
        else:
            print("Follower Failed. : %d"% res.status_code)
        return ret

    def get_hashtags(self,hashtag):
        # 探索できる上限は、15分に180回まで
        params = {"q": "#" + hashtag, "count": 30} # 取得可能なツイート上限は100まで
        res = self._session.get(HASHTAG_RETRIVE_URL , params = params)
        hashtag_tweet_list = []
        if res.status_code == 200:
            tweets = json.loads(res.text)
            hashtags = tweets.get('statuses', [])
            if len(hashtags) >0:
                for tweet in hashtags:
                    if self.old_hashtag_created_at == tweet['created_at']:
                        break
                    hashtag_tweet_list.append(tweet['text'].encode('utf-8'))
                self.old_hashtag_created_at = hashtags[0]['created_at']
            print len(hashtag_tweet_list)
        else:
            print("Hashtag Failed. : %d"% res.status_code)
        return hashtag_tweet_list

    def get_mention_timeline(self):
        # 探索できる上限は、15分に75回まで
        params = {"count": 30} # 取得可能なツイート上限は100まで
        res = self._session.get(MENTIONS_TIMELINE_URL , params = params)
        mention_tweet_list = []
        if res.status_code == 200:
            timelines = json.loads(res.text)
            if len(timelines) > 0:
                for tweet in timelines:
                    if self.old_mentions_created_at == tweet['created_at']:
                        break
                    mention_tweet_list.append(tweet['text'].encode('utf-8'))
                self.old_mentions_created_at = timelines[0]['created_at']
        else:
            print("Timeline Failed. : %d"% res.status_code)
        return mention_tweet_list
