#-*-coding:utf-8-*-
import time


class StatusManager(object):

    def __init__(self):
        self._now = 0.
    
    def update(self):
        while True:
            self._now = time.time()
            # TODO センサー情報
            # TODO 天気情報
            # TODO 強制実行アクション取得
            time.sleep(.1)

    def get_data(self):
        return {"now": self._now}
