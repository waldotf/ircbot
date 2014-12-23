from logic import *
from ircfuncs import *
#Helper functions----------------------------------------------
def namelist(playerlist):   #returns list of names of Player objects in given list
    names = []
    for player in playerlist:
        names.append(player.name)
    return names



#Commands------------------------------------------------------
def parsecommand(curplayer,command): #react to !messages
    command = command.strip('\r\n')
    print ("---  "+command+"  ---")
    if command.split(' ')[0]=='add':
        com_add(curplayer,command)
    elif command.split(' ')[0]=='remove': 
        com_remove(curplayer)
        
    elif command.split(' ')[0]=='list':
        com_list()

    elif command.split(' ')[0] == 'killbot': 
        qq()
        
    elif command.split(' ')[0] == 'players':
        com_players()
            
    elif command.split(' ')[0] =='myclasses':
        com_myclasses(curplayer)
        
def com_add(curplayer,command):       #add command
    for tfclass in command.split(' '):
        if tfclass=='scout':
            add_scout(curplayer)
        elif tfclass=='roamer':
            add_roamer(curplayer)
        elif tfclass=='pocket':
            add_pocket(curplayer)
        elif tfclass=='demo':
            add_demo(curplayer)
        elif tfclass=='medic':
            add_medic(curplayer)
        elif tfclass=='captain':
            add_captain(curplayer)
        elif tfclass=='all':
            add_scout(curplayer)
            add_roamer(curplayer)
            add_pocket(curplayer)
            add_demo(curplayer)
            add_medic(curplayer)
        elif tfclass=='combat':
            add_scout(curplayer)
            add_roamer(curplayer)
            add_pocket(curplayer)
            add_demo(curplayer)
    sendmsg(channel,(str(len(playerlist))+' users added: '+str(playerlist)))
        
def com_remove(curplayer):
    remove(curplayer)
    sendmsg(channel,str(len(playerlist))+' users added: '+str(playerlist))
    
def com_list():   #list all classes and who is added up
    sendmsg(channel, ("SCOUT = "+str(namelist(scoutlist))))
    sendmsg(channel, ("ROAMER = "+str(namelist(roamerlist))))
    sendmsg(channel, ("POCKET = "+str(namelist(pocketlist))))
    sendmsg(channel, ("DEMO = "+str(namelist(demolist))))
    sendmsg(channel, ("MEDIC = "+str(namelist(mediclist))))

def com_players():    #returns all known players
    tlist = []
    sendmsg(channel,str(len(playerlist))+' users added: '+str(playerlist))

def com_myclasses(curplayer):   #show current classes
    classlist = []
    if curplayer.scout ==1:
        classlist.append('Scout')
    if curplayer.roamer ==1:
        classlist.append('Roamer')
    if curplayer.pocket ==1:
        classlist.append('Pocket')
    if curplayer.demo ==1:
        classlist.append('Demo')
    if curplayer.medic ==1:
        classlist.append('Medic')
    if curplayer.captain ==1:
        classlist.append('Captain')
    
    sendmsg(channel,str(classlist))
