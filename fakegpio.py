class GPIO:
    OUT = 0
    IN = 1
    BCM = 11

    outputs = {}
    inputs = {}

    @staticmethod
    def setmode(mode):
        pass

    @staticmethod
    def cleanup():
        pass

    @classmethod
    def setup(cls, num, direction):
        if direction == cls.OUT:
            cls.outputs[num] = None
        else:
            cls.inputs[num] = None

    @classmethod
    def input(cls, num):
        if num not in cls.inputs:
            raise Exception("%s not a GPIO input" % num)

        return cls.inputs[num]

    @classmethod
    def output(cls, num, value):
        if num not in cls.outputs:
            raise Exception("%s not a GPIO output" % num)

        cls.outputs[num] = value




