#-*-coding:utf-8-*-
import time

class ActionBase(object):

    # 一定期間（秒）、やすむ
    REST_DURATION = 10.

    def __init__(self, speaker):
        self._sp = speaker

        self._last_running_time = 0.

    def check(self, data):
        """ 実行するかどうか """
        return data["now"] - self._last_running_time > self.REST_DURATION
        
    def run(self, data):
        time.sleep(1.)
        self._last_running_time = time.time()
        return None
