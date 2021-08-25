
import random
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = (('2', 2), ('3', 3), ('4', 4), ('5', 5), ('6', 6),
         ('7', 7), ('8', 8), ('9', 9), ('T', 10), ('J', 10), ('Q', 10), ('K', 10), ('A', 1))


class Card:
    '''Because rank is assigned from something with an index, Python will expect a list or tuple'''  # Use the multiline comments to write docstrings

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank[0]
        self.value = rank[1]

    def __str__(self):
        # Use f-strings to format (cleanest)
        return f'{self.rank} of {self.suit}'


class Deck():

    def __init__(self):

        self.deck = []

        # Iterate through the suits and ranks via nested loops, append each card into a list to create the deck
        for x in suits:
            for y in ranks:
                self.deck.append(Card(x, y))

    def shuffle(self):
        random.shuffle(self.deck)

    def deal_one(self):
        return self.deck.pop()


class Hand():

    def __init__(self):
        self.cards = []
        self.sum = 0
        self.aces = 0  # Keep track of number of ace
        self.sum_adj = 0

    def add_card(self, card):
        self.cards.append(card)
        self.sum += card.value

        # We want to track number of ace dealt
        if card.value == 1:
            self.aces += 1

    def adjust_for_aces(self):
        '''Ace by default is 1'''

        self.sum_adj = self.sum

        if self.aces == 0:
            print(f'Hand value is {self.sum}.')
        elif self.sum <= 11:
            self.sum_adj = self.sum + 10
            print(f'Hand value can be either {self.sum} or {self.sum_adj}.')
        else:
            print(f'Hand value is {self.sum}.')

    def check_blackjack(self):
        '''Call this function before hit_or_stand , to check presence of blackjack which is an automatic win'''

        if self.sum == 11 and self.aces == 1:
            playing = False
        else:
            playing = True

        return playing


class Player(Hand):

    def __init__(self):
        Hand.__init__(self)  # Can also call super(Player, self).__init__()
        # I prefer single quotes, less space
        self.name = input('Please enter your name: ')

    def check_bet(self, bets):
        '''This function keep track of players balance when betting, win or lose
        We will do if statement to ensure balance can cover bet amount in game logic section'''

        if self.bets <= self.balance:
            self.balance -= bets
            print(f'{self.name} bets: {bets}')
        else:
            print("You don't have enough in your balance.")

    def balance_input(self):
        while True:
            try:
                self.balance = int(input('How much bankroll do you have? '))
            except:
                print('Sorry please provide an integer')
            else:
                break

    def bet_input(self):
        while True:
            try:
                self.bet = int(
                    input('How much would you like to bet on this game? '))
                print(f'{self.name} bets: {self.bet}')
            except:
                print("Sorry please provide an integer")
            else:
                if self.bet > self.balance:
                    print(
                        f"Sorry, you don't have enough in your balance to cover your bet. You have: {self.balance}")
                else:
                    break

    def hit_or_stand(self):
        '''This function take in Deck and Hand object and assgin playing as a global variable. If player want to hit, deploy the hit function. If player stands, set playing variable to False'''

        while True:
            if self.sum_adj < 21:
                x = input('Would you like to hit or stand? Enter h or s: ')

                if x[0].lower() == 'h':
                    self.add_card(deck.deal_one())
                    print(f'{self.name} gets: {self.cards[-1]}')
                    self.adjust_for_aces()

                elif x[0].lower() == 's':
                    print(f"{self.name} stands. Dealer's turn.")
                    break
                else:
                    print('Sorry, I did not understand that, please enter h or s only!')

            elif self.sum_adj == 21:
                print(f"{self.name} have 21! {self.name} will stand ")
                break
            else:
                print("Bust!")
                self.lose()
                break

    def win(self):
        self.balance += self.bet
        print(f'Congraduation {self.name}, you have won double your bets!')
        print(f'Your new balance is {self.balance}')

    def lose(self):
        self.balance -= self.bet
        print(f'{self.name}, you have lost your bets!')
        print(f'Your new balance is {self.balance}')


class Dealer(Hand):

    def __init__(self):
        Hand.__init__(self)

    def hit_or_stand(self):
        '''This function take in Deck and Hand object and assgin playing as a global variable. If player want to hit, deploy the hit function, if player stands, set playing variable to False'''

        while self.sum_adj < 17:
            print('Dealer will hit!')
            self.add_card(deck.deal_one())
            print(f'Dealer gets: {self.cards[-1]}')
            self.adjust_for_aces()

    def win(self):
        print(f'Dealer win! {player.name} loses!')
        player.lose()

    def lose(self):
        print(f'Dealer lose! {player.name} wins!')
        player.win()


def show_some(player, dealer):
    print("\nDealer's Hand:")
    print(" <card hidden>")
    print('', dealer.cards[1])
    print(f"\n{player.name}'s Hand:", *player.cards, sep='\n ')


def show_dealer(dealer):
    print("\nDealer's Hand:", *dealer.cards, sep='\n ')
    #print("Dealer's Hand =",player.sum)


def show_all(player, dealer):
    print("\nDealer's Hand:", *dealer.cards, sep='\n ')
    print("Dealer's Hand =", max(dealer.sum, dealer.sum_adj))

    print(f"\n{player.name}'s Hand:", *player.cards, sep='\n ')
    print(f"{player.name}'s Hand =", max(player.sum, player.sum_adj))


game_on = True
while game_on:
    print('''Welcome to BlackJack! Get as close to 21 as you can without going over!
Dealer hits until she reaches 17. Aces count as 1 or 11.''')

    # Initialize and shuffle the deck
    deck = Deck()
    deck.shuffle()
    # Create the players
    dealer = Dealer()
    player = Player()

    # Get inputs
    player.balance_input()
    player.bet_input()

    # Initiate the dealing of cards
    player.add_card(deck.deal_one())
    dealer.add_card(deck.deal_one())
    player.add_card(deck.deal_one())
    dealer.add_card(deck.deal_one())

    show_some(player, dealer)

    global playing
    playing = True

    player.check_blackjack()

    # If player does have BJ, playing_player = False
    if not playing:  # Check this way for truthiness with Booleans!
        print('Player has a blackjack!')
        dealer.check_blackjack()
        if playing:  # Means dealer don't have BJ
            print(
                f'Congraduation,{player.name} has blackjack. {player.name} won! ')
            player.win()
        elif not playing:
            print('Both the dealer and the player have blackjack, it is a tie')

    if playing:
        player.adjust_for_aces()
        # The method will regulate when player want hit or stand and when play bust!
        player.hit_or_stand()

    # If player has not busted
    while player.sum_adj <= 21 and playing == True:
        show_dealer(dealer)
        dealer.check_blackjack()

        if not playing:  # meaning dealer have blackjack
            print('Dealer have blackjack!')
            player.lose()
        if playing:  # meaning dealer doesn't have blackjack
            dealer.adjust_for_aces()
            dealer.hit_or_stand()  # the method will regulate when dealer hit or stand
            show_all(player, dealer)

        if dealer.sum_adj > 21:
            print(f"Dealer Bust! {player.name} wins! ")
            player.win()
            break

            # when dealer stands and did not go bust, this if will activate
            # dealer wins
        elif max(player.sum, player.sum_adj) < max(dealer.sum, dealer.sum_adj):
            dealer.win()
            break

            # dealer loses
        elif max(player.sum, player.sum_adj) > max(dealer.sum, dealer.sum_adj):
            dealer.lose()
            break

        elif max(player.sum, player.sum_adj) == max(dealer.sum, dealer.sum_adj):
            print(
                f"Dealer and {player.name} tie! It's a push. {player.name} still have {player.balance} in balance.")
            break

    new_game = input('Would you like to play another hand? Enter Y or N: ')

    while True:
        if new_game[0].lower() == 'y':
            game_on = True
            break
        elif new_game[0].lower() == 'n':
            game_on = False
            break
        else:
            new_game = input(
                'Would you like to play another hand? Enter Y or N: ')
