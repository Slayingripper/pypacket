import psutil
import aprslib
cpu = psutil.cpu_percent()
ram = psutil.virtual_memory().percent
def callback():
    #  print(packet)
    # # a valid passcode for the callsign is required in order to send
    AIS = aprslib.IS("5B4ANU", passwd="15540", host = "asia.aprs2.net" ,port=14580)

    AIS.connect()
    # # send a single status message
    AIS.sendall("5B4ANU>APRS,TCPIP*:> Cpu Usage:"+str(cpu)+"Ram usage:"+str(ram)+"")
    print(cpu,ram)
if __name__ == '__main__':
    callback()
    
    