"""Implementation of the state pattern"""
import itertools


class State(object):
    """Base state. This is to share functionality"""

    def scan(self):
        """Scan the dial to the next station"""
        print "Scanning... Station is", self.stations.next(), self.name


class AmState(State):
    def __init__(self, radio):
        self.radio = radio
        self.stations = itertools.cycle(["1250", "1380", "1510"])
        self.name = "AM"

    def toggle_amfm(self):
        print "Switching to FM"
        self.radio.state = self.radio.fmstate


class FmState(State):
    def __init__(self, radio):
        self.radio = radio
        self.stations = itertools.cycle(["81.3", "89.1", "103.9"])
        self.name = "FM"

    def toggle_amfm(self):
        print "Switching to AM"
        self.radio.state = self.radio.amstate


class Radio(object):
    """A radio.
    It has a scan button, and an AM/FM toggle switch."""

    def __init__(self):
        """We have an AM state and an FM state"""

        self.amstate = AmState(self)
        self.fmstate = FmState(self)
        self.state = self.amstate

    def toggle_amfm(self):
        self.state.toggle_amfm()

    def scan(self):
        self.state.scan()


def main():
    ''' Test our radio out '''
    radio = Radio()
    actions = ([radio.scan] * 2 + [radio.toggle_amfm] + [radio.scan] * 2) * 2
    for action in actions:
        action()

if __name__ == '__main__':
    main()
