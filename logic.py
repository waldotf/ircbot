scoutlist = []
mediclist = []
demolist = []
pocketlist = []
roamerlist = []
captainlist = []
playerlist = []
playernames = []
adminlist = ['Waldo_']

class Player:
    def __init__(self, name):
        self.name = name
        self.scout = 0
        self.roamer = 0
        self.demo = 0
        self.pocket = 0
        self.medic = 0
        self.captain = 0
    def __str__(self):
        return self.name
    def __repr__(self):
        return self.name



def startgame():
    sendmsg(channel,'game started')
def checkfull():        #check if enough players are added up to play
    return 0


def findplayer(name):
    curplayer = 0
    if len(playerlist)>0:
        for player in playerlist:
            if player.name == name:
                curplayer = player
                break
    if curplayer == 0:
        curplayer = Player(name)
    return curplayer


def add_scout(player):
    if player not in scoutlist:
        scoutlist.append(player)
        player.scout = 1
    if player not in playerlist:
        playerlist.append(player)
def add_roamer(player):
    if player not in roamerlist:
        roamerlist.append(player)
        player.roamer = 1
    if player not in playerlist:
        playerlist.append(player)
def add_pocket(player):
    if player not in pocketlist:
        pocketlist.append(player)
        player.pocket = 1
    if player not in playerlist:
        playerlist.append(player)
def add_medic(player):
    if player not in mediclist:
        mediclist.append(player)
        player.medic = 1
    if player not in playerlist:
        playerlist.append(player)
def add_demo(player):
    if player not in demolist:
        demolist.append(player)
        player.demo = 1
    if player not in playerlist:
        playerlist.append(player)
def add_captain(player):
    if player not in captainlist:
        captainlist.append(player)
        player.captain = 1
    if player not in playerlist:
        playerlist.append(player)

def remove(player):
    if player in scoutlist:
        scoutlist.remove(player)
        player.scout = 0
    if player in roamerlist:
        roamerlist.remove(player)
        player.roamer = 0
    if player in pocketlist:
        pocketlist.remove(player)
        player.pocket = 0
    if player in mediclist:
        mediclist.remove(player)
        player.medic = 0
    if player in demolist:
        demolist.remove(player)
        player.demo = 0
    if player in captainlist:
        captainlist.remove(player)
        player.captain = 0
    if player in playerlist:
        playerlist.remove(player)
