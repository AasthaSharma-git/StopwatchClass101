import time
import os
from playsound import playsound

hurry = int(input("Enter the time in second :- "))
playsound("D:/C101/countdown.mp3")



def countdowntime(second):
    while(second >= 0):
        print("Time remaining :- ",second, end="\r")
        second = second-1
        time.sleep(1)

    playsound("D:/C101/notification-bell.wav")

countdowntime(hurry)