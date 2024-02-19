import subprocess
import time
import threading

def t_45():
    print("t_45")
    subprocess.call(["python","T45\Automation_45.py"])


def t_46():
    print("t_46")
    subprocess.call(["python","T46\Automation_46.py"])

t1 = threading.Thread(target = t_45)
t2 = threading.Thread(target = t_46)

t1.start()

time.sleep(60)
t2.start()