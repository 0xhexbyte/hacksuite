import socket
import _thread
import time
class Core(object):
    ipurl=0
    mode=1024
    menu1=False
    f=None
    net_speed="LAN"
    menu2=False
    def GetData(self, url):
        self.url = url
        try:
            self.ipurl = socket.gethostbyname(self.url)
        except Exception as e:
            print ("Invalid URL or IP")
            exit(0)
        Core.ipurl=self.ipurl
        print (80*"-")
        print (32*" ","Hack Suite - Port Scan")
        print (80*"-")
        while Core.menu1 is not True:
            choice = input("\n1 - Simple \n2 - Extended\n")
            if choice == "1":
                Core.mode=1024
                menu=True
                break
            elif choice == "2":
                Core.mode=64000
                menu = True
                break
            else:
                print("Incorrect answer, choose 1 or 2")
        while Core.menu2 is not True:
            choice = input("\n1 - LAN \n2 - Global Network\n")
            if choice == "1":
                Core.net_speed=0.05
                menu2=True
                break
            elif choice == "2":
                Core.net_speed=0.3
                menu2 = True
                break
            else:
                print("Incorrect answer, choose 1 or 2")

    def Start_Scan(self, port_start, port_end):
        Core.f = open(Core.ipurl, "a")
        try:
            for x in range(port_start,port_end):
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                res = sock.connect_ex((Core.ipurl,x))
                if res is 0:
                    tmp="Port",x,"is open", socket.getservbyport(x)
                    tmp1=str(tmp[0])+" "+str(tmp[1])+" "+str(tmp[2])+" "+str(tmp[3])
                    print(tmp1)
                    Core.f.write(str(tmp)+"\n")
            Core.f.close()
        except Exception as e:
            print (e)
try:
    scan = Core()
    scan.GetData(input("Enter the IP address or the URL:\n"))
    print("Range:",Core.mode,"\n Target:",Core.ipurl,"\n Scanning speed:",Core.net_speed)
    print("Please wait...")
    for count in range(0,Core.mode):
        #print (Core.mode)
        time.sleep(Core.net_speed)
        _thread.start_new_thread(scan.Start_Scan, (count,count+1))
        if count > Core.mode:
            exit(0)
except Exception as e:
    print (e)

