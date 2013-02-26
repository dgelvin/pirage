import Queue
import threading
import logging

from fakegpio import GPIO

logger = logging.getLogger()


class OutputThread(threading.Thread):

    POLL_FREQUENCY = 0.1

    todo = Queue.Queue()

    def __init__(self, kill_event):
        threading.Thread.__init__(self, name='OutputThread')
        self.kill_event = kill_event

    def run(self):
        logger.debug("starting")
        while not self.kill_event.is_set():
            while not self.todo.empty():
                try:
                    num, value = self.todo.get_nowait()
                except Queue.Empty:
                    continue
                logging.debug("setting %s to %s" % (num, value))
                GPIO.output(num, value)

            self.kill_event.wait(self.POLL_FREQUENCY)
        logger.debug("exited cleanly")
