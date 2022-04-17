import threading


def f1():
    while True:
        print("f1")

def f2():
    while True:
        print("f2")
t1 = threading.Thread(target=f1)
t1.start()

t2 = threading.Thread(target=f2)
t2.start()