# In this implementation a card (that is not a 10) is represented
# by a 2 character string, where the 1st character represents a rank and the 2nd a suit.
# Each card of rank 10 is represented as a 3 character string, first two are the rank and the 3rd is a suit.

# Family name: xxxxxx 
# Student number: xxxxxx
# Course: IT1 1120 
# Assignment Number 4, Part 1


import random

def wait_for_player():
    '''()->None
    Pauses the program until the user presses enter
    '''
    try:
         input("\nPress enter to continue. ")
         print()
    except SyntaxError:
         pass


def make_deck():
    '''()->list of str
        Returns a list of strings representing the playing deck,
        with one queen missing.
    '''
    deck=[]
    suits = ['\u2660', '\u2661', '\u2662', '\u2663']
    ranks = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']
    for suit in suits:
        for rank in ranks:
            deck.append(rank+suit)
    deck.remove('Q\u2663') # remove a queen as the game requires
    return deck

def shuffle_deck(deck):
    '''(list of str)->None
       Shuffles the given list of strings representing the playing deck    
    '''
    random.shuffle(deck)

#####################################

def deal_cards(deck):
    '''(list of str)-> tuple of (list of str,list of str)

    Returns two lists representing two decks that are obtained
    after the dealer deals the cards from the given deck.
    The first list represents dealer's i.e. computer's deck
    and the second represents the other player's i.e user's list.
    '''
    dealer=[]
    other=[]

     # COMPLETE THE BODY OF THIS FUNCTION ACCORDING TO THE DESCRIPTION ABOVE
     # YOUR CODE GOES HERE
    for i in range(len(deck)):
        if i % 2 == 0:
            dealer.append(deck[i])
        else:
            other.append(deck[i])
            
    return (dealer, other)
 


def remove_pairs(l):
    '''
     (list of str)->list of str

     Returns a copy of list l where all the pairs from l are removed AND
     the elements of the new list shuffled

     Precondition: elements of l are cards represented as strings described above

     Testing:
     Note that for the individual calls below, the function should
     return the displayed list but not necessarily in the order given in the examples.

     >>> remove_pairs(['9♠', '5♠', 'K♢', 'A♣', 'K♣', 'K♡', '2♠', 'Q♠', 'K♠', 'Q♢', 'J♠', 'A♡', '4♣', '5♣', '7♡', 'A♠', '10♣', 'Q♡', '8♡', '9♢', '10♢', 'J♡', '10♡', 'J♣', '3♡'])
     ['10♣', '2♠', '3♡', '4♣', '7♡', '8♡', 'A♣', 'J♣', 'Q♢'])
     >>> remove_pairs(['10♣', '2♣', '5♢', '6♣', '9♣', 'A♢', '10♢'])
     ['2♣', '5♢', '6♣', '9♣', 'A♢']
    '''

    no_pairs=[]
    l.sort()
    i=0
    while i<len(l):
        if i==len(l)-1 or l[i][-2: :-1] != l[i+1][-2: :-1]:
            no_pairs.append(l[i])
            i+=1
        else:
            i+=2
    random.shuffle(no_pairs)
    return no_pairs



def print_deck(deck):
    '''
    (list)-None
    Prints elements of a given list deck separated by a space
    '''
    for element in deck:
        print(element, end=' ')
    print()

    # COMPLETE THE BODY OF THIS FUNCTION ACCORDING TO THE DESCRIPTION ABOVE
    # YOUR CODE GOES HERE

    
def get_valid_input(n):
    '''
    (int)->int
    Returns an integer given by the user that is at least 1 and at most n.
    Keeps on asking for valid input as long as the user gives integer outside of the range [1,n]
     
    Precondition: n>=1
    '''
    # COMPLETE THE BODY OF THIS FUNCTION ACCORDING TO THE DESCRIPTION ABOVE
    # YOUR CODE GOES HERE
   
    flag=True
    question = int(input("Give a number between 1 and "+str(n)+": "))
    while flag:
        if 1<=question<=n:
            flag=False
        else:
            question=int(input("Invalid number. Please enter a number between 1 and "+str(n)+" :"))
    return question 

       
def numeric(userInput):
    if userInput==1:
        x='st'
    elif userInput==2:
        x='nd'
    elif userInput==3:
        x='rd'
    elif userInput>3:
        x='th'
    return(str(userInput)+x)            
     

def play_game():
    '''()->None
    This function plays the game'''
        
    deck=make_deck()
    shuffle_deck(deck)
    tmp=deal_cards(deck)

    dealer=tmp[0]
    human=tmp[1]

    print("Hello. My name is Robot and I am the dealer.")
    print("Welcome to my card game!")
    print("Your current deck of cards is: \n")
    # printing human's deck 
    print_deck(human)
    #print_deck(dealer)
    print("\nDo not worry. I cannot see the order of your cards")
    print("Now discard all the pairs from your deck. I will do the same.")
    wait_for_player()
    print("*"*59)    
    dealer=remove_pairs(dealer)    
    human=remove_pairs(human)    
     
    flag=0   
    while len(dealer) >= 1 and len(human) >= 1:
            # hyman's turn 
        if flag%2==0:        
            print("Your turn.\n")
            print("Your current deck of cards is: \n")
            print(' '.join(human))  
            print("\nI have ",len(dealer),"cards. If 1 stands for my first card and")
            print(len(dealer),"for my last card, which of my cards would you like?")
            userInput = get_valid_input(len(dealer))
            print("You asked for my "+numeric(userInput)+" card.")
            print("Here it is. It is ",dealer[userInput-1],"\n")
            print("With ",dealer[userInput-1]," added, your current deck of cards is: \n")
            human.append(dealer[userInput-1]) 
            print(' '.join(human),'\n') 
            dealer.remove(dealer[userInput-1])
            print("And after discarding pairs and shuffling, your deck is: \n")
            human=remove_pairs(human)
            print(' '.join(human),'\n')
            wait_for_player()
            print("*"*59)
            flag+=1

            # robots's turn 
        elif flag%2!=0 :
            print("My turn\n")
            rand_int = random.randint(1,(len(human)))
            print("I took your "+numeric(rand_int)+" card")
            # add card from dealer
            dealer.append(human[(rand_int-1)])
            # remove card from human
            human.remove(human[(rand_int-1)])
            human=remove_pairs(human)
            dealer=remove_pairs(dealer)
            wait_for_player()                    
            print("*"*59)
            flag+=1
            
        if (len(human)==0): 
             flag=False
             print('''Ups. You do not have any more cards
Congratulations! You, Human, win''')
        elif (len(dealer)==0): 
             flag=False
             print('''Ups. I do not have any more cards
You lost! I, Robot, win''')
              

# main
play_game()



