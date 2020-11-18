import requests 
import json
import aprslib
def getinfo(callsign):
  
    
    # Making a GET request 
    r = requests.get("https://www.hamqth.com/dxcc_json.php?callsign="+callsign+"") 
    #r = requests.get("https://www.hamqth.com/dxcc_json.php?callsign=5B4ANU") 
    
    jsonResponse = r.json()
   
    # check status code for response received 
    # success code - 200 
    print(r) 
    
    # print content of request 
    print(r.content) 
    details = jsonResponse['details']
    print (jsonResponse['details'])
    timezone = jsonResponse['utc']
    print(jsonResponse['utc'])
    
    AIS = aprslib.IS("5B4ANU", passwd="15540", host = "asia.aprs2.net" ,port=14580)

    AIS.connect()
    # # send a single status message
    AIS.sendall("5B4ANU>APRS,TCPIP*:> Callsign Location : "+str(details)+" Timezone: "+str(timezone)+"")
if __name__ == '__main__':
    getinfo("")
    