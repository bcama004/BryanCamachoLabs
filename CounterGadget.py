from Buzzer import *
from Button import *
from Displays import *


class CounterGadget:
    """
    This is the class for the counter gadget that can count up, reset,
    and display a count on an LCD
    """

    def __init__(self):
        self._number = 0
        self._display = LCDDisplay(sda = 0, scl = 1, i2cid = 0)
        self._buzzer = PassiveBuzzer(15)
        self._buttonUp = Button(17, "up", buttonhandler = self)
        self._buttonReset = Button(16, "reset", buttonhandler = self)
        self.display()

    def increment(self):
        """ Add one to the number attribute """
        self._number = self._number + 1  

    def reset(self):
        """Reset the number attributes """
        self._number = 0

    def display(self):
        """ Show the numbers on the Display """
        self._display.showNumber(self._number)  

    def buzzer(self):
        self._buzzer.beep()

    def run(self):
        """ Keep this app running """   
    
        while True:
            time.sleep(0.5)

    def buttonPressed(self, name):
        """Handle the button presses """
        if name == "up":
            self.increment()
        elif name == "reset":
            self.reset()
            self.buzzer()
        self.display()

    def buttonReleased(self, name):
        """ Handle button releases """
        pass        
