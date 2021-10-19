import random
import time

slot = {}
Game_Over = False
Game_lose = False

def interface():
    print("_"*25)
    print("| "+slot.get("11"," ")+" | "+slot.get("12"," ")+" | "+slot.get("13"," ")+" | "+slot.get("14"," ")+" | "+slot.get("15"," ")+" | "+slot.get("16"," ")+" | ")
    print("| "+slot.get("21"," ")+" | "+slot.get("22"," ")+" | "+slot.get("23"," ")+" | "+slot.get("24"," ")+" | "+slot.get("25"," ")+" | "+slot.get("26"," ")+" | ")
    print("| "+slot.get("31"," ")+" | "+slot.get("32"," ")+" | "+slot.get("33"," ")+" | "+slot.get("34"," ")+" | "+slot.get("35"," ")+" | "+slot.get("36"," ")+" | ")
    print("| "+slot.get("41"," ")+" | "+slot.get("42"," ")+" | "+slot.get("43"," ")+" | "+slot.get("44"," ")+" | "+slot.get("45"," ")+" | "+slot.get("46"," ")+" | ")
    print("| "+slot.get("51"," ")+" | "+slot.get("52"," ")+" | "+slot.get("53"," ")+" | "+slot.get("54"," ")+" | "+slot.get("55"," ")+" | "+slot.get("56"," ")+" | ")
    print("| "+slot.get("61"," ")+" | "+slot.get("62"," ")+" | "+slot.get("63"," ")+" | "+slot.get("64"," ")+" | "+slot.get("65"," ")+" | "+slot.get("66"," ")+" | ")
    print("_"*25)

def insert(x,slot,player):
    for y in range(6,0,-1):
        if(slot.get(str(y)+str(x),False)):
            continue;
        else:    
            if player == 1 :
                slot[str(y)+str(x)] ='x'
                print(player)
                check(int(x),int(y))
                break
            elif player == 2 :
                time.sleep(0.2)
                slot[str(y)+str(x)] ='w'
                check(int(x),int(y))
                break
            

def check(x,y):

    #แนวนอน
    global Game_Over
    global Game_lose
    p1 = slot.get(str(y)+str(x),False)
    p2 = slot.get(str(y)+str(x+1),False)
    p3 = slot.get(str(y)+str(x+2),False)
    if p1 == 'x' and  p2 == 'x' and p3 == 'x':
            Game_Over = True
    elif p1 == 'w' and  p2 == 'w' and p3 == 'w':
            Game_lose = True
    p1 = slot.get(str(y)+str(x),False)
    p2 = slot.get(str(y)+str(x-1),False)
    p3 = slot.get(str(y)+str(x-2),False)
    if p1 == 'x' and  p2 == 'x' and p3 == 'x':
            Game_Over = True
    elif p1 == 'w' and  p2 == 'w' and p3 == 'w':
            Game_lose = True
    p1 = slot.get(str(y)+str(x),False)
    p2 = slot.get(str(y)+str(x-1),False)
    p3 = slot.get(str(y)+str(x+1),False)
    if p1 == 'x' and  p2 == 'x' and p3 == 'x':
            Game_Over = True
    elif p1 == 'w' and  p2 == 'w' and p3 == 'w':
            Game_lose = True
    
    #แนวตั้ง
    p1 = slot.get(str(y)+str(x),False)
    p2 = slot.get(str(y+1)+str(x),False)
    p3 = slot.get(str(y+2)+str(x),False)
    if p1 == 'x' and  p2 == 'x' and p3 == 'x':
            Game_Over = True
    elif p1 == 'w' and  p2 == 'w' and p3 == 'w':
            Game_lose = True
    p1 = slot.get(str(y)+str(x),False)
    p2 = slot.get(str(y-1)+str(x),False)
    p3 = slot.get(str(y-2)+str(x),False)
    if p1 == 'x' and  p2 == 'x' and p3 == 'x':
            Game_Over = True
    elif p1 == 'w' and  p2 == 'w' and p3 == 'w':
            Game_lose = True
    p1 = slot.get(str(y)+str(x),False)
    p2 = slot.get(str(y+1)+str(x),False)
    p3 = slot.get(str(y-1)+str(x),False)
    if p1 == 'x' and  p2 == 'x' and p3 == 'x':
            Game_Over = True
    elif p1 == 'w' and  p2 == 'w' and p3 == 'w':
            Game_lose = True
  
    #เฉียงซ้าย
    p1 = slot.get(str(y)+str(x),False)
    p2 = slot.get(str(y+1)+str(x+1),False)
    p3 = slot.get(str(y+2)+str(x+2),False)
    if p1 == 'x' and  p2 == 'x' and p3 == 'x':
            Game_Over = True
    elif p1 == 'w' and  p2 == 'w' and p3 == 'w':
            Game_lose = True
    p1 = slot.get(str(y)+str(x),False)
    p2 = slot.get(str(y-1)+str(x-1),False)
    p3 = slot.get(str(y-2)+str(x-2),False)
    if p1 == 'x' and  p2 == 'x' and p3 == 'x':
            Game_Over = True
    elif p1 == 'w' and  p2 == 'w' and p3 == 'w':
            Game_lose = True
    p1 = slot.get(str(y)+str(x),False)
    p2 = slot.get(str(y+1)+str(x+1),False)
    p3 = slot.get(str(y-1)+str(x-1),False)
    if p1 == 'x' and  p2 == 'x' and p3 == 'x':
            Game_Over = True
    elif p1 == 'w' and  p2 == 'w' and p3 == 'w':
            Game_lose = True

    #เฉียงขวา
    p1 = slot.get(str(y)+str(x),False)
    p2 = slot.get(str(y+1)+str(x-1),False)
    p3 = slot.get(str(y+2)+str(x-2),False)
    if p1 == 'x' and  p2 == 'x' and p3 == 'x':
            Game_Over = True
    elif p1 == 'w' and  p2 == 'w' and p3 == 'w':
            Game_lose = True
    p1 = slot.get(str(y)+str(x),False)
    p2 = slot.get(str(y-1)+str(x+1),False)
    p3 = slot.get(str(y-2)+str(x+2),False)
    if p1 == 'x' and  p2 == 'x' and p3 == 'x':
            Game_Over = True
    elif p1 == 'w' and  p2 == 'w' and p3 == 'w':
            Game_lose = True
    p1 = slot.get(str(y)+str(x),False)
    p2 = slot.get(str(y-1)+str(x+1),False)
    p3 = slot.get(str(y+1)+str(x-1),False)
    if p1 == 'x' and  p2 == 'x' and p3 == 'x':
            Game_Over = True
    elif p1 == 'w' and  p2 == 'w' and p3 == 'w':
            Game_lose = True

def check_coin(coin):
    if coin <= 6 :
        player = 1
        insert(coin,slot,player)
        computer = random.randint(1,6)
        player = 2
        insert(computer,slot,player)

    elif coin >= 7:
        print('Pls Select 1-6!')
    elif coin <= 0:
        print('Pls Select 1-6!')


while True:     
    while True:
        interface()
        coin = int(input(" [1] [2] [3] [4] [5] [6]  :"))
        check_coin(coin)
        
        if(Game_Over):
            interface()
            print("You Win ! : Computer Lose")
            reset = input("Play Agin? [Y/N] : ")
            if reset == "Y" or reset == 'y':
                slot.clear()
                Game_Over = False
                
            elif reset == 'N' or reset == 'n':
                slot.clear()
                Game_Over = True
                exit()
            else:
                slot.clear()
                print("Error!")
                exit()
        elif(Game_lose):
            interface()
            print("Computer Win ! : You Lose")
            reset = input("Play Agin? [Y/N] : ")
            if reset == "Y" or reset == 'y':
                slot.clear()
                Game_Over = False
                
            elif reset == 'N' or reset == 'n':
                slot.clear()
                Game_Over = True
                exit()
            else:
                slot.clear()
                print("Error!")
                exit()