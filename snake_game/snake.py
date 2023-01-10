import cv2
import cvzone
from cvzone.HandTrackingModule import HandDetector
import math
import random
import numpy as np


detector=HandDetector(maxHands=1,detectionCon=0.8)

cap=cv2.VideoCapture(0)
cap.set(3,1200)
cap.set(4,800)

class snakeClass:
    def __init__(self,path):
        self.initialitaion()
        self.snakeFood()
        self.food=cv2.imread(path,cv2.IMREAD_UNCHANGED)
        self.wfood,self.hfood,_=self.food.shape
        self.score=0
        self.gameover=False

    def initialitaion(self):
        self.points=[]
        self.currrentPoints=[]
        self.foodPoint=0,0
        self.allowdLength=150
        
        self.currentLength=0
        self.length=[]
        self.previousHead=0,0
        self.snakeFood()


     #food points
    def snakeFood(self):
        self.foodPoints=random.randint(100,300),random.randint(100,300)
    
    def update(self,imgMain,currentHead):
        if self.gameover:
            cv2.putText(imgMain,"Game Over",(150,150),cv2.FONT_HERSHEY_COMPLEX,1,(255,0,0),2)
            cv2.putText(imgMain,"Your Score:"+str(self.score),(150,200),cv2.FONT_HERSHEY_COMPLEX,1,(255,0,0),2)
        else:
            px,py=self.previousHead
            cx,cy=currentHead
            self.points.append([cx,cy])

            distance=math.hypot(cx-px,cy-py)
            self.length.append(distance)
            self.currentLength+=distance
            self.previousHead=cx,cy


            # #Reduce length
            if self.currentLength>self.allowdLength:
                for i,len in enumerate(self.length):
                    self.currentLength-=len
                    self.points.pop(i)
                    self.length.pop(i)
                    if self.currentLength<self.allowdLength:
                        break

            
            if self.points:
                for i,point in enumerate(self.points):
                    if i!=0:
                        cv2.line(imgMain,self.points[i-1],self.points[i],(0,255,0),15)
                    cv2.circle(imgMain,(cx,cy),5,(0,255,0),cv2.FILLED)
            
            #draw food
            rx,ry=self.foodPoints
            imgMain=cvzone.overlayPNG(imgMain,self.food,(rx-self.hfood//2,ry-self.wfood//2))

            #eating food
            if (rx-self.hfood//2<cx<rx+self.hfood//2 and ry-self.wfood//2<cy<ry+self.wfood//2):
                self.allowdLength+=20
                self.score+=1
                self.snakeFood()
            cv2.putText(imgMain,"Score:"+str(self.score),(5,25),cv2.FONT_HERSHEY_COMPLEX,1,(255,0,255),2)
            print(self.score)

            for i,point in enumerate(self.points):
                if np.size(self.points)>20 and i<np.size(self.points)-30:
                    dst=math.hypot(point[0]-cx,point[1]-cy)
                    if -1<dst<1:
                        self.gameover=True
                        self.initialitaion()

        return imgMain


class SNAKE:
    def __init__(self):
        self.startGame

    def startGame(self):
        game=snakeClass("Donut.png")
        while True:
            frame,img=cap.read()
            img=cv2.resize(img,(1000,600))
            img=cv2.flip(img,1)
            hands,img=detector.findHands(img,flipType=False)

            if hands:
                lmlist=hands[0]['lmList']
                center=lmlist[8][0:2]
                img=game.update(img,center)
                
            cv2.imshow("image",img)
            cv2.waitKey(1)

snakeGame = SNAKE()
snakeGame.startGame()