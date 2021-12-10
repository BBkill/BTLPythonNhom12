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

movingSpeed = 40  # tốc độ của cái bát
game = Tk()
game.title("Chú Ếch tham ăn")
canvas = Canvas(master=game, width=Width, height=Hight, background="white", bd=0)
canvas.pack()

img = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
img[0] = ImageTk.PhotoImage(Image.open("backgr.png").resize((1000,630),Image.ANTIALIAS))
img[1] = ImageTk.PhotoImage(Image.open("bowl.png").resize((150,90),Image.ANTIALIAS))
img[2] = [ImageTk.PhotoImage(Image.open("apple.png").resize((50,50),Image.ANTIALIAS)),50,50]
img[3] = ImageTk.PhotoImage(Image.open("bomb.png"))
img[4] = ImageTk.PhotoImage(Image.open("bomm.png"))
img[5] = ImageTk.PhotoImage(Image.open("addHeart.png"))
img[6] = ImageTk.PhotoImage(Image.open("goldApple.png"))
img[7] = ImageTk.PhotoImage(Image.open("over.png"))
img[8] = ImageTk.PhotoImage(Image.open("replay.png"))
img[9] = ImageTk.PhotoImage(Image.open("duahau.png"))
img[10] = ImageTk.PhotoImage(Image.open("quaLe.png"))
img[11] = ImageTk.PhotoImage(Image.open("score.png"))
heart = [0, 0, 0]

backgr = canvas.create_image(0, 0, anchor=NW, image=img[0])
bowl = canvas.create_image(0, 450, anchor=NW, image=img[1])

def setup(speed):
    global fallingSpeed, Score, live, file, highestScore, heart, apple, bomb, appleGold, ADDHeart, CoutingtScore, HighestScore, h
    x = randint(rangeL, rangeR)
    y = -40
    fallingSpeed=speed
    apple = [canvas.create_image(x, y, anchor=NW, image=img[2][0])]
    bomb = canvas.create_image(x, y, anchor=NW, image=img[3])
    appleGold = canvas.create_image(x, y, anchor=NW, image=img[6])
    ADDHeart = canvas.create_image(x, y, anchor=NW, image=img[5])
    h=[10,45,80]
    heart[0] = canvas.create_image(h[0], 5, anchor=NW, image=img[5])
    heart[1] = canvas.create_image(h[1], 5, anchor=NW, image=img[5])
    heart[2] = canvas.create_image(h[2], 5, anchor=NW, image=img[5])
    Score = 0  # điểm
    file = open("HighestScore.txt", "r")
    highestScore = int(file.readline())
    file.close()
    live = 3  # mạng
    CoutingtScore = canvas.create_text(860, 20, text="Score: " + str(Score), font=("Consolas", 14), fill="white")
    HighestScore = canvas.create_text(905,40, text="Highest Score: " + str(highestScore),font=("Consolas", 14),fill="white")
    canvas.update()


apple = [canvas.create_image(0, 0, anchor=NW, image=img[2][0])]

from apple import Apple
def fallingApple():
  global apple
  apple2 = Apple(apple,1,canvas)  
  apple2.falling()

while True:
  fallingApple()
  setup(1/1000)