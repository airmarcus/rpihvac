import sys
import time
import RPi.GPIO as GPIO
import fileinterface
import sys

args = sys.argv
print("Moving" + args[1] + ":" + args[2])

MasterStepPinForward = 13
MasterStepPinBackward = 15
GameroomStepPinForward = 16
GameroomStepPinBackward = 18

fulltime = .775

def makemove(pin, ptime):
    GPIO.cleanup()
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(MasterStepPinForward, GPIO.OUT)
    GPIO.setup(MasterStepPinBackward, GPIO.OUT)
    GPIO.setup(GameroomStepPinForward, GPIO.OUT)
    GPIO.setup(GameroomStepPinBackward, GPIO.OUT)
    GPIO.output(pin, GPIO.HIGH)
    print('ptime=' + str(ptime))
    time.sleep(ptime)
    GPIO.output(pin, GPIO.LOW)
    GPIO.cleanup()

def move(room, position):
    if (position > 100) or (position < 0):
        return
    gameroompos = fileinterface.getgameroom()
    masterpos = fileinterface.getmaster()
    runtime = 0.01
    if room == "gameroom":
        runtime = float(position-gameroompos)/100*fulltime
        pin = GameroomStepPinForward if runtime >0 else GameroomStepPinBackward
        gameroompos = position
        print("Moving GR to " + str(position))
    else:
        runtime = float(position-masterpos)/100*fulltime
        pin = MasterStepPinForward if runtime >0 else MasterStepPinBackward
        masterpos = position
        print("Moving Master to " + str(position))
    fileinterface.setpositions(masterpos, gameroompos)
    runtime = -runtime if runtime < 0 else runtime
    print(str(pin)+' ' + str(runtime))
    makemove(pin,runtime)

move(args[1],int(args[2]))
