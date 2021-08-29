import time

class Timer:

    def __init__(self):
        self._start_time = 0
        self._time = 0


    def startTimer(self):
        #timer was already started
        if(self._start_time != 0):
            return -1

        self._start_time = time.time()
        return 0


    def stopTime(self):
        #have not started the timer
        if(self._start_time == 0):
            return -1

        self._time = time.time() - self._start_time
        return 0


    def get_time(self):
        return self._time

    
    def reset_timer(self):
        self._start_time = 0
        self._time = 0