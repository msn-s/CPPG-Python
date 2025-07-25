#------------------------------------------------------------------
# Author: Mason Hilder
# Date: July 22nd, 2025
# Purpose: A program that allows users to purchase lottery tickets
# as well as select certain options within the main menu of the lottery
#------------------------------------------------------------------

#region IMPORTS
import random
#endregion

#region DECLARATIONS
WELCOME_MESSAGE = '''Welcome To the big 7 lottery!'''
PAYOUT_TABLE = '''
--------------------------------------------
Matching	Prize Payout	 Odds of Winning
7 of 7	    85%	             1 in 33,294,800
6 of 7	    5%	             1 in 113,248
5 of 7	    5%	             1 in 1,841
4 of 7	    $20	             1 in 82.9
3 of 7	    $5 (free ticket) 1 in 8.5
--------------------------------------------
'''
MENU  = '''
--------------------------------------------------------
1. Purchase ticket(s)
2. Display ticket(s)
3. Winning numbers menu
4. Enter tickets sold (in millions, e.g "5" = 5 Miliion)
5. Print out winnings chart
6. Check for winning tickets
7. Exit program
--------------------------------------------------------
\n
'''
MIN_OPTION = 1
MAX_OPTION = 7
MIN_TICKETS = 1
MAX_TICKETS = 3
MIN_TICKET_NUMBER = 1
MAX_TICKET_NUMBER = 50

used_numbers = []
winning_numbers = []
ticket_one = []
ticket_two = []
ticket_three = []
prize_pool = 500000
tickets_sold = 5000000
doContinue = True

#endregion

#region FUNCTIONS
def mainMenu():
    '''A function that prints main menu and requires user input for next step'''
    isValid = False
    print(MENU)
    while not isValid:
        try:
            user_input = int(input("Select an option: ").strip())
            
            if MIN_OPTION <= user_input <= MAX_OPTION:
                isValid = True
                return user_input
            
            else:
                print("Option not in valid range")            
        
        except ValueError as v:
            print("Input must be an integer")


def drawTable(): 
    '''Draws the payout table'''
    print(PAYOUT_TABLE)   

def getTicketAmount():
    ''' Get amount of tickets from user'''
    isValid = False
    while not isValid:
        try:
            tickets = int(input("How many tickets would you like? (1-3): ").strip())
            
            if MIN_OPTION <= tickets <= MAX_OPTION:
                isValid = True
                return tickets
            
            else:
                print("Option not in valid range")            
        
        except ValueError as v:
            print("Input must be an integer")

def menuSelect(option):
    if option == 1:
        yes_no = input("Would you like your first set of 7 numbers to be selected automatically? (y/n)").strip().lower()
        
        if yes_no == "y":
            tickets = getTicketAmount()
            drawn_tickets = drawLotto(tickets)
            for ticket in drawn_tickets:
                ticket_one.append(ticket)
        
        
        elif yes_no == "n":  
            selected_tickets = pickLotto()   
            
            for ticket in selected_tickets:
                ticket_one.append(ticket)
        else:
            print("Invalid, must be (y/n)")


    elif option == 2:
        
        print(ticket_one)
        print(ticket_two)
        print(ticket_three)

        pass

    elif option == 3:

        pass

    elif option == 4:

        pass

    elif option == 5:

        drawTable()

    elif option == 6:

        pass 
    
    elif option == 7:

        print("Succesfully exited program")
        exit()


def pickLotto():
    '''A function that allows the user to manually pick their first set of 7 numbers for their lotto ticket.'''
    print("\nEnter your numbers one by one below (No repeats) ")
    ticket_holder = []
    current_ticket = 1
    try:
        while len(ticket_holder) < 7:
            ticket = int(input("Number %s: " % (current_ticket)).strip())
            if MIN_TICKET_NUMBER <= ticket <= MAX_TICKET_NUMBER:
                if ticket in ticket_holder:
                    print("No repeats allowed \n")
                else:
                    ticket_holder.append(ticket)
                    current_ticket += 1
            else:
                print("Number must be between 1-50!")
    except ValueError:
        print("Must enter integer (1-50)")

    return ticket_holder



def drawLotto(tickets):
    '''A function that draws random numbers (1-50, no repeats) and checks to make sure it does not draw any already used numbers'''
    global ticket_one
    for i in range(tickets):
        lotto_tickets = random.sample(range(1, 51), 7)
        return lotto_tickets

def calculateWinnings():
    '''A function that compares users tickets to winning numbers, calculats prize money based on matching numbers '''
    pass
#endregion

#region MAIN LOOP
while doContinue:
    option = mainMenu()
    menuSelect(option)
