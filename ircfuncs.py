import socket
import sys

server = "blacklotus.ca.us.quakenet.org"     #irc server
channel = "#tf2.pug.na"     #channel
botname = "aBot"    #bot nickname
PORT = 6667     #irc port, default 6667

ircsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ircsock.connect((server, PORT)) #connect to server
ircsock.send("USER "+botname+" "+botname+" "+botname+" :Authentication successful\n")   #authenticate
ircsock.send("NICK "+botname+"\n")  #set botname as nick

def ping(message):     #ping irc server
    ircsock.send("PONG :"+message+"\n")
    print("Sent - PONG :"+message+"\n")
def sendmsg(target, msg):     # send message to channel
    ircsock.send("PRIVMSG "+target+" :"+msg+"\n")
    print("PRIVMSG "+target+" :"+msg+"\n")
def joinchan(chan):     #join specific channel
    ircsock.send("JOIN "+chan+"\n")
def qq():   #quit connection to server
    ircsock.close()
    sys.exit('KILLBOT')

    
