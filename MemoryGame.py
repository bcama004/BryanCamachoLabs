from Buzzer import *
from Displays import *
from Button import *
from Lights import *
from CompositeLights import *
from Model import *
from machine import *

class MemoryGame:

"""
This class is for the memory game which will feature color coded buttons and lights
with a display showing an assortment of relevant messages
"""

  def __init__(self):
    self._display = LCDDisplay(sda = 0, scl = 1, i2cid = 0)
    self._buzzer = PassiveBuzzer(15)
    self._buttonRed = Button(16, "1", buttonhandler = self)
    self._buttonBlue = Button(17, "2", buttonhandler = self)
    self._buttonYellow = Button(18, "3", buttonhandler = self)
    self._buttonGreen = Button(19, "4", buttonhandler = self)
    self._buttonReset = Button(11, "reset", buttonhandler = self)
    self._buttonChangeState = Button(10, "change", buttonhandler = self)
    self.display()
  

  def display(self):

"""
Welcome Message
"""

    self._display.showText('Test Your Mind')


  def run(self):
        """ Keep this app running """   
    
        while True:
            time.sleep(0.5)

  def exit(self):        
    self.exit()

"""
Methods for button behaviors
"""

  def blinkRedLight(self):
    lightRed = Light(13, "1")
    self._buzzer.beep(250)
    lightRed.blink()
  
  def blinkBlueLight(self):
    lightBlue = Light(12, "2")
    self._buzzer.beep(500)
    lightBlue.blink()

  def blinkYellowLight(self):
    lightYellow = Light(26, "3")
    self._buzzer.beep(750)
    lightYellow.blink()

  def blinkGreenLight(self):
    lightGreen = Light(22, "4")
    self._buzzer.beep(1000)
    lightGreen.blink()

  def playSequence(self):
    self.blinkBlueLight()
    self.blinkGreenLight()
    self.blinkBlueLight()
    self.blinkRedLight()
    self.blinkYellowLight()


  def buttonPressed(self, name):
        """Handle the button presses """
        if name == "1":
          self.blinkRedLight()
        elif name == "2":
          self.blinkBlueLight()
        elif name == "3":
          self.blinkYellowLight()
        elif name == "4":
          self.blinkGreenLight()
        elif name == "change":
          self.playSequence()
        elif name == "reset":
          self._display.reset()
          self._display.showText('Bye Bye')
          time.sleep(1.0)
          self._display.reset()
  
  def buttonReleased(self, name):
        """ Handle button releases """
        pass 
    
