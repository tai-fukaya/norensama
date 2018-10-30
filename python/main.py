#-*-coding:utf-8-*-
from datetime import datetime
import random
import threading
import time

import _secret as config
# StatusManager
from status import StatusManager, TwitterManager
from twitter import Twitter

# from pyaudio_speaker import Speaker
from pydub_speaker import Speaker

from ifttt import Ifttt
# Action
from action import *
from action.blow import Yurayura, Soyosoyo, Byubyu


class Norensama(object):

    def __init__(self):
        self._speaker = Speaker()
        self._ifttt = Ifttt({
            "api_key": config.IFTTT_APIKEY
        })
        self._twitter = Twitter({
            "consumer_key": config.TWITTER_CONSUMER_KEY,
            "consumer_secret": config.TWITTER_CONSUMER_SECRET,
            "access_token": config.TWITTER_ACCESS_TOKEN,
            "access_token_secret": config.TWITTER_ACCESS_TOKEN_SECRET,
        })
        self._twitter_manager = TwitterManager(self._twitter)
        self._status = StatusManager()

        self._twitter_actions = [
            TwitterDirtyWords(self._speaker),
            TwitterGreeting(self._speaker),
            TwitterHanashi(self._speaker),
            TwitterHowOld(self._speaker),
            TwitterIkku(self._speaker),
            TwitterNormal(self._speaker),
            TwitterSize(self._speaker),
            TwitterWhoAreYou(self._speaker),
        ]
        self._actions = [
            # あいさつ
            TimeSignal(self._speaker),
            GreetingCommuter(self._speaker),
            SoLonely(self._speaker),
            Ghost(self._speaker),
            Byebye(self._speaker),
            Hello(self._speaker),
            HelloDoor(self._speaker),
            HelloGuide(self._speaker),
            Talk(self._speaker),
            TalkDoor(self._speaker),
            TalkGuide(self._speaker),
            # コレド紹介
            IntroductionCoredo(self._speaker),
            IntroductionNight(self._speaker),
            IntroductionHungryLunch(self._speaker),
            IntroductionHungryNight(self._speaker),
            # # 風の音系
            # Soyosoyo(self._speaker),
            # Yurayura(self._speaker),
            # Byubyu(self._speaker),
            # 日付
            Today(self._speaker),
            # 天気
            WeatherWarm(self._speaker),
            WeatherCold(self._speaker),
            WeatherCloudy(self._speaker),
            WeatherRainy(self._speaker),
            WeatherSunny(self._speaker),
            WeatherRainyTomorrow(self._speaker),
            WeatherSunnyTomorrow(self._speaker),
            WeatherCloudyTomorrow(self._speaker),
        ]

        day = datetime.now().day
        if day == 3:
            self._actions.append(Day1103(self._speaker))
        elif day == 9:
            self._actions.append(Day1109(self._speaker))
            self._actions.append(Day1109Restaurant(self._speaker))
        elif day == 10:
            self._actions.append(Day1110(self._speaker))
            self._actions.append(Day1110Restaurant(self._speaker))
            # self._actions.append(DaySorry(self._speaker))
        elif day == 11:
            self._actions.append(Day1111(self._speaker))
            # self._actions.append(DaySorry(self._speaker))

        # セリフの強制実行
        self._force_speak_action = ForceSpeak(self._speaker)
        self._blow_action_index = 1

    def main(self):
        print("main")
        status_thread = threading.Thread(target=self._status.update)
        status_thread.daemon = True
        status_thread.start()
        twitter_thread = threading.Thread(target=self._twitter_manager.update)
        twitter_thread.daemon = True
        twitter_thread.start()

        self._status.set_serif_names(self._force_speak_action.get_serif_names())

        while True:
            time.sleep(.1)

            data = self._status.get_data()
            data["twitter"] = self._twitter_manager.get_data()

            # センサー反応
            runable_action = [x for x in self._actions if x.check(data)]
            if runable_action:
                print("action")
                start = time.time()
                idx = int(random.random()*len(runable_action))
                message = runable_action[idx].run(data)
                self._twitter_manager.tweet(message)
                print(time.time() - start)

            # ツイッター反応系
            tw_runable_action = [x for x in self._twitter_actions if x.check(data)]
            if tw_runable_action:
                print("twitter action")
                start = time.time()
                idx = int(random.random()*len(tw_runable_action))
                message = tw_runable_action[idx].run(data)
                self._twitter_manager.tweet(message)
                print(time.time() - start)
  
            # 強制起動もここでやる
            if self._force_speak_action.check(data):
                message = self._force_speak_action.run(data)
                self._twitter_manager.tweet(message)
    
if __name__ == "__main__":
    noren = Norensama()
    noren.main()
