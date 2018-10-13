#-*-coding:utf-8-*-
import threading
import time

from speaker import Speaker

class Norensama(object):

    def __init__(self):
        self._speaker = Speaker()
    
    def main(self):
        start = time.time()
        print("main")
        self._speaker.say("yureta")
        print(time.time() - start)
        self._speaker.finish()

if __name__ == "__main__":
    noren = Norensama()
    noren.main()
