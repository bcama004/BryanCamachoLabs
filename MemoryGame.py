from Buzzer import *
from Displays import *
from Button import *
from Lights import *
from CompositeLights import *
from Model import *
from machine import *
from RandomNumberGenerator import *


class MemoryGame:

    """
    This class is for the memory game which will feature color coded buttons and lights
    with a display showing an assortment of relevant messages
    """

    def __init__(self):
        self._display = LCDDisplay(sda = 0, scl = 1, i2cid = 0)
        self._buzzer = PassiveBuzzer(15)
        self.randomNumbers = []
        self.entriesValue = 0
        self.score = 0
        self._buttonRed = Button(16, "1", buttonhandler = self)
        self._buttonBlue = Button(17, "2", buttonhandler = self)
        self._buttonYellow = Button(18, "3", buttonhandler = self)
        self._buttonGreen = Button(19, "4", buttonhandler = self)
        self._lightRed = Light(13, "1")
        self._lightBlue = Light(12, "2")
        self._lightYellow = Light(26, "3")
        self._lightGreen = Light(22, "4")
        self._statusLight = NeoPixel(pin=9, numleds=16, brightness=1)
        self._randomArray = RandomNumberGenerator()
        self._model = Model(9, self, debug=True)
        self._model.addButton(self._buttonRed)
        self._model.addButton(self._buttonBlue)
        self._model.addButton(self._buttonYellow)
        self._model.addButton(self._buttonGreen)
        self._model.addTransition(0, [BTN1_PRESS, BTN2_PRESS, BTN3_PRESS, BTN4_PRESS], 1)  # Start -> Display Sequence
        self._model.addTransition(1, [NO_EVENT], 2)
        self._model.addTransition(2, [BTN1_PRESS], 3)
        self._model.addTransition(2, [BTN2_PRESS], 4)
        self._model.addTransition(2, [BTN3_PRESS], 5)
        self._model.addTransition(2, [BTN4_PRESS], 6)
        self._model.addTransition(7, [BTN1_PRESS, BTN2_PRESS, BTN3_PRESS, BTN4_PRESS], 1)
        self._model.addTransition(8, [BTN1_PRESS, BTN2_PRESS, BTN3_PRESS, BTN4_PRESS], 0)



    
    def run(self):
        """ Keep this app running """   
        self._model.run()

    """
    These methods will light a specific color light with its corresponsding sound
    when called.
    """
    def blinkRedLight(self):
        self._buzzer.beep(250)
        self._lightRed.blink()
  
    def blinkBlueLight(self):
        self._buzzer.beep(500)
        self._lightBlue.blink()

    def blinkYellowLight(self):
        self._buzzer.beep(750)
        self._lightYellow.blink()

    def blinkGreenLight(self):
        self._buzzer.beep(1000)
        self._lightGreen.blink()

    """
    State 0: Idle State.  Resets score and game pattern array.
    State 1: Pattern Generating State.  Automatically leads to State 2 when done.
    State 2: Input Entry State.  Keeps track of number of inputs entered and routes
    to different states based on the input.  A central state between correct inputs
    in a round.
    State 3: Red button input. Determines if the red button was the correct input
    and routes appropriately.
    State 4: Blue button input.  Determines if the blue button was the correct input
    and routes appropriately.
    State 5: Yellow button input.  Determines if the yellow button was the correct input
    and routes appropriately.
    State 6: Green button input.  Determines if the green button was the correct input
    and routes appropriately.
    State 7: Congratulates the player on a successful pattern entry.  Awards a point.
    State 8: Game Over State.  Ends the game after a mistake is input and shows
    the final score.
    """

    def stateEntered(self, state, event):
        if state == 0:
            self._display.reset()
            self.score = 0
            self._display.showText("You Ready to Go?")
            self._display.showText(f"Score: {self.score}", 1)
            randomNumbers = []
        elif state == 1:
            self._display.showText("Watch the Lights")
            self.entriesValue = 0
            self.randomNumbers = self._randomArray.generate_random_array()
            print(self.randomNumbers)
            for number in self.randomNumbers:
                lightNumber = number
                if lightNumber == 1:
                    self.blinkRedLight()
                elif lightNumber == 2 :
                    self.blinkBlueLight()
                elif lightNumber == 3:
                    self.blinkYellowLight()
                elif lightNumber == 4:
                    self.blinkGreenLight()
        elif state == 2:
            if self.entriesValue == 5:
                self._model.gotoState(7)
            else:
                self._display.showText("Enter the Colors")
        elif state == 3:
            self.blinkRedLight()
        elif state == 4:
            self.blinkBlueLight()
        elif state == 5:
            self.blinkYellowLight()
        elif state == 6:
            self.blinkGreenLight()
        elif state == 7:
            self.score = self.score + 1
            self._buzzer.beep(1500)
            self._statusLight.run(NeoPixel.RAINBOW)
            self._display.showText(f"Score: {self.score}", 1)
            self._display.showText("You got a Point!")
        elif state == 8:
            self._buzzer.beep(100)
            self._statusLight.onRed()
            self._display.showText("Nope, Game Over!")
            self._display.showText(f"Final Score: {self.score}", 1)


    def stateLeft(self, state, event):
        if state == 7:
            self._statusLight.off()
        elif state == 8:
            self._statusLight.off()

    def stateDo(self, state):
        if state == 2:
            if self.entriesValue == 5:
                self._model.gotoState(7)
        elif state == 3:
            if self.randomNumbers[self.entriesValue] == 1:
                self.entriesValue = self.entriesValue + 1
                self._model.gotoState(2)
            else:
                self._model.gotoState(8)
        elif state == 4:
            if self.randomNumbers[self.entriesValue] == 2:
                self.entriesValue = self.entriesValue + 1
                self._model.gotoState(2)
            else:
                self._model.gotoState(8)
        elif state == 5:
            if self.randomNumbers[self.entriesValue] == 3:
                self.entriesValue = self.entriesValue + 1
                self._model.gotoState(2)
            else:
                self._model.gotoState(8)
        elif state == 6:
            if self.randomNumbers[self.entriesValue] == 4:
                self.entriesValue = self.entriesValue + 1
                self._model.gotoState(2)
            else:
                self._model.gotoState(8)



    
