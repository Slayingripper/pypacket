import sysusage
from solarpanels import solar
from wakemeup import wakemeup
from sysusage import callback
from callsign import getinfo
def packetexecute(packetstring):
    
    if '#1010#' in packetstring:
        print("Packet found")
        callback()
    elif 'Nicosia' in packetstring:
        print("Packet found")
    elif '#1337#' in packetstring:
        wakemeup()
    elif '#SL01#'in packetstring:
        solar()   
    elif '#73#' in packetstring:
      #  packetstring = packetstring.split('!')
        newpacket = packetstring[packetstring.find("(")+1 : packetstring.find(")")]
        getinfo(newpacket)
            
    

    
if __name__ == "__main__":
    packetexecute("")
