def getgameroom():
    f = open('positions.py','r')
    f.readline()
    position = int(f.readline())
    f.close()
    return position

def getmaster():
    f = open('positions.py','r')
    position = int(f.readline())
    f.close()
    return position

def setpositions(master, gameroom):
    f = open('positions.py','w')
    f.write(str(master)+'\n' + str(gameroom))
    f.close()
