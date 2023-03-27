import threading
import socket

srvIP2 = input("Podaj serwer IP: ")
srvPort2 = int(input("Podaj port serwera: "))
cntPort2 = int(input("Podaj port klienta:"))
srvAddrPort2 = (srvIP2, srvPort2)
buff = 1024

UDPcnt = socket.socket(family=socket.AF_INET, type = socket.SOCK_DGRAM)
UDPcnt.bind(("127.0.0.1", cntPort2))
UDPcnt.sendto("Połączono.".encode(), srvAddrPort2)

def rcv():
    while True:
        try:
            message, _ = UDPcnt.recvfrom(buff)
            print(message.decode())
        except:
            pass
thread = threading.Thread(target=rcv)
thread.start()

while True:
    message = input("")
    if message == "$quit":
        exit()
    else:
        UDPcnt.sendto(message.encode(), srvAddrPort2)