from playsound import playsound
import pyautogui as pag
import time
from threading import Thread

title_offset = (1440, 423)
pot_offset = (1357, 740)
met_offset = (1509, 737)
pwr_offset = (1659, 707)

gray = (128, 128, 128)

thread_running = True

def alrm():
    playsound("alarm.wav")

def potf(title):
    pot = [0, 0]
    pot[0] = title[0]-title_offset[0]+pot_offset[0]
    pot[1] = title[1]-title_offset[1]+pot_offset[1]
    while thread_running:
        if pag.pixel(pot[0], pot[1]) == gray:
            t = Thread(target = alrm)
            t.start()
            time.sleep(15)
        time.sleep(0.5)

def metf(title):
    met = [0, 0]
    met[0] = title[0]-title_offset[0]+met_offset[0]
    met[1] = title[1]-title_offset[1]+met_offset[1]
    while thread_running:
        if pag.pixel(met[0], met[1]) == gray:
            t = Thread(target = alrm)
            t.start()
            time.sleep(15)
        time.sleep(0.5)

def pwrf(title):
    pwr = [0, 0]
    pwr[0] = title[0]-title_offset[0]+pwr_offset[0]
    pwr[1] = title[1]-title_offset[1]+pwr_offset[1]
    while thread_running:
        if pag.pixel(pwr[0], pwr[1]) == gray:
            t = Thread(target = alrm)
            t.start()
            time.sleep(15)
        time.sleep(0.5)

def exitf():
    a = input("press enter again to exit")


if __name__=='__main__':
    thread_running = True
    title = pag.locateCenterOnScreen("title.png")
    if title is None:
        print("Looking for title...")
        while title is None:
            time.sleep(0.5)
            title = pag.locateCenterOnScreen("title.png")
    _ = input("Title found, press enter to run")
    

    t0 = Thread(target = exitf)
    #t1 = Thread(target = potf, args=(title,))
    t2 = Thread(target = metf, args=(title,))
    t3 = Thread(target = pwrf, args=(title,))

    t0.start()
    #t1.start()
    t2.start()
    t3.start()

    t0.join()
    thread_running = False
    print("exit")
    
