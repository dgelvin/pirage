import threading
import logging
from devices import Garage

logger = logging.getLogger()


class InputThread(threading.Thread):

    POLL_FREQUENCY = 0.1

    GARAGE_SENSOR = 17
    BUTTON_INPUT = 25
    LIGHT_SWITCH = 23

    BUTTON_RELAY = 4
    LIGHT_RELAY = 24

    def __init__(self, kill_event):
        threading.Thread.__init__(self, name='InputThread')
        self.kill_event = kill_event
        self.garage = Garage(self.GARAGE_SENSOR, self.BUTTON_INPUT, self.BUTTON_RELAY)

    def run(self):
        logger.debug("starting")
        while not self.kill_event.is_set():
            self.kill_event.wait(self.POLL_FREQUENCY)
        logger.debug("exited cleanly")
