#So basically there's this one Discord bot that spawns collectible countryballs (if you don't know what that is it's like countries in the form of collectible balls, kinda like Pokemon)...
#and I made a bot to farm them (sorry to any of my friends reading this)
#The bot changed the art of the balls so it kinda fucked my whole system, and I'm not going to do the work to make an image recognition bot because 1. I'm lazy, and 2. I don't know how to do any of that
#this bot also (technically) spans over 250 files, but there's only a few that execute code

#sorry for talking so much, here it is:


#File storing the PNG's of all the country balls (ballsStorage.py)


import os

os.chdir(r'C:\Users\#####\Python\BALLS')

group1 = {"ball1.png": "botswana", "ball2.png": "macau", "ball11.png" : "jamaica", "ball16.png" : "namibia", "ball41.png" : "numidia", "ball42.png" : "african union", "ball61.png" : "south africa", "ball62.png" : "micronesia", "ball63.png" : "gambia", "ball182.png" : "bahrain", "ball203.png" : "togo", "ball211.png" : "japanese empire"}
group2 = {"ball3.png": "macedonia","ball4.png": "cambodia", "ball12.png" : "djibouti", "ball17.png" : "mali", "ball43.png" : "australia", "ball44.png" : "italy", "ball66.png" : "cameroon", "ball67.png" : "xiongnu", "ball68.png" : "croatia", "ball174.png" : "philippines", "ball193.png" : "germania", "ball210.png" : "belgium"}
group3 = {"ball46.png" : "korea", "ball70.png" : "mauritania", "ball71.png" : "khiva", "ball72.png" : "mozambique", "ball73.png" : "algeria", "ball106.png" : "russian soviet federative socialist republic", "ball107.png" : " byelorussian soviet socialist republic", "ball183.png" : "tunisia", "ball208.png" : "malaysia", "ball225.png" : "franks"}
group4 = {"ball7.png": "morocco", "ball8.png": "free city of danzig", "ball14.png" : "tajikistan", "ball19.png" : "norway", "ball47.png" : "albania", "ball48.png" : "moldova", "ball74.png" : "georgia", "ball75.png" : "chile", "ball76.png" : "zhou", "ball178.png" : "fiji", "ball195.png" : "andorra", "ball209.png" : "carthage"}
group5 = {"ball50.png" : "polish underground state", "ball78.png" : "equador", "ball79.png" : "somalia", "ball80.png" : "mongolia", "ball81.png" : "nato", "ball110.png" : "bangladesh", "ball111.png" : "french indochina", "ball130.png" : "azerbaijan", "ball181.png" : "league of nations", "ball204.png" : "united nations", "ball226.png" : "hong kong"}
group6 = {"ball82.png" : "slovenia", "ball83.png" : "new zealand", "ball84.png" : "chad", "ball85.png" : "ukraine", "ball112.png" : "montenegro", "ball113.png" : "uzbekistan", "ball132.png" : "bay company","ball135.png" : "france", "ball172.png" : "ghana", "ball184.png" : "tunisia", "ball202.png" : "samoa", "ball212.png" : "congo free state"}
group7 = {"ball25.png" : "hungary", "ball26.png" : "northern ireland", "ball27.png" : "singapore", "ball28.png" : "netherlands", "ball53.png" : "paris commune", "ball54.png" : "greece", "ball86.png" : "laos", "ball87.png" : "switzerland", "ball88.png" : "columbia", "ball192.png" : "scotland", "ball206.png" : "myanmar", "ball228.png" : "belize"}
group8 = {"ball29.png" : "luxembourg", "ball30.png" : "quebec", "ball31.png" : "liechtenstein", "ball32.png" : "reichtangle", "ball55.png" : "bolivia", "ball56.png" : "germany", "ball90.png" : "papua new guinea", "ball91.png" : "manchukuo", "ball173.png" : "siam", "ball186.png" : "eswatini", "ball205.png" : "costa rica"}
group9 = {"ball33.png" : "estonia", "ball34.png" : "serbia", "ball35.png" : "dr congo", "ball36.png" : "tibet", "ball57.png" : "cape verde", "ball58.png" : "liberia", "ball94.png" : "german empire", "ball95.png" : "taiwan", "ball127.png" : "ethiopian empire", "ball185.png" : "ceylon", "ball201.png" : "kyrgyzstan", "ball213.png" : "guyana"}
group10 = {"ball60.png" : "czechia", "ball98.png" : "nepal", "ball99.png" : "byzantium", "ball100.png" : "north korea", "ball101.png" : "cuba", "ball120.png" : "latvia", "ball121.png" : "ancient athens", "ball151.png" : "monaco", "ball166.png" : "mexico", "ball177.png" : "guatemala", "ball198.png" : "south sudan", "ball224.png" : "mauritania"}
group11 = {"ball171.png" : "ancient sparta", "ball24.png" : "honduras", "ball9.png": "paraguay", "ball10.png": "hejaz", "ball15.png" : "kiribati", "ball20.png" : "sri lanka", "ball49.png" : "ethiopia", "ball133.png" : "saudi arabia", "ball150.png" : "vichy france", "ball191.png" : "san marino", "ball207.png" : "qatar", "ball227.png" : "palau"}
group12 = {"ball37.png" : "bahams", "ball38.png" : "saint lucia", "ball39.png" : "ireland", "ball40.png" : "warsaw pact", "ball59.png" : "kosovo", "ball138.png" : "armenia", "ball139.png" : "bulgaria", "ball156.png" : "turkey", "ball157.png" : "lebanon", "ball180.png" : "wales", "ball197.png" : "iraq", "ball220.png" : "tonga", "ball231.png" : "argentina"}
group13 = {"ball21.png" : "tuvalu", "ball22.png" : "south vietnam", "ball23.png" : "sudan", "ball51.png" : "babylon", "ball52.png" : "palestine", "ball5.png": "burundi", "ball6.png": "ukrainian soviet socialist republic", "ball13.png" : "denmark", "ball18.png" : "panama", "ball194.png" : "germania", "ball219.png" : "india", "ball229.png" : "afghanistan"}
group14 = {"ball129.png" : "madagascar", "ball146.png" : "soviet union", "ball147.png" : "romania", "ball163.png" : "oman", "ball170.png" : "union of south africa", "ball122.png" : "nicaragua", "ball123.png" : "western sahara", "ball142.png" : "burkina faso", "ball187.png" : "sweden", "ball200.png" : "vanuatu", "ball221.png" : "kuwait"}
group15 = {"ball103.png" : "iceland", "ball102.png" : "uae", "ball64.png" : "cyprus", "ball65.png" : "gabon", "ball105.png" : "portugal", "ball124.png" : "argentina", "ball125.png" : "libya", "ball160.png" : "cote d'lvoire", "ball145.png" : "belarus", "ball176.png" : "tannu tuva", "ball199.png" : "timor-leste", "ball223.png" : "dominican republic"}
group16 = {"ball144.png" : "austria", "ball136.png" : "west germany", "ball69.png" : "finland", "ball104.png" : "north vietnam", "ball126.png" : "napoleonic france", "ball109.png" : "iran", "ball128.png" : "south yemen", "ball134.png" : "zimbabwe", "ball175.png" : "niger", "ball196.png" : "yugoslavia", "ball218.png" : "bhutan", "ball230.png" : "malta"}
group17 = {"ball140.png" : "republican spain", "ball141.png" : "vietnam", "ball158.png" : "uganda", "ball159.png" : "venezuela", "ball165.png" : "qing","ball137.png" : "poland", "ball45.png" : "free france", "ball155.png" : "kazakhstan", "ball168.png" : "syria", "ball190.png" : "bosnia and herzegovina", "ball217.png" : "prussia", "ball234.png" : "zhou"}
group18 = {"ball143.png" : "turkmenistan", "ball161.png" : "confederate states", "ball164.png" : "zambia", "ball131.png" : "el savador", "ball148.png" : "sierra leone", "ball149.png" : "kingdom of italy", "ball77.png" : "seychelles", "ball108.png" : "thailand", "ball189.png" : "congo", "ball214.png" : "kenya", "ball222.png" : "azerbaijan"}
group19 = {"ball162.png" : "antarctica", "ball169.png" : "lesotho", "ball154.png" : "eritrea", "ball152.png" : "Czechoslovakia", "ball153.png" : "east germany", "ball167.png" : "central african republic", "ball114.png" : "haiti", "ball115.png" : "tanzania", "ball179.png" : "arab league", "ball216.png" : "mayan empire", "ball232.png" : "seychelles"}
group20 = {"ball92.png" : "nigeria", "ball93.png" : "british raj", "ball116.png" : "ancient egypt", "ball117.png" : "iraq", "ball96.png" : "suriname", "ball97.png" : "uruguay", "ball118.png" : "yemen", "ball119.png" : "united states", "ball89.png" : "senegal", "ball188.png" : "tunisia", "ball215.png" : "Achaemenid empire", "ball233.png" : "belize"}

#Comparing the unknown ball to the ones in the storage (findCountry.py)

import os, threading, ballsStorage as storage
import time, pyperclip
os.chdir(r'C:\Users\#####\Python\BALLS')
def search1():
    for k, v in storage.group1.items():
        if open(k, "rb").read() == open("ball.png", "rb").read():
            pyperclip.copy(v)
            print(v)

def search2():
    for k, v in storage.group2.items():
        if open(k, "rb").read() == open("ball.png", "rb").read():
            pyperclip.copy(v)
            print(v)

def search3():
    for k, v in storage.group3.items():
        if open(k, "rb").read() == open("ball.png", "rb").read():
            pyperclip.copy(v)
            print(v)

def search4():
    for k, v in storage.group4.items():
        if open(k, "rb").read() == open("ball.png", "rb").read():
            pyperclip.copy(v)
            print(v)

def search5():
    for k, v in storage.group5.items():
        if open(k, "rb").read() == open("ball.png", "rb").read():
            pyperclip.copy(v)
            print(v)

def search6():
    for k, v in storage.group6.items():
        if open(k, "rb").read() == open("ball.png", "rb").read():
            pyperclip.copy(v)
            print(v)

def search7():
    for k, v in storage.group7.items():
        if open(k, "rb").read() == open("ball.png", "rb").read():
            pyperclip.copy(v)
            print(v)

def search8():
    for k, v in storage.group8.items():
        if open(k, "rb").read() == open("ball.png", "rb").read():
            pyperclip.copy(v)
            print(v)

def search9():
    for k, v in storage.group9.items():
        if open(k, "rb").read() == open("ball.png", "rb").read():
            pyperclip.copy(v)
            print(v)

def search10():
    for k, v in storage.group10.items():
        if open(k, "rb").read() == open("ball.png", "rb").read():
            pyperclip.copy(v)
            print(v)

def search11():
    for k, v in storage.group11.items():
        if open(k, "rb").read() == open("ball.png", "rb").read():
            pyperclip.copy(v)
            print(v)

def search12():
    for k, v in storage.group12.items():
        if open(k, "rb").read() == open("ball.png", "rb").read():
            pyperclip.copy(v)
            print(v)

def search13():
    for k, v in storage.group13.items():
        if open(k, "rb").read() == open("ball.png", "rb").read():
            pyperclip.copy(v)
            print(v)

def search14():
    for k, v in storage.group14.items():
        if open(k, "rb").read() == open("ball.png", "rb").read():
            pyperclip.copy(v)
            print(v)

def search15():
    for k, v in storage.group15.items():
        if open(k, "rb").read() == open("ball.png", "rb").read():
            pyperclip.copy(v)
            print(v)

def search16():
    for k, v in storage.group16.items():
        if open(k, "rb").read() == open("ball.png", "rb").read():
            pyperclip.copy(v)
            print(v)

def search17():
    for k, v in storage.group17.items():
        if open(k, "rb").read() == open("ball.png", "rb").read():
            pyperclip.copy(v)
            print(v)


def search18():
    for k, v in storage.group18.items():
        if open(k, "rb").read() == open("ball.png", "rb").read():
            pyperclip.copy(v)
            print(v)

def search19():
    for k, v in storage.group19.items():
        if open(k, "rb").read() == open("ball.png", "rb").read():
            pyperclip.copy(v)
            print(v)


def search20():
    for k, v in storage.group20.items():
        if open(k, "rb").read() == open("ball.png", "rb").read():
            pyperclip.copy(v)
            print(v)

def startBalls():

    a = threading.Thread(target=search1, args=())
    b = threading.Thread(target=search2, args=())
    c = threading.Thread(target=search3, args=())
    d = threading.Thread(target=search4, args=())
    e = threading.Thread(target=search5, args=())
    f = threading.Thread(target=search6, args=())
    g = threading.Thread(target=search7, args=())
    h = threading.Thread(target=search8, args=())
    i = threading.Thread(target=search9, args=())
    j = threading.Thread(target=search10, args=())
    k = threading.Thread(target=search11, args=())
    l = threading.Thread(target=search12, args=())
    m = threading.Thread(target=search13, args=())
    n = threading.Thread(target=search14, args=())
    o = threading.Thread(target=search15, args=())
    p = threading.Thread(target=search16, args=())
    q = threading.Thread(target=search17, args=())
    r = threading.Thread(target=search18, args=())
    s = threading.Thread(target=search19, args=())
    t = threading.Thread(target=search20, args=())

    a.start()
    b.start()
    c.start()
    d.start()
    e.start()
    f.start()
    g.start()
    h.start()
    i.start()
    j.start()
    k.start()
    l.start()
    m.start()
    n.start()
    o.start()
    p.start()
    q.start()
    r.start()
    s.start()
    t.start()

#main file that just displays what's going on in the other file (BallCatcher.py)

from PIL import ImageGrab, ImageOps
import cv2, os, win32api, win32con, time, pyautogui, keyboard
from findCountry import *

def click(x, y):
        pyautogui.moveTo(x, y)
        time.sleep(0.1)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0,0)
        time.sleep(0.1)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0,0)
def catchBall():
    ballsDir = r'C:\Users\#####\Python\BALLS'
    image = ImageGrab.grab(bbox=(448, 275, 978, 924))
    os.chdir(ballsDir)
    image.save("TestImage.png")
    whole = cv2.imread("TestImage.png", cv2.IMREAD_UNCHANGED)
    text = cv2.imread("Ball_Text.png", cv2.IMREAD_UNCHANGED)
    pfp = cv2.imread("pfp.png", cv2.IMREAD_UNCHANGED)
    #Finding when a ball spawns by looking at the text
    method = cv2.TM_CCOEFF_NORMED
    findText = cv2.matchTemplate(whole, text, method)
    wT = text.shape[1]
    hT = text.shape[0]
    #wait mechanism
    ballSpawned = False
    while ballSpawned == False:
        for y in range(800, 950, 20):
             print(pyautogui.pixel(597, y)[0])
             if pyautogui.pixel(597, y)[0] == 88 or pyautogui.pixel(597, y)[0] == 69:
                ballSpawned = True
                break
    #break out of the wait mechanism program detected a ball has spawned
    click(-660, 287)
    minValTEXT, maxValTEXT, minLocTEXT, maxLocTEXT = cv2.minMaxLoc(findText)
    print(maxLocTEXT[0]+550, maxLocTEXT[1] + 350)
    click(maxLocTEXT[0]+550, maxLocTEXT[1] + 350)
    time.sleep(0.5)
    ball = ImageGrab.grab(bbox=(1050, 490, 1300, 875))
    ball = ImageOps.grayscale(ball)
    ball.save("ball.png")
    startBalls()
catchBall()


#File used for getting the PNG of the ball and putting it in the storage (getImg.py)

from PIL import ImageGrab, ImageOps
import cv2, os, win32api, win32con, pyautogui, time

time.sleep(2)
def click(x, y):
        pyautogui.moveTo(x, y)
        time.sleep(0.1)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0,0)
        time.sleep(0.1)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0,0)
ballsDir = r'C:\Users\#####\Python\BALLS'
image = ImageGrab.grab(bbox=(448, 275, 978, 924))
os.chdir(ballsDir)
image.save("TestImage.png")
whole = cv2.imread("TestImage.png", cv2.IMREAD_UNCHANGED)
text = cv2.imread("Ball_Text.png", cv2.IMREAD_UNCHANGED)
#Finding when a ball spawns by looking at the text
method = cv2.TM_CCOEFF_NORMED
findText = cv2.matchTemplate(whole, text, method)
minValTEXT, maxValTEXT, minLocTEXT, maxLocTEXT = cv2.minMaxLoc(findText)
w = text.shape[1]
h = text.shape[0]
with open("count.txt", "r") as f:
    value = ord(f.read())
click(maxLocTEXT[0]+550, maxLocTEXT[1] + 450)
time.sleep(1)
ball = ImageGrab.grab(bbox=(1050, 490, 1300, 875))
ball = ImageOps.grayscale(ball)
ball.save(f"ball{value-32}.png")
cv2.rectangle(whole, maxLocTEXT, (maxLocTEXT[0] + w, maxLocTEXT[1] + h), (0, 255, 0), 1)

#end of program
cv2.waitKey(0)
cv2.destroyAllWindows()
os.remove("TestImage.png")

value += 1

with open("count.txt", "w") as file:
    file.write(chr(value))





