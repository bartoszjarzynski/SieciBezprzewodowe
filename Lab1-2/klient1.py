import threading
import socket

srvIP = input("Podaj serwer IP: ")
srvPort = int(input("Podaj port serwera: "))
cntPort = int(input("Podaj port klienta:"))
srvAddrPort = (srvIP, srvPort)
buff = 1024

UDPcnt = socket.socket(family=socket.AF_INET, type = socket.SOCK_DGRAM)
UDPcnt.bind(("127.0.0.1", cntPort))
UDPcnt.sendto("Połączono.".encode(), srvAddrPort)

def rcv():
    while True:
        try:
            wd, _ = UDPcnt.recvfrom(buff)
            print(wd.decode())
        except:
            pass
thread = threading.Thread(target=rcv)
thread.start()

while True:
    wd = input("")
    if wd == "$quit":
        exit()
    else:
        UDPcnt.sendto(wd.encode(), srvAddrPort)