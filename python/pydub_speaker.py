#-*-coding:utf-8-*-
import os
import pydub
from pydub import playback as pb
import time


class Speaker(object):

    def __init__(self):
        pass

    def say(self, file_name):
        file_path = os.path.join(
            os.path.dirname(os.path.abspath(__file__)),
            "data/_secret_wav",
            "{}.wav".format(file_name)
        )
        sound = pydub.AudioSegment.from_file(file_path, "wav")
        pb.play(sound)
