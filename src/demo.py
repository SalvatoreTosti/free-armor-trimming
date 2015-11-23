from clickLogger import clickLogger
from keyLogger import keyLogger
from clickPlayer import clickPlayer

# klogger = keyLogger()
# #klogger.run()

cPlayer = clickPlayer()
#cPlayer.addEvent([5.5,[100,100]])
cPlayer.readCoordinateList()
cPlayer.play()
#cPlayer.processNextEvent(3,100,100)

#logger = clickLogger()
#logger.run()
