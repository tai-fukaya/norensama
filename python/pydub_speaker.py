#-*-coding:utf-8-*-
import os
import pydub
from pydub import playback as pb
import time


class Speaker(object):

    def __init__(self):
        pass

    def say(self, file_name):
        start = time.time()
        file_path = os.path.join(
            os.path.dirname(os.path.abspath(__file__)),
            "data/_secret_wav",
            "{}.wav".format(file_name)
        )
        if not os.path.exists(file_path):
            print("this file does not exist:{}".format(file_name))
            return
        print(file_name)
        sound = pydub.AudioSegment.from_file(file_path, "wav")
        print(time.time() - start)
        pb.play(sound)
        print(time.time() - start)
