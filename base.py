import socket
import time
from ircfuncs import *
from commands import *
from logic import *
        
while 1: #loop
    ircmsg = ircsock.recv(2048) #receive standard message from server
    print('@@'+ircmsg)   #live feed from server

    if ircmsg.find("PING :") != -1: #if server pings, pong
        ping(str(ircmsg.split(':')[-1]))
    if ircmsg.split(':').count("Highest connection count") ==1: #On first entry
        joinchan(channel)
    if ircmsg.split(':')[-1][0] =='!':  #grab messages that start with control character
        parsecommand(findplayer(ircmsg.split(':')[-2].split('!')[0]),ircmsg.split(':')[-1][1:])
        #               ^get player with given name and pass with command
    playernames = []
    for player in playerlist:
        playernames.append(player.name)

    playerlist = list(set(playerlist))
    if checkfull():
        startgame()


    time.sleep(1)   #prevent melting
