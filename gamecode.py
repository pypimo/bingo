# Multiplayer bingo

import random

stop = 0

while (not stop) :

    print("""\n
    ****************************
    Players please pay attention
    Rules for the game: 
    1) Until someone gets a bingo, random numbers in columns(B, I, N, G, O) will be generated
    2) Each player will be asked to type Yes or No to ask if the number is in their Bingo Card
    3) The middle most space is the free space in the card
    4) If any user get all the numbers in a diagonal, row or column, type "BINGO" after entering the row number
    5) The first user to do so Wins (of course we will ensure there's no cheating ;-)
    Let's begin
    ****************************""")
    print()

    num = int(input("Enter number of players: "))
    print()

    names = {}

    for i in range(1, num+1):
        print("Player", i)
        name = input("Enter your name here: ")
        names[i] = name
        print()
    
    # Making Bingo Cards

    # Dictionary for storing cards for each player
    all_cards = {}
    # Player Number
    player=1
    
    while (player<=num) :
        card = []

        # Separate columns as list
        B = random.sample(range(1, 16), 5)
        I = random.sample(range(16, 31), 5)
        N = random.sample(range(31, 46), 4)
        G = random.sample(range(46, 61), 5)
        O = random.sample(range(61, 76), 5)

        # Free space at the middle
        N.insert(2, "FS") # FS for free space 

        # A single card with 5 columns
        card.append(B)
        card.append(I)
        card.append(N)
        card.append(G)
        card.append(O)

        #displays cards
        #print(card)

        columns = ["B", "I", "N", "G", "O"]
        all_cards[player]=card
        player+=1


    # Calling bingo numbers
    bingo = 0
    
    # Game begins
    play = {}
    for i in range(1, num+1):
        play[i] = []
    check = []
    available_choices = { "B" : (1, 15), "I" : (16, 30), "N" : (31, 45), "G" :(46, 60), "O" : (61, 75) }
    letters = ["B", "I", "N", "G", "O"]

    # game begins
    while (not bingo):

        #displaying cards to users
        player=0
        print()
        print("Cards of all players\n")
        
        while player < num:
            player+=1

            print("***", "Player", player, names[player], "Card", "***")
            print("   B   I   N   G   O")
            for i in range(5):
                print(i+1, end = "  ")
                for j in range(5):
                    #ensures equal spacing in output
                    space = "  " if len(str(all_cards[player][j][i])) == 2 else "   "
                    if all_cards[player][j][i] in play[player]:
                        print(all_cards[player][j][i], end ="")
                        space = " " if len(str(all_cards[player][j][i])) == 2 else "  "
                        print("|", end=space)
                    else:
                        print(all_cards[player][j][i], end=space)
                print()
            print()

        # selecting numbers for Call
        letter = random.choice(letters)
        number = random.randint(available_choices[letter][0], available_choices[letter][1])

        # so that only distinct numbers are selected
        total_counts = 0
        while (number in check) :
            total_counts += 1
            if (total_counts % 15 == 0):
                letter = random.choice(letters)
            number = random.randint(available_choices[letter][0], available_choices[letter][1])
        else:
            check.append(number)

        # user interaction
        print("\n** Call --> column:", letter, "number:", number, "**")

        for i in range(1, num+1):
            print()
            print("Player", i, names[i])
            verdict = input("Is the number given in your card in the specified column? (Y: Yes/N: No): ")

            nxt_player = 0
            while (verdict == "Y" and nxt_player==0):
                user_row = int(input("Enter the row number[1, 2, 3, 4, 5] where the number is: "))

                if (all_cards[i][letters.index(letter)][user_row-1] == number) :
                    play[i].append(number)
                    bingo = input("This is the place to enter 'BINGO' the moment you get it!: ")

                    #ensuring correct play
                    if bingo=="BINGO":
                        cnfrmd = 0
                        
                        #checking columns
                        is_freespace = 0
                        for col in range(5):
                            l = []
                            for row in range(5):
                                if (all_cards[i][col][row] != "FS"):
                                    l.append(all_cards[i][col][row])
                                else:
                                    is_freespace = 1

                            flag = 1
                            for member in l:
                                if i not in check:
                                    flag = 0
                                    break 

                            if (flag)and ( (is_freespace==1 and len(l)==4) or (is_freespace==0 and len(l)==5) ):
                                cnfrmd = 1

                            if (cnfrmd):
                                break
                                
                        # checking rows
                        if (not cnfrmd):
                            is_freespace = 0
                            for row in range(5):
                                l = []
                                for col in range(5):
                                    if all_cards[i][col][row] != "FS":
                                        l.append(all_cards[i][col][row])
                                    else:
                                        is_freespace = 1

                                flag = 1
                                for member in l:
                                    if member not in check:
                                        flag = 0
                                        break 

                                if (flag)and ( (is_freespace==1 and len(l)==4) or (is_freespace==0 and len(l)==5) ):
                                    cnfrmd = 1
                                if (cnfrmd):
                                    break 
                        
                        # checking diagonal 1
                        if (not cnfrmd):
                            is_freespace = 0
                            for row in range(5):
                                l = []
                                for col in range(5):
                                    if (row==col and all_cards[i][col][row] != "FS"):
                                        l.append(all_cards[i][col][row])
                                    else:
                                        is_freespace = 1

                                flag = 1
                                for member in l:
                                    if member not in check:
                                        flag = 0
                                        break 

                                    if (flag)and ( (is_freespace==1 and len(l)==4) or (is_freespace==0 and len(l)==5) ):
                                        cnfrmd = 1

                                    if (cnfrmd):
                                        break   

                        #checking diagonal 2
                        if (not cnfrmd):
                            is_freespace = 0
                            for row in range(5, -1):
                                l = []
                                for col in range(5):
                                    if (row+col==6 and all_cards[i][col][row]!="FS"):
                                        l.append(all_cards[i][col][row])
                                    else:
                                        is_freespace = 0

                                flag = 1
                                for member in l:
                                    if member not in check:
                                        flag = 0
                                        break 

                                if (flag)and ( (is_freespace==1 and len(l)==4) or (is_freespace==0 and len(l)==5) ):
                                    cnfrmd = 1

                                if (cnfrmd):
                                    break  

                        # chkd
                        if (cnfrmd == 1):
                            bingo = 1
                            print("Congratulations Player", name[i], "! You did a great job!! \nIt was really interesting but then one of you won (⌣̩̩́_⌣̩̩̀) \nThank you for playing, see you again :D""")
                            stop = int(input("If you want to play again enter 0 else 1: "))
                        else:
                            print("Hey, that isn't correct, there's no 'BINGO' yet!")
                            bingo = 0
                            nxt_player = 1
                    else:
                        nxt_player = 1
                else:
                    print("Hmm, that doesn't seem correct; check again")
                    verdict = input("If number not in your card enter 'N' else 'Y': ")       
