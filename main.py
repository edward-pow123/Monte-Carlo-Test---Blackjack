import random
import xlsxwriter

#~~~~~~~~~~~~~~~~
#creating xlsx file

workbook = xlsxwriter.Workbook("results.xlsx")
worksheet = workbook.add_worksheet()

#adding headers
worksheet.write("A1", "Round Result")

worksheet.write("C1", "PLAYER1 DATA:")
worksheet.write("D1", "Bust")
worksheet.write("E1", "Cards Given")
worksheet.write("F1", "Total")
worksheet.write("G1", "Dealer")

worksheet.write("I1", "PLAYER2 DATA:")
worksheet.write("J1", "Bust")
worksheet.write("K1", "Cards Given")
worksheet.write("L1", "Total")
worksheet.write("M1", "Dealer")

indexer_i = 1

#~~~~~~~~~~~~~~~~~~ 
#initilising variables for player
class players:
    def __init__(self):
        self.cards_given = []
        self.deal = None
        self.win = None
        self.bust = False
        self.total = 0
        self.dealer = False

#~~~~~~~~~~
# defining total function
def play1_total(player1):
    player1.total = 0
    for card in player1.cards_given:
        player1.total += card
    return player1.total

def play2_total(player2):
    player2.total = 0 
    for card in player2.cards_given:
        player2.total += card
    return player2.total


def blackjack(worksheet, indexer_i):
    cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    player1 = players()
    player2 = players()

    #~~~~~~~~~~~
    #chooses dealer
    a = random.randint(1,2)
    if a == 1:
        player1.dealer = True
    else:
        player2.dealer = True

    #~~~~~~~~~~~~~~~~
    #gives both players 2 cards

    for b in range(2):
        a = random.randint(0, len(cards)-1)
        player1.cards_given.append(cards.pop(a))

    for c in range(2):
        a = random.randint(0, len(cards)-1)
        player2.cards_given.append(cards.pop(a))

    #~~~~~~~~~~~~~~~~~
    #checking total
    play1_total(player1)
    play2_total(player2)

    #~~~~~~~~~~~~~~~~
    #decides if players will hit or not

    if player1.total < 21 and player1.dealer != True:
        a = random.randint(0, 1)
        if a == 0:
            player1.deal = False
        if a == 1:
            player1.deal = True

    if player2.total < 21 and player2.dealer != True:       
        a = random.randint(0, 1)
        if a == 0:
            player2.deal = False
        if a == 1:
            player2.deal = True

    #if player is dealer they have to deal if they're total is 
    #under 16 they have to deal and cannot deal over 17

    if player1.dealer == True and player1.total < 16:
        while player1.total < 16:
            a = random.randint(0, len(cards)-1)
            player1.cards_given.append(cards.pop(a))
            play1_total(player1)

    if player2.dealer == True and player2.total < 16:
        while player2.total < 16:
            a = random.randint(0, len(cards)-1)
            player2.cards_given.append(cards.pop(a))
            play2_total(player2)

    if player1.dealer == True and player1.total ==17:
        a = random.randint(0, len(cards)-1)
        player1.cards_given.append(cards.pop(a))
        a = random.randint(0, 1)
        if a == 0:
            player1.deal = False
        if a == 1:
            player1.deal = True
        play1_total(player1)

    if player2.dealer == True and player2.total ==17:
        a = random.randint(0, len(cards)-1)
        player2.cards_given.append(cards.pop(a))
        a = random.randint(0, 1)
        if a == 0:
            player2.deal = False
        if a == 1:
            player2.deal = True
        play2_total(player2)

    #~~~~~~~~~~~~~~~~~
    #letting player hit if not over 21 until it decided they don't

    while player1.deal == True and player1.total <= 21 and player1.dealer == False:
        a = random.randint(0, len(cards)-1)
        player1.cards_given.append(cards.pop(a))
        a = random.randint(0, 1)
        if a == 0:
            player1.deal = False
            break
        if a == 1:
            player1.deal = True
        play1_total(player1)

    while player2.deal == True and player2.total <= 21 and player2.dealer == False:
        a = random.randint(0, len(cards)-1)
        player2.cards_given.append(cards.pop(a))
        a = random.randint(0, 1)
        if a == 0:
            player2.deal = False
            break
        if a == 1:
            player2.deal = True
        play2_total(player2)


    #~~~~~~~
    #checks if player is bust

    play1_total(player1)
    play2_total(player2)

    if player1.total > 21:
        player1.bust = True

    if player2.total > 21:
        player2.bust = True

    #~~~~~~~~~
    #checks who won

    if player1.bust == True and player2.bust == True:
        outcome = "no winners"

    elif player1.bust == True:
        outcome = "player 2 win"

    elif player2.bust == True:
        outcome = "player 1 win"

    elif player1.total > player2.total:
        outcome = "player 1 win"

    elif player2.total > player1.total:
        outcome = "player 2 win"

    else:
        outcome = "draw"

    #~~~~~~~~~~~~
    #writes to file

    with open("results.txt", "a") as f:
        f.write(f"PLAYER1 DATA: Bust = {player1.bust} | Cards Given = {player1.cards_given} | Total = {player1.total} | Dealer = {player1.dealer} \n")
        f.write(f"PLAYER2 DATA: Bust = {player2.bust} | Cards Given = {player2.cards_given} | Total = {player2.total} | Dealer = {player2.dealer} \n")
        f.write(f"ROUND RESULT: {outcome} \n")
        f.write("\n")

    #~~~~~~~~~~~~~
    # writes to xlsx index
    
    #writing round result
    worksheet.write(indexer_i, 0, outcome)

    #writing p1 data
    worksheet.write(indexer_i, 3, player1.bust)
    worksheet.write(indexer_i, 4, str(player1.cards_given))
    worksheet.write(indexer_i, 5, player1.total)
    worksheet.write(indexer_i, 6, player1.dealer)

    #writing p2 data
    worksheet.write(indexer_i, 9, player2.bust)
    worksheet.write(indexer_i, 10, str(player2.cards_given))
    worksheet.write(indexer_i, 11, player2.total)
    worksheet.write(indexer_i, 12, player2.dealer)

    indexer_i += 1

    return worksheet, indexer_i

for i in range(10):
    worksheet, indexer_i = blackjack(worksheet, indexer_i)
    

workbook.close()

print("Complete")

