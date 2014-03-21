__author__ = 'Kim Vitaly 13-ICT'
from random import randint

def random_card():
    return randint(2,12)

my_money = 10
n_round = 1
answer = 'y'

while answer == 'y' and my_money > 0:
    str_money = str(my_money)
    dealer_cards = 0
    my_cards = 0
    ask = ''
    ask_d = ''
    rate = 0

    while rate <= 0 or rate > my_money:
        rate = int(raw_input("Choose rate between 1 and " + str_money + " dollars:  "))
    my_money -= rate

    print
    print "Game: Start"
    print "Round %d" %n_round
    print

    dealer_cards += random_card()
    my_cards += random_card()
    dealer_cards += random_card()
    my_cards += random_card()

    print "Your cards: %d" %(my_cards)
    print "Dealer's cards: %d" %(dealer_cards)
    print

    while my_cards < 21:
        while ask != 'y' and ask != "n":
            ask = raw_input('Do you want one more card?: (y/n)  ')
        if ask == 'y':
            my_cards += random_card()
            print "Now your cards: %d" %(my_cards)
            ask = ''
        else:
            break

    print

    if dealer_cards < my_cards and my_cards < 21:
        while dealer_cards < 21:
            while ask_d != 'y' and ask_d != "n":
                ask_d = raw_input('Does DEALER want one more card?: (y/n)  ')
            if ask_d == 'y':
                dealer_cards += random_card()
                print "Now dealer's cards: %d" %(dealer_cards)
                ask_d = ''
            else:
                break

    print

    if my_cards == 21:
        print "How lucky you are! You won %d $." % rate
        my_money += rate * 2
        print "Now you have %d $" %(my_money)
    elif my_cards > dealer_cards and my_cards < 21 :
        print 'You Won! Congrats, here\'s your %d $.' % rate
        my_money += rate * 2
        print "Now you have %d $" %(my_money)
    elif dealer_cards > 21:
        print 'You Won! Congrats, here\'s your %d $.' % rate
        my_money += rate * 2
        print "Now you have %d $" %(my_money)
    else:
        print 'You lose, Sad to be you :(. Now you have only %d $' %(my_money)

    n_round += 1
    print
    if my_money == 0:
        print "Sorry, you bankrupt. You can not continue the game"
        print
        print "Credits:"
        print "Made by %s" % __author__
    else:
        answer = raw_input("Do you want to play one more time? (y/n)  ")
        if answer == 'n':
            print "Ok, have a nice day :)"
            print
            print "Credits:"
            print "Made by %s" % __author__
        else:
            print "Here we go again!"
            print