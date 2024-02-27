from playsound import playsound
import pyautogui as pag
import time
from PIL import Image
from PIL import ImageGrab
from PIL import ImageChops
from PIL import ImageStat

print(pag.locateCenterOnScreen("title.png"))

input= input("wait.")
a, b= pag.position()
print(a, b)
print(pag.pixel(a, b))
