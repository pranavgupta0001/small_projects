"""



"""

# %%
import random

playerBank = None


def printLine(n=1):
    print("-"*22 + "\n"*n)


class Bank():
    def __init__(self):
        self.balance = 0
        self.bet = 0

    def addMoney(self):
        while True:
            try:
                amount = input(
                    "How much money did you want to add in your Casino account.")
                amount = int(amount)
                break
            except:
                print("Enter Valid number containing digits 0-9")
        self.balance += amount
        print("Your new Balance: {}".format(self.getBalance))

    def subtractMoney(self, amount):
        self.balance -= amount

    def placeBet(self):
        if self.getBet > 0:
            print("Your Bet on these Cards: {}".format(self.getBet))
        while True:
            try:
                amount = input("How much money did you want to bet.")
                amount = int(amount)
                if amount > self.getBalance-self.getBet:
                    print("Your Total Bet: {}\nYour Balance: {}\nYou can not bet more than you have.".format(
                        self.getBet, self.getBalance))
                    continue
                break
            except:
                print("Enter Valid number containing digits 0-9")
        self.bet += amount
        print("Your Bet on these Cards: {}".format(self.getBet))

    def completeBet(self, won=None):
        if won:
            self.balance += self.getBet*2
            print("Amount added to your account: {}\nYour Balance: {}".format(
            self.getBet*2, self.getBalance))
        elif won == None:
            self.bet = 0
            print("Amount added to your account: 0\nYour Balance: {}".format(
            self.getBalance))
        else:
            self.balance -= self.getBet
            print("Amount subtracted from your account: {}\nYour Balance: {}".format(
            self.getBet, self.getBalance))

        

        self.bet = 0

    @property
    def getBalance(self):
        return self.balance

    @property
    def getBet(self):
        return self.bet


class Card():
    def __init__(self, rank, shape):
        self.rank = rank
        self.shape = shape

    def __str__(self) -> str:
        if self.rank == 1:
            return f"Ace of {self.shape}"
        elif self.rank == 11:
            return f"Joker of {self.shape}"
        elif self.rank == 12:
            return f"Queen of {self.shape}"
        elif self.rank == 13:
            return f"King of {self.shape}"
        else:
            return f"{self.rank} of {self.shape}"

    @property
    def value(self):
        if self.rank > 10:
            return 10
        return self.rank


class Bundle():
    def __init__(self):
        self.bundle = []

    def fullDeck(self):
        shapes = ["Clubs", "Diamonds", "Hearts", "Spades"]
        for shape in shapes:
            for rank in range(1, 14):
                self.bundle.append(Card(rank, shape))

    def shuffle(self):
        random.shuffle(self.bundle)

    def add(self, cards):
        if type(cards) == list:
            for card in cards:
                self.bundle.append(card)
        else:
            self.bundle.append(cards)

    def getCard(self, number=1):
        cards = []
        for i in range(number):
            cards.append(self.bundle.pop(0))
        return cards




    @property
    def sum(self):
        sum = 0
        aceCount =0
      
        for card in self.bundle:
            if card.value == 1: 
                aceCount+=1
                sum += 11
            else:
                sum += card.value
        
        if sum>21:
            while aceCount>0:
                sum-=10
                aceCount-=1
        return sum

    

    def __str__(self):
        string = ""
        for card in self.bundle:
            string += str(card) + ", "
        return string

    def __sizeof__(self):
        return len(self.bundle)







#%%
# Returns Player, Dealer, fullBundle Cards, and Player Bet
def playerTurn():

    fullBundle = Bundle()
    dealerCards = Bundle()
    playerCards = Bundle()
    fullBundle.fullDeck()
    fullBundle.shuffle()
    dealerCards.add(fullBundle.getCard(2))
    playerCards.add(fullBundle.getCard(2))

    while True:
        printLine()
        print("Your Cards: {} \nYour Sum: {}".format(
            playerCards, playerCards.sum))
        print("Dealer Cards: {}, Hidden".format(dealerCards.bundle[0]))

        if playerCards.sum >= 21:
            break
        # Player wants to bet
        playerBank.placeBet()
        x = input("Press 1 for Hit, Press 2 for Stay\n(1/2):")

        # Player choose to Hit
        if x == "1" or x == "Hit":

            playerCards.add(fullBundle.getCard())
        else:
            break

    return fullBundle, dealerCards, playerCards


def dealerTurn(fullBundle, dealearCards):
    while dealearCards.sum < 17:
        dealearCards.add(fullBundle.getCard())
    return fullBundle, dealearCards


def play():
    fullBundle, dealerCards, playerCards = playerTurn()
    fullBundle, dealerCards = dealerTurn(fullBundle, dealerCards)
    printLine()
    print("Your Cards: {} \nYour Sum: {}".format(
        playerCards, playerCards.sum))
    print("Dealer Cards: {} \nDealer Sum: {}".format(
        dealerCards, dealerCards.sum))
    printLine()
    if playerCards.sum > 21:
        print("Burst!!!\nCasino Wins")
        playerBank.completeBet(False)
    elif dealerCards.sum > 21:
        print("You Win!!!")
        playerBank.completeBet(True)
    elif playerCards.sum == dealerCards.sum:
        print("Push. No one wins")
        playerBank.completeBet()
    elif playerCards.sum > dealerCards.sum:
        print("You Win!!!")
        playerBank.completeBet(True)
    elif dealerCards.sum > playerCards.sum:
        print("You Loose\nCasino Wins!!!")
        playerBank.completeBet(False)
    else:
        print(dealerCards, playerCards)


def clearConsole():
    import os

    def cls():
        os.system('cls' if os.name == 'nt' else 'clear')
    cls()


def main():

    
    playerBank.addMoney()
    while True:
        play()
        x = input("Do you want to play again.(Y/N):")
        if x.lower() == "y":
            clearConsole()
            continue
        else:
            break
    print("You can get your ${} at checkout.".format(playerBank.getBalance))
    print("\n\n---------------------\n Thank You :)\nCome Back Soon\n CodedBy:0001\n---------------------")
    printLine(2)
    x = input("Press any key to exit:")

if __name__ == '__main__':
    print("""Welcome to 0001 Casino
            BlackJack
    """)
    playerBank = Bank()
    main()
