import pygame.mixer
from pygame.mixer import Sound
import time
from gpiozero import MotionSensor
from gpiozero import Button
from signal import pause

pygame.mixer.init()
pir = MotionSensor(4)
button = Button(2)
drum = Sound("test/ka_ru_na_2.wav")

while True:
    button.when_pressed = drum.play
    time.sleep(4)
    if pir.motion_detected:
        drum.play()
        print("Motion Detect!: !")
        time.sleep(4)
