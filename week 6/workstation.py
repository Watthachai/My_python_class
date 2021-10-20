import random


cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]*4



def deal_card(cards):
        #แจก card 2 ใบ
        hand = []
        for i in range(2):
                random.shuffle(cards)
                card = cards.pop() #สร้างตัวแปรรับค่า card จากที่เอาออกจาก List
                hand.append(card)
        
        print(cards)
        return(hand)

def add_card(cards,hand):
        new_hand = hand.copy() #สร้าง List ใหม่เพื่อรับค่า list เก่า
        random.shuffle(cards) #สลับตำแหน่งใน List
        card = cards.pop() #สร้างตัวแปรรับค่า card จากที่เอาออกจาก List
        new_hand.append(card)
        return new_hand

def cal_score(card):
        score = 0
        for x in card:
                if card == 11:                  
	                if score >= 11:                 #ถ้ามี card มากกว่า 11 ace จะบวก 1
                                score += 1
                score += x
       
        return score
 

def replay():
        play = input("Do you want play agin(Y/N) ? : ").lower()
        if play == 'y':
                user_hand = []
                com_hand = []
                global cards 
                cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]*4
                main()
        else:
                print('Good Bye')
                exit()

def blackjack_check(user_hand,com_hand):

        #เช็คว่ามี blackjack รึป่าว
        
        if (cal_score(com_hand) == 21) :
                print('You lose!')
                print("Computer's final card : "+str(com_hand)+' fianl score : '+str(cal_score(com_hand)))
                replay()
        elif (cal_score(user_hand) == 21):
                print('You win!')
                print("Computer's final card : "+str(com_hand)+' fianl score : '+str(cal_score(com_hand)))
                replay()

def compare(user_hand,com_hand):
        if (cal_score(user_hand) == cal_score(com_hand)):
                print('Draw!')
                print("Computer's final card : "+str(com_hand)+' fianl score : '+str(cal_score(com_hand)))
                replay()
        if (cal_score(user_hand) < cal_score(com_hand)):
                print('You lose!')
                print("Computer's final card : "+str(com_hand)+' fianl score : '+str(cal_score(com_hand)))
                replay()
        if (cal_score(user_hand) > cal_score(com_hand)):
                print('You win!')
                print("Computer's final card : "+str(com_hand)+' fianl score : '+str(cal_score(com_hand)))
                replay()


def main():

       
        print('Welcome to Black Jack !')
        #แจก card 2 ใบ
        user_hand = deal_card(cards)
        com_hand = deal_card(cards)

        print("Your Card is : "+str(user_hand) +'current score : '+str(cal_score(user_hand)))
        print("Computer's first card : "+str(com_hand[0]))
        #เช็คว่ามี blackjack รึป่าว
        blackjack_check(user_hand,com_hand)


        #ถ้าไม่มีให้ player เลือกที่จะจั่ว หรือ ไม่จั่ว
        user_turn = True


        while user_turn:
                option =  input("Type 'y' to get another card, type 'n' to pass : ").lower()

                if option == 'y':
                        user_hand = add_card(cards,user_hand)
                        print("Your Card is : "+str(user_hand) +'current score : '+str(cal_score(user_hand)))
                
                        blackjack_check(user_hand,com_hand)
                        #เช็คหากว่าคะแนนเกิน 21 หรือไม่
                        if cal_score(user_hand) > 21:
                                user_turn = False
                                print("Your are busted , you lose!")
                                replay()
                elif option == 'n':
                        user_turn = False
        #รอบของ computer 
        Computer_turn = True
        while Computer_turn:
                #ถ้า คะแนนยังไม่ถึง 17 ให้จั่วไปเรื่อยๆ
                if cal_score(com_hand) < 17 :
                        com_hand = add_card(cards,com_hand)
                        blackjack_check(user_hand,com_hand)
                        #เช็คหากว่าคะแนนเกิน 21 หรือไม่
                        if cal_score(com_hand) > 21 :
                                Computer_turn = False
                                print("Computer's final card : "+str(com_hand)+' fianl score : '+str(cal_score(com_hand)))
                                print("Computer busted , Your win!")
                                replay()
                else:
                        compare(user_hand,com_hand)



main()