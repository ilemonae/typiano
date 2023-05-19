# typiano - may 2023

# module import > 
import turtle
import random
import time
# module import <

# settings >


turtle.textinput("intro", "controls are 'd', 'f', 'j', and 'k' keys. got it?")

endIsNear = 0
subtract = None
while subtract == None:
  subtract = turtle.numinput("settings", "select difficulty (1-15)", minval = 1, maxval = 15)
subtract = int(subtract)

keySpawnRate = 160 - 10*subtract

if keySpawnRate == 10:
  keySpawnRate = 15



discoMode = None
while discoMode == None:
  discoMode = turtle.numinput("settings", "disco mode? 1: yes; 0: no")
discoMode = int(discoMode)




timeGoal = None
while timeGoal == None:
  timeGoal = turtle.numinput("settings", "session time? 1: 2 minute session; 0: 5 minute session" )

if timeGoal == 0:
  timeGoal = 5*60*100
else:
  timeGoal = 2*60*100




tuTime = turtle.Turtle()
tuTime.penup()
tuTime.hideturtle()
tuTime.speed(0)
tuTime.goto(200,100)
tuTime.write("time:", font = ("Courier New", 20, "normal"), align = "center")
tuTime.goto(200,75)
timE = 0
tuTime.write(   str(int((timeGoal*100 - timE*100) / 10000))    , font = ("Courier New", 20, "normal" ), align = "center" )


threes = 0
fives = 0
ones = 0
misus = 0
keysSpawned = 0


# settings <

# colors
backGroundColor = "darkgrey"
middleKeyColor = "black"
outsideKeyColor = "dimgrey"
borderColor = "black"
lightColor = "white"
if discoMode == 1:
  backGroundColor = "black"
  borderColor = "white"
  lightColor = "white"
# colors
# screen setup >

win = turtle.Screen()
win.colormode(255)
win.title("typiano")
win.bgcolor(backGroundColor)
win.setup(width = 700, height = 700)
win.tracer(0)









tu = turtle.Turtle()
tu.hideturtle()
tu.penup()
tu.speed(0)
linTu = turtle.Turtle()
linTu.hideturtle()
linTu.penup()
linTu.speed(0)
setupTu = turtle.Turtle()
tuType = turtle.Turtle()
tuType.speed(0)
tuType.penup()
tuType.hideturtle()
tuKeyScore = turtle.Turtle()
tuKeyScore.penup()
tuKeyScore.speed(0)
tuKeyScore.hideturtle()
tuRunTotal = turtle.Turtle()
tuRunTotal.penup()
tuRunTotal.speed(0)
tuRunTotal.hideturtle()
tuRunTotal.color("white")
# drawing frame on the screen >
setupTu.color(borderColor)
setupTu.penup()
setupTu.speed(0)
setupTu.hideturtle()
setupTu.goto(-200,-350)
setupTu.pendown()
setupTu.goto(-200,350)
setupTu.penup()
setupTu.goto(49,-350)
setupTu.pendown()
setupTu.goto(49,350)
setupTu.penup()
setupTu.goto(-200,-250)
setupTu.pendown()
setupTu.goto(49,-250)
setupTu.penup()
tuType.color("pink")
tuType.goto(200,200)
tuType.write("typiano", font = ("Courier New", 20, "normal"), align = "center")
scoreType = turtle.Turtle()
scoreType.penup()
scoreType.color("white")
scoreType.hideturtle()
scoreType.speed(0)
scoreType.goto(200, 175)
scoreType.write("0", font = ("Courier New", 20, "normal"), align = "center")
# drawing frame on the screen <

# screen setup <

# vars >

# x pos for key slots >
d = -199 
f = -137
j = -75
k = -13
# x pos for key slots <
ystart = 338 # default y pos for keys <-
vanP = -363 # vanishing point for keys <-
# key information (ex. 'd' slot key #1: y postion, existance boolean, etc.) >
dKey1y = ystart
fKey1y = ystart
jKey1y = ystart
kKey1y = ystart
dKey2y = ystart
fKey2y = ystart
jKey2y = ystart
kKey2y = ystart
dKey3y = ystart
fKey3y = ystart
jKey3y = ystart
kKey3y = ystart
keyExis = []
keyExis.append([0,0,0])
keyExis.append([0,0,0])
keyExis.append([0,0,0])
keyExis.append([0,0,0])
keyHit = []
keyHit.append([0,0,0])
keyHit.append([0,0,0])
keyHit.append([0,0,0])
keyHit.append([0,0,0])
keySpeed = 4
# key information... <
getKeyD = 0
getKeyF = 0
getKeyJ = 0
getKeyK = 0
slot = 0 # slot number randint <-
keyNum = 0 # key number randint <-
refresh = 0 # counter for screen refresh <-
refreshRate = 3 # rate for screen refresh <-
keySpawn = 0 # counter for key spawn <-
score = 0
runTotal = 0
keyDisplayCount = 0
keyDisplayColor = ""
keyDisplayStr = ""
# vars <

# functions >

# draw keys >
def drawKey(x, y, color):
  tu.color(color)
  tu.goto(x, y+12)
  tu.pendown()
  tu.begin_fill()
  tu.goto(x+61, y+12)
  tu.goto(x+61, y-12)
  tu.goto(x, y-12)
  tu.goto(x,y+12)
  tu.end_fill()
  tu.penup()
# draw keys <
# draw 'd' key >
def drawDkey(y):
  drawKey(d, y, outsideKeyColor)
# draw 'd' key <
# draw 'f' key >
def drawFkey(y):
  drawKey(f, y, middleKeyColor)
# draw 'f' key <
# draw 'j' key >
def drawJkey(y):
  drawKey(j, y, middleKeyColor)
# draw 'j' key <
# draw 'k' key >
def drawKkey(y):
  drawKey(k, y, outsideKeyColor)
# draw 'k' key <
# draw target line >
def drawTline(color):
  linTu.color(color)
  linTu.goto(-200,-250)
  linTu.pendown()
  linTu.goto(49,-250)
  linTu.penup()
def drawTlineD(x):
  global lightColor
  linTu.color(lightColor)
  linTu.goto(d, -250+x)
  linTu.pendown()
  linTu.goto(f-1, -250+x)
  linTu.penup()
def drawTlineF(x):
  linTu.color(lightColor)
  linTu.goto(f, -250+x)
  linTu.pendown()
  linTu.goto(j-1, -250+x)
  linTu.penup()
def drawTlineJ(x):
  linTu.color(lightColor)
  linTu.goto(j, -250+x)
  linTu.pendown()
  linTu.goto(k-1, -250+x)
  linTu.penup()
def drawTlineK(x):
  linTu.color(lightColor)
  linTu.goto(k, -250+x)
  linTu.pendown()
  linTu.goto(49, -250+x)
  linTu.penup()
# draw target line <
# draw scoreboard >
def drawScore():
  global score
  scoreType.clear()
  scoreType.write(score, font = ("Courier New", 20, "normal"), align = "center")
# draw scoreborad <
# store getKeys >
def keyStoD():
  global getKeyD
  global keyHit
  global dKey1y
  global dKey2y
  global dKey3y
  global keyDisplayCount
  global keyDisplayColor
  global keyDisplayStr
  global runTotal
  global score
  if dKey1y > -185 and dKey2y > 185 and dKey3y > 186 and endIsNear != 1:
    score = score -50
    drawScore()
  
  getKeyD = 'd'
  if dKey1y <= -185: # key detection V
    if keyHit[0][0] == 0:
        if getKeyD == 'd':
            if dKey1y == -250:
                keyHit[0][0] = 1
                keyScore("pink")
            elif dKey1y >= -210:
                keyHit[0][0] = 1
                keyScore("cyan")
            elif dKey1y >= -290:
                keyHit[0][0] = 1
                keyScore("yellow")
            elif dKey1y >= -315:
                keyHit[0][0] = 1
                keyScore("cyan")

  if dKey2y <= -185: # key detection V
    if keyHit[0][1] == 0:
        if getKeyD == 'd':
            if dKey2y == -250:
                keyHit[0][1] = 1
                keyScore("pink")
            elif dKey2y >= -210:
                keyHit[0][1] = 1
                keyScore("cyan")
            elif dKey2y >= -290:
                keyHit[0][1] = 1
                keyScore("yellow")
            elif dKey2y >= -315:
                keyHit[0][1] = 1
                keyScore("cyan")
  if dKey3y <= -195: # key detection V
    if keyHit[0][2] == 0:
        if getKeyD == 'd':
            if dKey3y == -250:
                keyHit[0][2] = 1
                keyScore("pink")
            elif dKey3y >= -210:
                keyHit[0][2] = 1
                keyScore("cyan")
            elif dKey3y >= -290:
                keyHit[0][2] = 1
                keyScore("yellow")
            elif dKey3y >= -315:
                keyHit[0][2] = 1
                keyScore("cyan")
def keyStoZD():
  global getKeyD
  getKeyD = 0
def keyStoF():
  global score
  global getKeyF
  global keyHit
  global fKey1y
  global fKey2y
  global fKey3y
  global keyDisplayCount
  global keyDisplayColor
  global keyDisplayStr
  global runTotal
  if fKey1y > -185 and fKey2y > 185 and fKey3y > 186 and endIsNear != 1:
    score = score -50
    drawScore()
  getKeyF = 'f'
  if fKey1y <= -185: # key detection V
    if keyHit[1][0] == 0:
        if getKeyF == 'f':
            if fKey1y == -250:
                keyHit[1][0] = 1
                keyScore("pink")
            elif fKey1y >= -210:
                keyHit[1][0] = 1
                keyScore("cyan")
            elif fKey1y >= -290:
                keyHit[1][0] = 1
                keyScore("yellow")
            elif fKey1y >= -315:
                keyHit[1][0] = 1
                keyScore("cyan")
  if fKey2y <= -185: # key detection V
    if keyHit[1][1] == 0:
        if getKeyF == 'f':
            if fKey2y == -250:
                keyHit[1][1] = 1
                keyScore("pink")
            elif fKey2y >= -210:
                keyHit[1][1] = 1
                keyScore("cyan")
            elif fKey2y >= -290:
                keyHit[1][1] = 1
                keyScore("yellow")
            elif fKey2y >= -315:
                keyHit[1][1] = 1
                keyScore("cyan")
  if fKey3y <= -185: # key detection V
    if keyHit[1][2] == 0:
        if getKeyF == 'f':
            if fKey3y == -250:
                keyHit[1][2] = 1
                keyScore("pink")
            elif fKey3y >= -210:
                keyHit[1][2] = 1
                keyScore("cyan")
            elif fKey3y >= -290:
                keyHit[1][2] = 1
                keyScore("yellow")
            elif fKey3y >= -315:
                keyHit[1][2] = 1
                keyScore("cyan")
def keyStoZF():
   global getKeyF
   getKeyF = 0
def keyStoJ():
  global keyHit
  global score
  global jKey1y
  global jKey2y
  global jKey3y
  global keyDisplayCount
  global keyDisplayColor
  global keyDisplayStr
  global runTotal
  global getKeyJ


  if jKey1y > -185 and jKey2y > 185 and jKey3y > 186 and endIsNear!=1:
    score = score -50
    drawScore()
  getKeyJ = 'j'
  if jKey1y <= -185: # key detection V
    if keyHit[2][0] == 0:
        if getKeyJ == 'j':
            if jKey1y == -250:
                keyHit[2][0] = 1
                keyScore("pink")
            elif jKey1y >= -210:
                keyHit[2][0] = 1
                keyScore("cyan")
            elif jKey1y >= -290:
                keyHit[2][0] = 1
                keyScore("yellow")
            elif jKey1y >= -315:
                keyHit[2][0] = 1
                keyScore("cyan")
  if jKey2y <= -185: # key detection V
    if keyHit[2][1] == 0:
        if getKeyJ == 'j':
            if jKey2y == -250:
                keyHit[2][1] = 1
                keyScore("pink")
            elif jKey2y >= -210:
                keyHit[2][1] = 1
                keyScore("cyan")
            elif jKey2y >= -290:
                keyHit[2][1] = 1
                keyScore("yellow")
            elif jKey2y >= -315:
                keyHit[2][1] = 1
                keyScore("cyan")
  if jKey3y <= -195: # key detection V
    if keyHit[2][2] == 0:
        if getKeyJ == 'j':
            if jKey3y == -250:
                keyHit[2][2] = 1
                keyScore("pink")
            elif jKey3y >= -210:
                keyHit[2][2] = 1
                keyScore("cyan")
            elif jKey3y >= -290:
                keyHit[2][2] = 1
                keyScore("yellow")
            elif jKey3y >= -315:
                keyHit[2][2] = 1
                keyScore("cyan")
def keyStoZJ():
   global getKeyJ
   getKeyJ = 0
def keyStoK():
  global keyHit
  global score
  global kKey1y
  global kKey2y
  global kKey3y
  global keyDisplayCount
  global keyDisplayColor
  global keyDisplayStr
  global runTotal
  global getKeyK
  if kKey1y > -185 and kKey2y > 185 and kKey3y > 186 and endIsNear !=1:
    score = score -50
    drawScore()
  getKeyK = 'k'
  if kKey1y <= -185: # key detection V
    if keyHit[3][0] == 0:
        if getKeyK == 'k':
            if kKey1y == -250:
                keyHit[3][0] = 1
                keyScore("pink")
            elif kKey1y >= -210:
                keyHit[3][0] = 1
                keyScore("cyan")
            elif kKey1y >= -290:
                keyHit[3][0] = 1
                keyScore("yellow")
            elif kKey1y >= -315:
                keyHit[3][0] = 1
                keyScore("cyan")
  if kKey2y <= -185: # key detection V
    if keyHit[3][1] == 0:
        if getKeyK == 'k':
            if kKey2y == -250:
                keyHit[3][1] = 1
                keyScore("pink")
            elif kKey2y >= -210:
                keyHit[3][1] = 1
                keyScore("cyan")
            elif kKey2y >= -290:
                keyHit[3][1] = 1
                keyScore("yellow")
            elif kKey2y >= -315:
                keyHit[3][1] = 1
                keyScore("cyan")
  if kKey3y <= -195: # key detection V
    if keyHit[3][2] == 0:
        if getKeyK == 'k':
            if kKey3y == -250:
                keyHit[3][2] = 1
                keyScore("pink")
            elif kKey3y >= -210:
                keyHit[3][2] = 1
                keyScore("cyan")
            elif kKey3y >= -290:
                keyHit[3][2] = 1
                keyScore("yellow")
            elif kKey3y >= -315:
                keyHit[3][2] = 1
                keyScore("cyan")
def keyStoZK():
   global getKeyK
   getKeyK = 0
# store getKeys <
# draw key score >
def keyScore(num):
  global keyDisplayCount
  global keyDisplayColor
  global keyDisplayStr
  global runTotal
  global score
  runTotal = runTotal + 1
  tuKeyScore.goto(-75, -125)
  if num == "yellow":
    global threes
    threes = threes + 1
    score =  score + 300
    keyDisplayColor = "yellow"
    keyDisplayStr = "300"
    tuKeyScore.color("yellow")
    tuKeyScore.clear()
    tuKeyScore.write("300", font = ("Courier New", 20, "normal"), align = "center")
  if num == "cyan":
    global ones
    ones = ones + 1
    score = score + 100
    keyDisplayColor = "cyan"
    keyDisplayStr = "100"
    tuKeyScore.color("cyan")
    tuKeyScore.clear()
    tuKeyScore.write("100", font = ("Courier New", 20, "normal"), align = "center")
  if num == "red":

    runTotal = 0

    keyDisplayColor = "red"
    keyDisplayStr = "MISS"
    tuKeyScore.color("red")
    tuKeyScore.clear()
    tuKeyScore.write("MISS", font = ("Courier New", 20, "normal"), align = "center")
  if num == "pink":
    global fives
    fives = fives + 1
    score = score + 500
    keyDisplayColor = "pink"
    keyDisplayStr = "500"
    tuKeyScore.color("pink")
    tuKeyScore.clear()
    tuKeyScore.write("500", font = ("Courier New", 20, "normal"), align = "center")
  keyDisplayCount = 20
  drawRunTotal()
  drawScore()
# draw key scores <
# draw run total >
def drawRunTotal():
    tuRunTotal.goto(-75,-100)
    tuRunTotal.clear()
    tuRunTotal.write(runTotal, font = ("Courier New", 20, "normal"), align = "center")


# draw run total <
# functions <

# key bindings >
win.listen()
win.onkeypress(keyStoD, 'd')
win.onkeyrelease(keyStoZD, 'd')
win.onkeypress(keyStoF, 'f')
win.onkeyrelease(keyStoZF, 'f')
win.onkeypress(keyStoJ, 'j')
win.onkeyrelease(keyStoZJ, 'j')
win.onkeypress(keyStoK, 'k')
win.onkeyrelease(keyStoZK, 'k')
# key bindings <

# game loop >
while timE != timeGoal:
  time.sleep(0.003)
  timE = timE + 1
  if timE % 100 == 0:
    tuTime.clear()
    tuTime.color("white")
    tuTime.goto(200,100)
    tuTime.write("time:", font = ("Courier New", 20, "normal"), align = "center")
    tuTime.goto(200, 75)
    tuTime.write(   str(int((timeGoal*100 - timE*100) / 10000))    , font = ("Courier New", 20, "normal" ), align = "center" )
  
  keySpawn = keySpawn + 1 # key spawning V
  if keySpawn == keySpawnRate:
    slot = random.randint(0,3)
    keyNum = random.randint(0,2)
    if discoMode == 1:
      r = random.randint(20,255)
      g = random.randint(20,255)
      b = random.randint(20,255)
      middleKeyColor = (r,g,b)
      outsideKeyColor = (r,g,b)
    if keyExis[slot][keyNum] == 0:
       keysSpawned = keysSpawned + 1


    if keyExis[slot][keyNum] == 0:
        keyExis[slot][keyNum] = 1
        keyHit[slot][keyNum] = 0
    keySpawn = 0

  tu.clear()
  
  if keyExis[0][0] == 1: # move keys down through slots V
    if dKey1y != vanP and dKey1y > vanP:
      dKey1y = dKey1y - keySpeed
      if keyHit[0][0] == 0:
        drawDkey(dKey1y)
    else:
      keyExis[0][0] = 0
      dKey1y = ystart
  if keyExis[1][0] == 1: # move keys down through slots V
    if fKey1y != vanP and fKey1y > vanP:
      fKey1y = fKey1y - keySpeed
      if keyHit[1][0] == 0:
        drawFkey(fKey1y)
    else:
      keyExis[1][0] = 0
      fKey1y = ystart
  if keyExis[2][0] == 1: # move keys down through slots V
    if jKey1y != vanP and jKey1y > vanP:
      jKey1y = jKey1y - keySpeed
      if keyHit[2][0] == 0:
        drawJkey(jKey1y)
    else:
      keyExis[2][0] = 0
      jKey1y = ystart
  if keyExis[3][0] == 1: # move keys down through slots V
    if kKey1y != vanP and kKey1y > vanP:
      kKey1y = kKey1y - keySpeed
      if keyHit[3][0] == 0:
        drawKkey(kKey1y)
    else:
      keyExis[3][0] = 0
      kKey1y = ystart
  if keyExis[0][1] == 1: # move keys down through slots V
    if dKey2y != vanP and dKey2y > vanP:
      dKey2y = dKey2y - keySpeed
      if keyHit[0][1] == 0:
        drawDkey(dKey2y)
    else:
      keyExis[0][1] = 0
      dKey2y = ystart
  if keyExis[1][1] == 1: # move keys down through slots V
    if fKey2y != vanP and fKey2y > vanP:
      fKey2y = fKey2y - keySpeed
      if keyHit[1][1] == 0:
        drawFkey(fKey2y)
    else:
      keyExis[1][1] = 0
      fKey2y = ystart
  if keyExis[2][1] == 1: # move keys down through slots V
    if jKey2y != vanP and jKey2y > vanP:
      jKey2y = jKey2y - keySpeed
      if keyHit[2][1] == 0:
        drawJkey(jKey2y)
    else:
      keyExis[2][1] = 0
      jKey2y = ystart
  if keyExis[3][1] == 1: # move keys down through slots V
    if kKey2y != vanP and kKey2y > vanP:
      kKey2y = kKey2y - keySpeed
      if keyHit[3][1] == 0:
        drawKkey(kKey2y)
    else:
      keyExis[3][1] = 0
      kKey2y = ystart
  if keyExis[0][2] == 1: # move keys down through slots V
    if dKey3y != vanP and dKey3y > vanP:
      dKey3y = dKey3y - keySpeed
      if keyHit[0][2] == 0:
        drawDkey(dKey3y)
    else:
      keyExis[0][2] = 0
      dKey3y = ystart
  if keyExis[1][2] == 1: # move keys down through slots V
    if fKey3y != vanP and fKey3y > vanP:
      fKey3y = fKey3y - keySpeed
      if keyHit[1][2] == 0:
        drawFkey(fKey3y)
    else:
      keyExis[1][2] = 0
      fKey3y = ystart
  if keyExis[2][2] == 1: # move keys down through slots V
    if jKey3y != vanP and jKey3y > vanP:
      jKey3y = jKey3y - keySpeed
      if keyHit[2][2] == 0:
        drawJkey(jKey3y)
    else:
      keyExis[2][2] = 0
      jKey3y = ystart
  if keyExis[3][2] == 1: # move keys down through slots V
    if kKey3y != vanP and kKey3y > vanP:
      kKey3y = kKey3y - keySpeed
      if keyHit[3][2] == 0:
        drawKkey(kKey3y)
    else:
      keyExis[3][2] = 0
      kKey3y = ystart


  refresh = refresh + 1 # controlling refresh rate V
  if refresh == refreshRate:
    win.update()
    tu.clear()
    refresh = 0

  if dKey3y < -315:
    if keyHit[0][2] == 0:
      keyScore("red")

  if dKey2y < -315:
    if keyHit[0][1] == 0:
      keyScore("red")

  if dKey1y < -315:
    if keyHit[0][0] == 0:
      keyScore("red")

  if fKey1y < -315:
    if keyHit[1][0] == 0:
      keyScore("red")

  if fKey2y < -315:
    if keyHit[1][1] == 0:
      keyScore("red")

  if fKey3y < -315:
    if keyHit[1][2] == 0:
      keyScore("red")

  if jKey1y < -315:
    if keyHit[2][0] == 0:
      keyScore("red")

  if jKey2y < -315:
    if keyHit[2][1] == 0:
      keyScore("red")

  if jKey3y < -315:
    if keyHit[2][2] == 0:
      keyScore("red")

  if kKey1y < -315:
    if keyHit[3][0] == 0:
      keyScore("red")

  if kKey2y < -315:
    if keyHit[3][1] == 0:
      keyScore("red")

  if kKey3y < -315:
    if keyHit[3][2] == 0:
      keyScore("red")


  linTu.clear()
  drawTline(borderColor)
  if getKeyD == 'd':
    for i in range(0,50,7):
      drawTlineD(i)
  if getKeyF == 'f':
    for i in range(0,50,7):
      drawTlineF(i)
  if getKeyJ == 'j':
    for i in range(0,50,7):
      drawTlineJ(i)
  if getKeyK == 'k':
    for i in range(0,50,7):
      drawTlineK(i)

  if keyDisplayCount != 0:
    keyDisplayCount = keyDisplayCount - 1
    if keyDisplayCount == 0:
      tuKeyScore.clear()

# game loop <

# print score >
endIsNear = 1
scoreType.clear()
tuRunTotal.clear()
tuKeyScore.clear()
tuType.clear()
tu.clear()
setupTu.clear()
linTu.clear()
tuTime.clear()
tu.color("white")
tu.goto(0,30)
tu.write("Score:", font = ("Courier New", 20, "normal"), align = "center")
tu.home()
tu.write(score, font = ("Courier New", 20, "normal"), align = "center")
win.update()
time.sleep(5)
tu.clear()
tu.color("white")

#there's a wierd glitch here, something to do with keybidnigns; doesn't really matter tho


tu.write("tyson diệp may 2023", font = ("Courier New", 20, "normal"), align = "center")
scoreType.clear()
tuRunTotal.clear()
tuKeyScore.clear()
tuType.clear()
setupTu.clear()
linTu.clear()
tuTime.clear()
win.update()
time.sleep(5)
