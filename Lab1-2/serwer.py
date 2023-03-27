import threading
import socket
import queue, string, random

hostLokalny = "127.0.0.1"
portLokalny = 5555
buff = 1024

UDPSrv = socket.socket(family=socket.AF_INET, type = socket.SOCK_DGRAM)
UDPSrv.bind((hostLokalny, portLokalny))

wdmsc = queue.Queue()
klienci = []

cntIP_1 = input("Podaj IP pierwszego klienta:")
cntPort_1 = int(input("Podaj port pierwszego klienta:"))
cntIP_2 = input("Podaj IP drugiego klienta:")
cntPort_2 = int(input("Podaj port drugiego klienta:"))

czZakl = input("Podaj częstotliwość zakłócenia - 0 lub 1: ")
print("Serwer UDP nasłuchuje.")

def dsrptr(wdmsc, czZakl):
    err = ""
    czZakl = float(czZakl)
    chr = string.ascii_letters + string.digits + string.punctuation
    for letter in err:
        rndnum = random.uniform(0,1)
        if czZakl >= rndnum:
            letter = random.choice(chr)
            err += letter
        else: 
            err += letter
    return err

def rcv():
    while True:
        try:
            wd, addr = UDPSrv.recvfrom(buff)
            if (addr[0] == cntIP_1 and addr[1] == cntPort_1) or (addr[0] == cntIP_2 and addr[1] == cntPort_2):
                wdmsc.put((wd,addr))
            else: pass
        except: pass    

def strumien():
    while True:
        while not wdmsc.empty():
            wd, addr = wdmsc.get()
            print(addr)
            
            wd = wd.decode()
            print("Pierwotny klient " + addr[0] + ": " + wd)
            
            wd = dsrptr(wd, czZakl)
            print("Klient " + addr[0] + ": " + wd)
            wd = wd.encode()
            
            if addr not in klienci:
                klienci.append(addr)
                for klient in klienci:
                    UDPSrv.sendto((addr[0] + " połączony.").encode(), klient)
            for klient in klienci:
                UDPSrv.sendto(wd, klient)

thread1 = threading.Thread(target=rcv)
thread2 = threading.Thread(target=strumien)

thread1.start()
thread2.start()            