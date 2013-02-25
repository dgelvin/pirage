#!/usr/bin/env python

import threading
import signal
import logging

logger = logging.getLogger()

class Controller:
    '''
    This is a basic controller class. It starts all the threads, handles SIGTERM and SIGINT,
    and stops and rejoins the threads cleanly. The __main__ thread will wait in the controllers
    wait method.
    '''

    # The controller poll frequency is inconsequential- it will catch a signal immediately
    POLL_FREQUENCY = 10


    def __init__(self):
        self.kill_event = threading.Event()
        #self.web_server_thread = WebServerThread(self.received_queue)
        #self.server_post_thread = ServerPostThread(self.kill_event, self.received_queue, self.outgoing_queue)
        #self.modem_post_thread = ModemPostThread(self.kill_event, self.outgoing_queue)

    def start(self):
        logger.info("starting")
        #self.web_server_thread.start()
        #self.server_post_thread.start()
        #self.modem_post_thread.start()

    def wait(self):
        while not self.kill_event.is_set():
            self.kill_event.wait(self.POLL_FREQUENCY)
        logger.info("exited cleanly")
            #self.web_server_thread.server.shutdown()
            #self.web_server_thread.join()
            #self.server_post_thread.join()
            #self.modem_post_thread.join()

    def sig_handler(self, signum, frame):
        self.kill_event.set()


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG,
                        datefmt="[%Y-%m-%d %T]",
                        format="%(asctime)s (%(threadName)s) %(levelname)s: %(message)s")

    controller = Controller()
    signal.signal(signal.SIGINT, controller.sig_handler)
    signal.signal(signal.SIGTERM, controller.sig_handler)
    controller.start()
    controller.wait()