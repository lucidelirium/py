#Example: python3 script.py 192.168.1 1 10
import sys
import os

network=str(sys.argv[1])
start=int(sys.argv[2])
stop=int(sys.argv[3])
stop+=1

for x in range(start, stop, 1):
    lastOctet=str(x)
    ip=(str(network+"."+lastOctet))
    response = os.system("ping -c 1 -W 1 " + ip + "> /dev/null")
    if response == 0:
      print (str(ip))
