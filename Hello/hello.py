import threading
from time import ctime,sleep

def music():
    for i in range(2):
        print ("I was listening to music.") #%ctime()
        sleep(1)

def move():
    for i in range(2):
        print ("I was at the move!") #%ctime()
        sleep(1)

if __name__=='__main__':
    music()
    move()
    print ("all over %s") #%ctime()
