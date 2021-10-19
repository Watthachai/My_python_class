import random


cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]



def deal_card(cards):
        hand = []
        for i in range(2):
                random.shuffle(cards)
                card = cards.pop()
                hand.append(card)
        return(hand)

def add_card(cards,hand):
        new_hand = hand.copy()
        random.shuffle(cards)
        card = cards.pop()
        new_hand.append(card)
        return new_hand

def cal_score(card):
        score = 0
        for x in card:
                if card == 11:
	                if score >= 11: 
                                score += 1
                score += x
       
        return score

def first_check(user_hand,com_hand):
        if (cal_score(com_hand) == 21) :
                print('You lose!')
                print("Computer's final card : "+str(com_hand)+' fianl score : '+str(cal_score(com_hand)))
                exit()
        elif (cal_score(user_hand) == 21):
                print('You win!')
                print("Computer's final card : "+str(com_hand)+' fianl score : '+str(cal_score(com_hand)))
                exit()

def main():

       
        print('Welcome to Black Jack !')
  
        user_hand = deal_card(cards)
        com_hand = deal_card(cards)

        print("Your Card is : "+str(user_hand) +'current score : '+str(cal_score(user_hand)))
        print("Computer's first card : "+str(com_hand[0]))
        first_check(user_hand,com_hand)

          user_turn = True


        while user_turn:
                option =  input("Type 'y' to get another card, type 'n' to pass : ").lower()

                if option == 'y':
                        user_hand = add_card(cards,user_hand)
                        print("Your Card is : "+str(user_hand) +'current score : '+str(cal_score(user_hand)))
                        first_check(user_hand,com_hand)
                        if cal_score(user_hand) > 21:
                                user_turn = False
                                print("Your are busted , you lose!")
                elif option == 'n':
                        user_turn == False

        



main()