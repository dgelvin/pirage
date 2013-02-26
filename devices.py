from fakegpio import GPIO
from output_thread import OutputThread


class Switch(object):
    def __init__(self, num):
        self.num = num
        self.state = self._get_state()

    def _get_state(self):
        return GPIO.input(self.num)


class Garage(object):

    def __init__(self, sensor, button_input, button_relay):
        pass


    def toggle(self):
        OutputThread.todo.put_nowait(self.button_relay, )



class Relay(object):
    pass