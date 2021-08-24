
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = (('2',2), ('3',3), ('4',4), ('5',5), ('6',6), 
         ('7',7), ('8',8), ('9',9), ('T',10), ('J',10), ('Q',10), ('K',10), ('A',1))

import random

#card class
class Card:
    
    def __init__ (self, suit, rank): #because rank is assigned from something with an index, Python will expect a list or tuple
        
        self.suit = suit
        self.rank = rank[0]
        self.value = rank[1]
        
    def __str__ (self):

        return self.rank+' of '+ self.suit

#deck class
class Deck():
      
    def __init__(self):
        
        self.deck = []
        
        for x in suits: #iterate through the suits and ranks via nested loops, append each card into a list to create the deck
            for y in ranks:
                self.deck.append(Card(x,y))
                
    def shuffle(self):
        random.shuffle(self.deck)
        
    def deal_one(self):
        return self.deck.pop()
                
    
        

class Hand():
    
    def __init__(self):
        self.cards = []
        self.sum = 0
        self.aces = 0 #keep track of number of ace
        self.sum_adj = 0

        
    def add_card (self, card):
        self.cards.append(card)
        self.sum += card.value
        
        #we want to track number of ace dealt
        if card.value == 1:
            self.aces +=1

    def adjust_for_aces (self):
        #Ace by default is 1
        self.sum_adj = self.sum
        
        if self.aces == 0:
            print (f'Hand value is {self.sum}.')
        else:
            ''''
            while self.sum +10 < 21 and self.aces != 0: 
                self.sum_adj = self.sum + 10
                self.aces -= 1
                if self.sum_adj <= 21:
                    print (f'hand value can be either {self.sum} or {self.sum_adj}.')
               
             '''
            if self.sum <= 11:
                self.sum_adj = self.sum + 10
                print (f'Hand value can be either {self.sum} or {self.sum_adj}.')
            else:
                print (f'Hand value is {self.sum}.')
        
    def check_blackjack (self):
    # call this function before hit_or_stand , to check presence of blackjack which is an automatic win

        if  self.sum == 11 and self.aces == 1 :
            #self.balance = self.balance + 1.5*bet
            
            #print (f'Congradulation, {self.name} have blackjack! You won one and half times your bets!')
            #print (f'Your new balance is {self.balance}')
            playing = False
            return playing
        else:
            playing = True
            return playing

#Player class

class Player(Hand):
    
    def __init__ (self):
        Hand.__init__ (self)
        self.name = input("Please enter your name: ")
    #this function keep track of players balance when betting, win or lose
    #We will do if statement to ensure balance can cover bet amount in game logic section
    
    '''
    def check_bet(self):
        if self.bets <= self.balance:
            self.balance -= bets
            print(f'{self.name} bets: {bets}')
        else:
            print("You don't have enough in your balance.")
    
    '''
    def balance_input (self):
        
        while True:
        
            try:
                self.balance = int(input('How much bankroll do you have? '))
            except:
                print("Sorry please provide an integer")
            else:
                break
                    
    def bet_input (self):
    
        while True:
        
            try:
                self.bet = int(input('How much would you like to bet on this game? ')) 
                print(f'{self.name} bets: {self.bet}')
            except:
                print("Sorry please provide an integer")
            else:
                if self.bet > self.balance:
                    print("Sorry, you don't have enough in your balance to cover your bet. You have: {}". format(self.balance))
                else:
                    break

    

            
    
    def hit_or_stand(self):
    #this function take in Deck and Hand object and assgin playing as a global variable
    #if player want to hit, deploy the hit function, if player stands, set playing variable to False
        
    
        while True:
            if self.sum_adj < 21:  
                x=input('Would you like to hit or stand? Enter h or s: ') 
        
                if x[0].lower() == 'h':
                    self.add_card(deck.deal_one())
                    print (f"{self.name} gets: {self.cards[-1]}")
                    self.adjust_for_aces()
            
                elif x[0].lower() == 's':
                    print (f"{self.name} stands. Dealer's turn.")
                    break
                else:
                    print('Sorry, I did not understand that, please enter h or s only!')
                    
            elif self.sum_adj == 21:
                print (f"{self.name} have 21! {self.name} will stand ")
                break
            else:
                print ("Bust!")
                self.lose()
                break

    def win (self):
        self.balance += self.bet 
        print (f'Congraduation {self.name}, you have won double your bets!')
        print (f'Your new balance is {self.balance}')
    
    def lose (self):
        self.balance -= self.bet 
        print (f'{self.name}, you have lost your bets!')
        print (f'Your new balance is {self.balance}')
        
        
    
    

class Dealer(Hand):
    
    def __init__ (self):
        Hand.__init__ (self)

    
    def hit_or_stand(self):
    #this function take in Deck and Hand object and assgin playing as a global variable
    #if player want to hit, deploy the hit function, if player stands, set playing variable to False
        
        
        while self.sum_adj < 17: 
                
            print('Dealer will hit!')
            self.add_card(deck.deal_one())
            print (f"Dealer gets: {self.cards[-1]}")
            self.adjust_for_aces()
            
            
            
    def win(self):
        print (f'Dealer win! {player.name} loses!')
        player.lose()
        
    def lose(self):
        print (f'Dealer lose! {player.name} wins!')
        player.win()
        
        
def show_some(player,dealer):
    print("\nDealer's Hand:")
    print(" <card hidden>")
    print('',dealer.cards[1])  
    print(f"\n{player.name}'s Hand:", *player.cards, sep='\n ')
    
def show_dealer(dealer):
    print("\nDealer's Hand:", *dealer.cards, sep='\n ')
    #print("Dealer's Hand =",player.sum)
    
def show_all(player,dealer):
    print("\nDealer's Hand:", *dealer.cards, sep='\n ')
    print("Dealer's Hand =",max(dealer.sum, dealer.sum_adj))

    print(f"\n{player.name}'s Hand:", *player.cards, sep='\n ')
    print(f"{player.name}'s Hand =", max(player.sum, player.sum_adj))


# In[ ]:


game_on = True
while game_on:

    print('Welcome to BlackJack! Get as close to 21 as you can without going over!\n    Dealer hits until she reaches 17. Aces count as 1 or 11.')
    
    deck = Deck()
    deck.shuffle()
    dealer = Dealer()
    player = Player()

    player.balance_input()
    player.bet_input()

    player.add_card(deck.deal_one())
    dealer.add_card(deck.deal_one())
    player.add_card(deck.deal_one())
    dealer.add_card(deck.deal_one())

    show_some(player,dealer)
    
   # global playing_player
    #global playing_dealer
    global playing
    #playing_player = True
    #playing_dealer = True
    playing  = True
    
    player.check_blackjack()
     
    
    #if player does have BJ, playing_player = False
    if playing == False:
        print ('Player have blackjack!')
        dealer.check_blackjack()
        if playing == True: #means dealer don't have BJ
            print (f'Congraduation,{player.name} has blackjack. {player.name} won! ')
            player.win()
        elif playing == False:
            print('Both the dealer and the player have blackjack, it is a tie')
    
    if playing == True:
        player.adjust_for_aces()
        player.hit_or_stand() #the method will regulate when player want hit or stand and when play bust!
    
    #if player has not busted
    while player.sum_adj <=21 and playing == True:
        
        show_dealer(dealer)
        
        dealer.check_blackjack()
        if playing == False: #meaning dealer have blackjack
            print ('Dealer have blackjack!')
            player.lose()
        if playing == True: #meaning dealer doesn't have blackjack
            dealer.adjust_for_aces()
            dealer.hit_or_stand() #the method will regulate when dealer hit or stand
            show_all(player,dealer)
        
        if dealer.sum_adj >21:
            print (f"Dealer Bust! {player.name} wins! ")
            player.win()
            break
        
            #when dealer stands and did not go bust, this if will activate 
            #dealer wins
        elif max(player.sum, player.sum_adj) < max(dealer.sum, dealer.sum_adj) :
            dealer.win()
            break
    
            #dealer loses
        elif max(player.sum, player.sum_adj) > max(dealer.sum, dealer.sum_adj):
            dealer.lose()
            break
        
        elif max(player.sum, player.sum_adj) == max(dealer.sum, dealer.sum_adj):
            print (f"Dealer and {player.name} tie! It's a push. {player.name} still have {player.balance} in balance.")
            break
    
    new_game = input('Would you like to play another hand? Enter Y or N: ')
    
    while True:
        if new_game[0].lower() == 'y':
            game_on = True
            #IPython.display.clear_output()
            break
        elif new_game[0].lower() == 'n':
            game_on = False
            break
        else:
            new_game = input('Would you like to play another hand? Enter Y or N: ')
        


# In[ ]:




