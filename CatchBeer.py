# Menu
from os import system
import sys
from tkinter.constants import FALSE
from tkinter import *
from typing import Tuple
import pygame
from pygame import mouse
from pygame.constants import K_BACKSPACE, K_ESCAPE, MOUSEBUTTONDOWN, QUIT
import pygame.display
import pygame.event
import pygame.draw
import pygame.mouse
from pygame.time import Clock
import pygame.time
import pygame.font
import pygame.image
from playsound import playsound

pygame.init()

# Khởi tạo Menu game
def setupMenu():
    screen.blit(image,(0,0))
    screen.blit(menu,(70,60))
    screen.blit(menuContent,(240,90))
    screen.blit(levelContent,(235,212))
    screen.blit(helpContent,(245,272))
    screen.blit(playContent,(190,150))
    screen.blit(aboutContent,(230,335))
    screen.blit(exitContent,(249,396))

# Nút back
def back():
    screen.blit(nutback,(530,80))

# lựa chọn About
def aboutBlock():
    screen.blit(image,(0,0))
    screen.blit(about,(50,70))
    screen.blit(aboutText1,(170,240))
    screen.blit(aboutText2,(220,275))
    screen.blit(TV1,(200,310))
    screen.blit(TV2,(200,340))
    screen.blit(TV3,(200,370))
    screen.blit(TV4,(200,400))
    back()
# lựa chọn Level
def levelBlock():
    screen.blit(image,(0,0))
    screen.blit(level,(130,70))
    screen.blit(lv1,(295,160))
    screen.blit(lv2,(275,260))
    screen.blit(lv3,(295,360))
    back()
# Lựa chọn Help
def coverBlock():
    screen.blit(image,(0,0))
    screen.blit(help,(50,80))
    screen.blit(guildContent_line_1,(168,200))
    screen.blit(guildContent_line_2,(168,235))
    screen.blit(guildContent_line_3,(168,270))
    screen.blit(guildContent_line_4,(168,305))
    screen.blit(guildContent_line_5,(168,340))
    screen.blit(guildContent_line_6,(168,375))
    back()

# Khởi tạo cửa sổ giao diện
screen = pygame.display.set_mode((1000, 633))
GREY = (120, 120, 120)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# text format
font = pygame.font.SysFont("corbel", 32, True)
font1 = pygame.font.SysFont("corbel", 28, True)

# Các lựa chọn ở Menu
menuContent = font.render("MENU", True, WHITE)
playContent = font.render("PLAY GAME", True, WHITE)
levelContent = font.render("LEVEL", True, WHITE)
helpContent = font.render("HELP", True, WHITE)
exitContent = font.render("EXIT", True, WHITE)
aboutContent = font.render("ABOUT", True, WHITE)

# Nội dung lựa chọn Help
guildContent_line_1 = font1.render("Sử dụng chuột để điều", True, WHITE)
guildContent_line_2 = font1.render("khiển chú ếch ăn được", True, WHITE)
guildContent_line_3 = font1.render("nhiều bánh và trái cây", True, WHITE)
guildContent_line_4 = font1.render("Hãy nhớ tránh những quả", True, WHITE)
guildContent_line_5 = font1.render("bom và các con bọ vì chúng", True, WHITE)
guildContent_line_6 = font1.render("sẽ làm mất điểm và mạng.", True, WHITE)

# Nội dung lựa chọn About
aboutText1= font1.render("Game được thực hiện ", True, WHITE)
aboutText2= font1.render("bởi nhóm 12:", True, WHITE)
TV1= font1.render("Hoàng Anh Quân", True, WHITE)
TV2= font1.render("Trần Quang Minh", True, WHITE)
TV3= font1.render("Đỗ Minh Đức", True, WHITE)
TV4= font1.render("Nguyễn Ngọc Dương", True, WHITE)

# Nội dung lựa chọn Level
lv1=font1.render("EASY", True, BLACK)
lv2=font1.render("MEDIUM", True, BLACK)
lv3=font1.render("HARD", True, BLACK)

# Load ảnh thiết kế giao diện
nutback=pygame.image.load('nutback.png')
image = pygame.image.load('nen.png') 
menu = pygame.image.load('menu.png')
level = pygame.image.load('level.png')
help= pygame.image.load('help.png')
about= pygame.image.load('about.png')

# tốc độ của vật thể rơi
fallingSpeed = 1  
speed=fallingSpeed

running = True

while running:

    clock = pygame.time.Clock()
    clock.tick(60)
    screen.fill(GREY)
    setupMenu()
    inMenu = True
    helpCheck = False
    aboutCheck = False
    levelCheck= False

    while inMenu:
        # bắt sự kiện click chuột
        mouse_x, mouse_y = pygame.mouse.get_pos()
        
        # Nếu chọn lựa chọn Level
        if levelCheck == True:
            levelBlock()
            # bắt sự kiện click chuột
            mouse_x, mouse_y = pygame.mouse.get_pos()
            for eventMenu in pygame.event.get():
                if eventMenu.type == pygame.QUIT:
                    sys.exit()
                if eventMenu.type == MOUSEBUTTONDOWN:
                    if (180 < mouse_x < 475) and (136 < mouse_y < 208):
                        speed=fallingSpeed/2
                        setupMenu()
                        levelCheck = False
                        break
                    if (180 < mouse_x < 475) and (234 < mouse_y < 305):
                        speed=fallingSpeed
                        setupMenu()
                        levelCheck = False
                        break
                    if (180 < mouse_x < 475) and (334 < mouse_y < 404):
                        speed=fallingSpeed+0.5
                        setupMenu()
                        levelCheck = False
                        break
                    if (540 < mouse_x < 655) and (87 < mouse_y < 142):
                        setupMenu()
                        levelCheck = False
            pygame.display.update()
       
        # Nếu chọn lựa chọn Help
        if helpCheck == True:
            coverBlock()
            mouse_x, mouse_y = pygame.mouse.get_pos()
            for eventMenu in pygame.event.get():
                if eventMenu.type == pygame.QUIT:
                    sys.exit()
                if eventMenu.type == MOUSEBUTTONDOWN:
                    if (540 < mouse_x < 655) and (87 < mouse_y < 142):
                        setupMenu()
                        helpCheck= False
            pygame.display.update()
        
        # Nếu chọn lựa chọn About
        if aboutCheck == True:
            aboutBlock()
            mouse_x, mouse_y = pygame.mouse.get_pos()
            for eventMenu in pygame.event.get():
                if eventMenu.type == pygame.QUIT:
                    sys.exit()
                if eventMenu.type == MOUSEBUTTONDOWN:
                    if (540 < mouse_x < 655) and (87 < mouse_y < 142):
                        setupMenu()
                        aboutCheck = False
            pygame.display.update()

        if levelCheck==False and helpCheck==False and aboutCheck==False:
            for eventMenu in pygame.event.get():
                #quit
                if eventMenu.type == pygame.QUIT:
                    sys.exit()
                if eventMenu.type == MOUSEBUTTONDOWN:
                    # Lựa chọn play
                    if (157 < mouse_x < 404) and (136 < mouse_y < 184):
                        inMenu = False
                        running = False
                        break
                    # Lựa chọn level
                    if (157 < mouse_x < 404) and (197 < mouse_y < 250):
                        levelCheck = True
                        break
                    # Lựa chọn help
                    if (157 < mouse_x < 404) and (263 < mouse_y < 305):
                        helpCheck = True
                        break
                    # lựa chọn about
                    if (157 < mouse_x < 404) and (322 < mouse_y < 372):
                        aboutCheck = True
                        break
                    # Lựa chọn Exit
                    if (157 < mouse_x < 404) and (386 < mouse_y < 430):
                        sys.exit()
            
        pygame.display.update()                
    pygame.display.update()
pygame.display.quit()

# Game
from tkinter import *
from time import sleep
from PIL import ImageTk, Image
from random import randint

# độ rộng của cửa nền
Width = 1000
Hight = 630

# khoảng xuất hiện táo
rangeR = 680
rangeL = 20

game = Tk()
game.title("Chú Ếch tham ăn")
canvas = Canvas(master=game, width=Width, height=Hight, background="white", bd=0)
canvas.pack()
gameOver = False

# List các item và game
img = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
#Background
img[0] = [ImageTk.PhotoImage(Image.open("backgr.png").resize((1000,630),Image.ANTIALIAS)),ImageTk.PhotoImage(Image.open("backgr2.png").resize((1000,630),Image.ANTIALIAS))]
#Con ếch
img[1] = [ImageTk.PhotoImage(Image.open("bowl.png").resize((80,80),Image.ANTIALIAS)),80,80]
#Quả táo
img[2] = [ImageTk.PhotoImage(Image.open("apple.png").resize((50,50),Image.ANTIALIAS)),50,50]
#Bom
img[3] = [ImageTk.PhotoImage(Image.open("bomb.png").resize((90,90),Image.ANTIALIAS)),90,90]
# Hoạt ảnh bom nổ
img[4] = ImageTk.PhotoImage(Image.open("bomm.png"))
# Trái tim
img[5] = [ImageTk.PhotoImage(Image.open("addHeart.png").resize((55,55),Image.ANTIALIAS)),55,55]
# Táo vàng
img[6] = [ImageTk.PhotoImage(Image.open("goldApple.png").resize((50,50),Image.ANTIALIAS)),50,50]
# Hoạt ảnh Gameover
img[7] = ImageTk.PhotoImage(Image.open("over.png"))
# Hoạt ảnh Replay
img[8] = ImageTk.PhotoImage(Image.open("replay.png"))
# Quả dưa hấu
img[9] = [ImageTk.PhotoImage(Image.open("duahau.png").resize((55,55),Image.ANTIALIAS)),55,55]
# Quả lê
img[10] = [ImageTk.PhotoImage(Image.open("quaLe.png").resize((50,60),Image.ANTIALIAS)),50,60]
# Khung hiện điểm khi gameover
img[11] = ImageTk.PhotoImage(Image.open("score.png"))
# Con bọ rệp
img[12] = [ImageTk.PhotoImage(Image.open("borep.png").resize((60,60),Image.ANTIALIAS)),60,60]
# Hộp quà bí ẩn
img[13] = [ImageTk.PhotoImage(Image.open("qua.png").resize((60,60),Image.ANTIALIAS)),60,60]
# Mạng chơi
heart = [0, 0, 0]
backgr = canvas.create_image(0, 0, anchor=NW, image=img[0][0])
backgr = canvas.create_image(0, 0, anchor=NW, image=img[0][1])
bowl = canvas.create_image(0, 530, anchor=NW, image=img[1][0])

# Hàm khởi tạo khi bắt đầu chơi
def setup(speed):
    global bowl,backgr,demlevel,fallingSpeed, Score, live, file, highestScore, heart, fruit, bomb, bo, appleGold, ADDHeart, giftbox, CoutingtScore, HighestScore, h, dembg
    demlevel=0
    backgr = canvas.create_image(0, 0, anchor=NW, image=img[0][0])
    backgr = canvas.create_image(0, 0, anchor=NW, image=img[0][1])
    bowl = canvas.create_image(0, 530, anchor=NW, image=img[1][0])

    img[2] = [ImageTk.PhotoImage(Image.open("apple.png").resize((50,50),Image.ANTIALIAS)),50,50]
    img[6] = [ImageTk.PhotoImage(Image.open("goldApple.png").resize((50,50),Image.ANTIALIAS)),50,50]
    img[9] = [ImageTk.PhotoImage(Image.open("duahau.png").resize((55,55),Image.ANTIALIAS)),55,55]
    img[10] = [ImageTk.PhotoImage(Image.open("quaLe.png").resize((50,60),Image.ANTIALIAS)),50,60]
    dembg=0
    fallingSpeed=speed
    fruit = [canvas.create_image(randint(rangeL, rangeR), -20, anchor=NW, image=img[2][0])]
    bomb = canvas.create_image(randint(rangeL, rangeR), -3500, anchor=NW, image=img[3][0])
    bo = canvas.create_image(randint(rangeL, rangeR), -50, anchor=NW, image=img[12][0])
    appleGold = canvas.create_image(randint(rangeL, rangeR), -100, anchor=NW, image=img[6][0])
    ADDHeart = canvas.create_image(randint(rangeL, rangeR), -5000, anchor=NW, image=img[5][0])
    giftbox = canvas.create_image(randint(rangeL, rangeR), -10000, anchor=NW, image=img[13][0])
    h=[10,50,90]
    heart[0] = canvas.create_image(h[0], 2, anchor=NW, image=img[5][0])
    heart[1] = canvas.create_image(h[1], 2, anchor=NW, image=img[5][0])
    heart[2] = canvas.create_image(h[2], 2, anchor=NW, image=img[5][0])
    Score = 0  # điểm
    file = open("HighestScore.txt", "r")
    highestScore = int(file.readline())
    file.close()
    live = 3  # mạng
    CoutingtScore = canvas.create_text(860, 20, text="Score: " + str(Score), font=("Consolas", 14), fill="white")
    HighestScore = canvas.create_text(905,40, text="Highest Score: " + str(highestScore),font=("Consolas", 14),fill="white")
    canvas.update()
# tạo trái cây
def fallingFruit():
    global fruit, Score, highestScore, file,fallingSpeed , demlevel, dembg, demhq
    canvas.move(fruit, 0, fallingSpeed)
    y = -20
    x = randint(rangeL, rangeR)
    if canvas.coords(fruit)[1] > Hight-img[2][2]/2:
        canvas.delete(fruit)
        rdFruit= randint(1,3)
        if rdFruit==1:
            fruit = canvas.create_image(x, y, anchor=NW, image=img[2][0])
        else:
            if rdFruit==2:
                fruit = canvas.create_image(x, y, anchor=NW, image=img[9][0])
            else:
                fruit = canvas.create_image(x, y, anchor=NW, image=img[10][0])

    if (
        canvas.coords(fruit)[0]+img[2][1]//2 >= canvas.coords(bowl)[0]
        and 
        canvas.coords(fruit)[0] + img[2][1]//2 <= canvas.coords(bowl)[0] + img[1][1]
    ) and (
        canvas.coords(fruit)[1] + img[2][2]*3//5 >= canvas.coords(bowl)[1]
        and  
        canvas.coords(fruit)[1] + img[2][2]*3//5 <= canvas.coords(bowl)[1]+img[1][2]//3
    ): 
        canvas.delete(fruit)
        rdFruit= randint(1,3)
        if rdFruit==1:
            fruit = canvas.create_image(x, y, anchor=NW, image=img[2][0])
        else:
            if rdFruit==2:
                fruit = canvas.create_image(x, y, anchor=NW, image=img[9][0])
            else:
                fruit = canvas.create_image(x, y, anchor=NW, image=img[10][0])
        Score = Score + 1
        canvas.itemconfig(CoutingtScore, text="Score: " + str(Score))
        demlevel = demlevel +1
        dembg = dembg+1
        levelup()
    canvas.update()
# tạo táo vàng
def GoldApple():
    global appleGold, Score, highestScore, file,Hight,demlevel, dembg
    canvas.move(appleGold, 0, fallingSpeed)
    y = -100
    x = randint(rangeL, rangeR)
    if canvas.coords(appleGold)[1]+img[6][2]//2 > Hight:
        canvas.delete(appleGold)            
        appleGold = canvas.create_image(x, y, anchor=NW, image=img[6][0])
    if (
        canvas.coords(appleGold)[0]+img[6][1]//2 >= canvas.coords(bowl)[0]
        and 
        canvas.coords(appleGold)[0] + img[6][1]//2 <= canvas.coords(bowl)[0] + img[1][1]
    ) and (
        canvas.coords(appleGold)[1] + img[6][2]*3//5 >= canvas.coords(bowl)[1]
        and 
        canvas.coords(appleGold)[1] + img[6][2]*3//5 <= canvas.coords(bowl)[1] + img[1][2]//3
    ):
        canvas.delete(appleGold)
        appleGold = canvas.create_image(x, y, anchor=NW, image=img[6][0])
        Score = Score + 3
        canvas.itemconfig(CoutingtScore, text="Score: " + str(Score))
        demlevel = demlevel + 1
        dembg = dembg+3
        levelup()
    canvas.update()

# bom rơi
def fallingBomb():
    global bomb, live, gameOver,Hight
    canvas.move(bomb, 0, fallingSpeed)
    y=0
    x = randint(rangeL, rangeR)
    if canvas.coords(bomb)[1]+img[3][2]//2 > Hight:
        canvas.delete(bomb)
        bomb = canvas.create_image(x, y, anchor=NW, image=img[3][0])
    if (
        canvas.coords(bomb)[0]+img[3][1]//2 >= canvas.coords(bowl)[0]
        and 
        canvas.coords(bomb)[0] + img[3][1]//2 <= canvas.coords(bowl)[0] + img[1][1]
    ) and (
        canvas.coords(bomb)[1] + img[3][2]*3//5 >= canvas.coords(bowl)[1]
        and 
        canvas.coords(bomb)[1] + img[3][2]*3//5 <= canvas.coords(bowl)[1] + img[1][2]//3
    ):
        canvas.delete(bomb)
        x = randint(rangeL, rangeR)
        bomb = canvas.create_image(x, y, anchor=NW, image=img[3][0])
        live = live - 1
        canvas.delete(heart[live])
        if live == 0:
            gameOver = True
        bomm = canvas.create_image(260, 60, anchor=NW, image=img[4])
        canvas.update()
        sleep(0.3)
        canvas.delete(bomm)
    canvas.update()

# Tạo bọ
def addbo():
    global bo, Score,Hight,demlevel,dembg
    canvas.move(bo, 0, fallingSpeed)
    y=-50
    x = randint(rangeL, rangeR)
    if canvas.coords(bo)[1]+img[12][2]//2 > Hight:
        canvas.delete(bo)
        bo = canvas.create_image(x, y, anchor=NW, image=img[12][0])
    if (
        canvas.coords(bo)[0]+img[12][1]//2 >= canvas.coords(bowl)[0]
            and 
        canvas.coords(bo)[0] + img[12][1]//2 <= canvas.coords(bowl)[0] + img[1][1]
    ) and (
        canvas.coords(bo)[1] + img[12][2]*3//5 >= canvas.coords(bowl)[1]
        and 
        canvas.coords(bo)[1] + img[12][2]*3//5 <= canvas.coords(bowl)[1] + img[1][2]//3
    ):
        canvas.delete(bo)
        bo = canvas.create_image(x, y, anchor=NW, image=img[12][0])
        if Score>0:
            Score = Score - 1
        canvas.itemconfig(CoutingtScore, text="Score: " + str(Score))
        if demlevel>0:
            demlevel= demlevel -1
        if dembg>0:
            dembg = dembg -1
        levelup()
    canvas.update()

# thêm mạng
def HelpHeart():
    global ADDHeart, live,Hight
    canvas.move(ADDHeart, 0, fallingSpeed)
    y=0
    x = randint(rangeL, rangeR)
    if canvas.coords(ADDHeart)[1]+img[5][2]//2 > Hight:
        canvas.delete(ADDHeart)
        ADDHeart = canvas.create_image(x, y, anchor=NW, image=img[5][0])
    if (
        canvas.coords(ADDHeart)[0] +img[5][1]//2 >= canvas.coords(bowl)[0]
        and 
        canvas.coords(ADDHeart)[0] + img[5][1]//2 <= canvas.coords(bowl)[0] + img[1][1]
    ) and (
        canvas.coords(ADDHeart)[1] + img[5][2]*3//5 >= canvas.coords(bowl)[1]
        and 
        canvas.coords(ADDHeart)[1] + img[5][2]*3//5 <= canvas.coords(bowl)[1] + img[1][2]//3
    ):
        canvas.delete(ADDHeart)
        ADDHeart = canvas.create_image(x, y, anchor=NW, image=img[5][0])
        if live<3:
            live = live + 1
            heart[live-1]=canvas.create_image(h[live-1], 2, anchor=NW, image=img[5][0])
        canvas.update()
    canvas.update()

#Hộp quà
def hopqua():
    global giftbox, live,Hight, highestScore, Score
    canvas.move(giftbox, 0, fallingSpeed)
    y = 0
    x = randint(rangeL, rangeR)
    if canvas.coords(giftbox)[1]+img[13][2]//2 > Hight:
        canvas.delete(giftbox)
        giftbox = canvas.create_image(x, y, anchor=NW, image=img[13][0])
    if (
        canvas.coords(giftbox)[0] +img[13][1]//2 >= canvas.coords(bowl)[0]
        and canvas.coords(giftbox)[0] + img[13][1]//2 <= canvas.coords(bowl)[0] + img[1][1]
    ) and (
        canvas.coords(giftbox)[1] + img[13][2]*3//5 >= canvas.coords(bowl)[1]
        and canvas.coords(giftbox)[1] + img[13][2]*3//5 <= canvas.coords(bowl)[1] + img[1][2]//3
    ):
        canvas.delete(giftbox)
        giftbox = canvas.create_image(x, y, anchor=NW, image=img[13][0])
        r=randint(1,4)
        if(r==4):
            Score*=2
        else:
            Score= Score +r*10
        canvas.itemconfig(CoutingtScore, text="Score: " + str(Score))
    canvas.update()

# Di chuyển con ếch bằng vị trí của chuột
def motion(event):
  global bowl
  canvas.move(bowl,event.x-canvas.coords(bowl)[0]-75,0)
  canvas.update()

canvas.bind_all('<Motion>',motion)

#Bắt click chuột khi gameover
def click1(event):
  global gameOver,fruit, appleGold, bomb, ADDHeart,bo
  x= event.x
  y= event.y
  if x>470 and x<570 and y>420 and y<520:
      canvas.delete(over)
      canvas.delete(replay)
      canvas.delete(fruit)
      canvas.delete(appleGold)
      canvas.delete(bomb)
      canvas.delete(bo)
      canvas.delete(ADDHeart)
      canvas.delete(giftbox)
      canvas.delete(endgame)
      canvas.delete(yourscore)
      canvas.delete(biggestscore)
      gameOver=False
      canvas.update()
      playGame()

# Tăng tốc độ rơi của vật thể dần theo số item ăn được và chuyển màn
def levelup():
    global Score,demlevel,fallingSpeed,dembg,backgr,bowl
    if demlevel >= 15:
        fallingSpeed=fallingSpeed+1
        demlevel=demlevel - 15
    if dembg >= 50 :
        dembg=0
        canvas.delete(backgr)
        img[2][0]=ImageTk.PhotoImage(Image.open("cake1.png").resize((50,50),Image.ANTIALIAS))
        img[6][0]=ImageTk.PhotoImage(Image.open("cake3.png").resize((50,50),Image.ANTIALIAS))
        img[9][0]=ImageTk.PhotoImage(Image.open("keo.png").resize((55,55),Image.ANTIALIAS))
        img[10][0]=ImageTk.PhotoImage(Image.open("cake2.png").resize((50,60),Image.ANTIALIAS))

# Hàm playgame
def playGame():
    global gameOver, over, replay, endgame, yourscore, biggestscore, highestScore, Score
    setup(speed)
    while not gameOver:
        fallingFruit()
        GoldApple()
        fallingBomb()
        HelpHeart()
        addbo()
        hopqua()
        sleep(1/300)  # set delay
    if highestScore < Score:
            highestScore = Score
            canvas.itemconfig(HighestScore, text="Highest Score: " + str(Score))
    canvas.itemconfig(CoutingtScore, text="Score: " + str(Score))
    file = open("HighestScore.txt", "w")
    file.write(str(highestScore))
    file.close()
    over = canvas.create_image(365 , 25 , anchor=NW, image=img[7])
    replay = canvas.create_image(470, 420, anchor=NW, image=img[8])
    endgame= canvas.create_image(348, 297, anchor=NW, image=img[11])
    yourscore= canvas.create_text(520, 345, text="Your Score: " + str(Score), font=("Consolas", 18), fill="white")
    biggestscore= canvas.create_text( 522, 380, text="Hightest Score: " + str(highestScore), font=("Consolas", 18), fill="white")
    canvas.delete(CoutingtScore)
    canvas.delete(HighestScore)
    canvas.update()
    canvas.bind_all("<Button-1>",click1)


while True:

    check = True
    playGame()
    canvas.update()
    game.mainloop()
    
