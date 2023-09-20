from prac.asc import asc
from prac.des import des
import threading



t1 = threading.Thread(target= asc)
t2 = threading.Thread(target=des)


t2.start()
t1.start()