import threading
import time
from ism import * 
from familiya import *
from sharifi import *
from jinsi import *
 

t1 = threading.Thread(target=ism)
t2 = threading.Thread(target=familiya)
t3 = threading.Thread(target=sharifi)
t4 = threading.Thread(target=jinsi)


t1.start()
t2.start()
t3.start()
t4.start()
