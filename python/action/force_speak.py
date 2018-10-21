#-*-coding:utf-8-*-
import os
import time

from action_base import ActionBase

class ForceSpeak(ActionBase):

    SERIF_DATA = {
        "わ":"wa",
    }


    def __init__(self, speaker):
        super(ForceSpeak, self).__init__(speaker)
        # data/_secret_wav以下
        folder_path = os.path.join(
            os.path.dirname(os.path.abspath(__file__)),
            "../data/_secret_wav"
        )
        self._file_names = []
        for _, _, files in os.walk(folder_path):
            for f in files:
                if ".wav" in f:
                    self._file_names.append(f[:-4])
            # TODO 再帰処理

        self._next_serif = ""

    def check(self, data):
        ret = False
        if data["force_serif"] in self._file_names:
            self._next_serif = data["force_serif"]
            ret = True
        return ret

    def run(self, data):
        if not self._next_serif:
            return None
        self._sp.say(self._next_serif)
        time.sleep(1.)
 
        return self._next_serif
        