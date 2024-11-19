from random import randint
import os
from playsound import playsound
import turtle as turtle

voice_activate = True

# START UP ------------------------------
# playsound('Welcome.mp3')
def menu():
    print("  ________      ___      .__   __.  ________   __  .______        ___      .______ \n"     
        " |       /     /   \     |  \ |  | |       /  |  | |   _  \      /   \     |   _  \    \n "
        "`---/  /     /  ^  \    |   \|  | `---/  /   |  | |  |_)  |    /  ^  \    |  |_)  |   \n "
        "   /  /     /  /_\  \   |  . `  |    /  /    |  | |   _  <    /  /_\  \   |      /    \n "
        "  /  /----./  _____  \  |  |\   |   /  /----.|  | |  |_)  |  /  _____  \  |  |\  \----. \n"
        "  /________/__/     \__\ |__| \__|  /________||__| |______/  /__/     \__\ | _| `._____| "
                                                                                           )
    # MENU --------------------------------------------
    playsound('Start_sound.mp3')
    print("_"*88)
    print(" "*41 + "MENU" + " "*41)
    # [|||||||||||||||||||||||||||||||||||||||]
    print(" "*7 + "Enter G to start Game" + " "*21 + "Enter R to read Rules" + " "*10)
    print(" "*7 + "Enter STOP to End program" + " "*17 + "Enter V to Activate/Deactivate Voice" + " "*10 )
    print(" "*49 + "Enter L to Hear Lore")
    print()

menu()

# MENU BUTTONS -------------------------------

while True:
    menu_button = input(">>> ")
    if menu_button == "R" or menu_button == "r":
        print("Instructions are being Loaded")
        os.system('Zanzibar_Rules.pdf')
        print("Instructions have Loaded")
        playsound("Zanzabar_Instructions.mp3")

    elif menu_button == "STOP":
        playsound('bye_game_end.mp3')
        break

    elif menu_button == "L" or menu_button == "l":
        print("Captain Zanzibar")
        playsound("LORE.mp3")
        pass

    elif menu_button == "V" or menu_button == "v":  # We turn on and off
        if voice_activate == True:
            voice_activate = False
            playsound('cant_science.mp3')
            print("flip u")

        elif voice_activate == False:
            voice_activate = True
            print("Voice Has been Actviated")

    elif menu_button == "G" or menu_button == "g":      #GAME
        print()

        # ----------------- GAME SET UP ------------------------------------------------

        # FILE FUNCTIONS ---------------------
        def create_score_board():
            with open("Zanzibar_Game__round_info.csv", "w") as round_score_file:
                round_score_file.write("\n" + "-" * 23 + "NEW GAME " + "-" * 23 + "\n")
                round_score_file.write(f"Round: Rolls/Chips, {'    , '.join(list_player_names)} ")
        def update_chips_scoreborde():
            with open("Zanzibar_Game__round_info.csv", "a") as round_score_file:
                chips_players = []
                for player in dictionary_user_player:
                    chips_players.append(str(dictionary_user_player[player][1]))
                round_score_file.write(f"\n{amount_of_rounds:<6} Chips      , {'       , '.join(chips_players):} ")


        # ------------- ITIALIZE ---------

        dictionary_user_player = {}
        list_players = []
        game_winner_list = []
        list_player_names = []
        roundscore = 0
        rounds_won = 0
        amount_of_rounds = 0
        # ------------- INPUTS ---------
        while True:
            try:
                chip_amount = int(input("Chip Amount: "))
                if chip_amount > 20:
                    playsound('more_than_20.mp3')
                if chip_amount == 20:
                    playsound('20_chips.mp3')
                if chip_amount < 20:
                    playsound('less_than_20.mp3')
                num_of_players = int(input("How many Players? "))
                break
            except:
                print("Invaild Input, Please Try again")

        # ------------- CREATE PLAYERS AND ADD INFO ---------
        for player_num in range(1, num_of_players + 1):
            player_name = input(f"Name of Player {player_num}: ")
            dictionary_user_player[f"player_{player_num}"] = [player_name, chip_amount, roundscore, rounds_won]
            list_players.append(f"player_{player_num}")
            list_player_names.append(player_name)

        initial_round_player = list_players[0]  # Make sure the frist player wil always be the initial round player

        create_score_board()
        update_chips_scoreborde()
        print("-"*88)
        print(
"   _____   _______              _____    _______      ____    ______      _____              __  __   ______  \n"
        "  / ____| |__   __|     /\     |  __ \  |__   __|    / __ \  |  ____|    / ____|     /\     |  \/  | |  ____| \n"
        " | (___      | |       /  \    | |__) |    | |      | |  | | | |__      | |  __     /  \    | \  / | | |__   \n"
        "  \___ \     | |      / /\ \   |  _  /     | |      | |  | | |  __|     | | |_ |   / /\ \   | |\/| | |  __| \n"
        "  ____) |    | |     / ____ \  | | \ \     | |      | |__| | | |        | |__| |  / ____ \  | |  | | | |___ \n"
        " |_____/     |_|    /_/    \_\ |_|  \_\    |_|       \____/  |_|         \_____| /_/    \_\ |_|  |_| |______| \n")

        # ------------------------ROUND LOOP------------------------------
        def run_victory(player_Name):
            screen = turtle.Screen()
            screen.bgcolor("navy")

            # Create a turtle object for txt
            text_turtle = turtle.Turtle()
            text_turtle.penup()
            text_turtle.color("white")
            text_turtle.goto(0, 0)

            text_turtle.write(f"WINNER WINNER\n{player_Name:^25}", align="center", font=("Times New Roman", 50, "bold"))

            # Create a turtle object for drawing the first cube
            cube_turtle = turtle.Turtle()
            cube_turtle.speed(0)  # Set the drawing speed to the maximum
            cube_turtle.penup()
            cube_turtle.color("white")
            cube_turtle.hideturtle()

            def draw_cube():
                cube_turtle.goto(-150, -50)  # Adjust the position of the cube
                cube_turtle.pendown()
                cube_turtle.begin_fill()
                for _ in range(4):
                    cube_turtle.forward(100)
                    cube_turtle.right(90)
                cube_turtle.end_fill()
                turtle.penup()
                turtle.goto(-100, -95)
                turtle.dot(10)
                turtle.goto(-100, -95)
                turtle.dot(10)
                turtle.penup()
                turtle.hideturtle()

            # Draw the cube
            draw_cube()

            # Create a turtle object for drawing the second cube
            cube_turtle = turtle.Turtle()
            cube_turtle.speed(0)  # Set the drawing speed to the maximum
            cube_turtle.penup()
            cube_turtle.color("white")
            cube_turtle.hideturtle()

            def draw_cube():
                cube_turtle.goto(10, -80)  # Adjust the position of the cube
                cube_turtle.pendown()
                cube_turtle.begin_fill()
                for _ in range(4):
                    cube_turtle.forward(100)
                    cube_turtle.right(90)
                cube_turtle.end_fill()
                turtle.penup()
                turtle.goto(40, -110)
                turtle.dot(10)
                turtle.goto(40, -110)
                turtle.dot(10)
                turtle.penup()
                turtle.goto(60, -130)
                turtle.dot(10)
                turtle.goto(60, -130)
                turtle.dot(10)
                turtle.penup()
                turtle.goto(80, -150)
                turtle.dot(10)
                turtle.goto(80, -150)
                turtle.dot(10)

            # Draw the cube
            draw_cube()

            # Cool graphic
            t = turtle.Turtle()
            t.speed(0)
            t.penup()
            t.goto(0, 200)
            t.pendown()
            colors = ['red', 'pink']
            for num in range(100):
                t.forward(num + 1)
                t.right(109)
                t.pencolor(colors[num % 2])

            turtle.exitonclick()
        def create_round_turn_order(initial_round_player):
            turn_order_list = []  # Itilziae
            num_of_players = len(list_players)  # Get the number of players

            player_name_split = initial_round_player.split("_")  # Get the number from the player string "player_2"
            starting_index = int(player_name_split[1]) - 1  # by spliting the string into 2 parts

            # print("The original list is : " + str(list_players))  # DeBug Show the Starting List

            for i in range(num_of_players):
                turn_order_list.append(list_players[starting_index % num_of_players])
                starting_index = starting_index + 1

            # print(f"The Cureent Round list is : {turn_order_list}")        # Debug to show Output
            return turn_order_list
        def has_anyone_won_game():
            """"""

            for player_num in range(1, num_of_players + 1):
                if dictionary_user_player[f'player_{player_num}'][1] <= 0:  # This means at least one player has won
                    return True
            return False
        def roll_display(dice_list):
            my_list = []
            for num in dice_list:
                if num == 1:
                    my_list.append(
"""
.______________.
|              |
|              |
|      ()      |
|              |
|______________|""".split("\n"))

                if num == 2:
                    my_list.append(
"""
.______________.
|              |
|   ()         |
|              |
|         ()   |
|______________|""".split("\n"))

                if num == 3:
                    my_list.append(
"""
.______________.
|              |
|   ()         |
|      ()      |
|         ()   |
|______________|""".split("\n"))

                if num == 4:
                    my_list.append(
"""
.______________.
|              |
|   ()    ()   |
|              |
|   ()    ()   |
|______________|""".split("\n"))

                if num == 5:
                    my_list.append(
"""
.______________.
|              |
|  ()      ()  |
|      ()      |
|  ()      ()  |
|______________|""".split("\n"))

                if num == 6:
                    my_list.append(
"""
.______________.
|              |
|  ()      ()  |
|  ()      ()  |
|  ()      ()  |
|______________|""".split("\n"))

            for row in zip(my_list[0], my_list[1], my_list[2]):
                print(row[0] + "   " + row[1] + "   " + row[2])
        def points_total_roll_value(player_dice_roll):
            """"All other combinations rank as a sum of the three dice added together:
            THE POINT TOTAL HIERARCY
            1 = 100 points
            6 = 60 points
            2 = 2 points
            3 = 3 points
            4 = 4 points
            5 = 5 points
            """
            total_points = 0
            for index, value in enumerate(player_dice_roll):
                if value == 1:
                    total_points += 100
                elif value == 6:
                    total_points += 60
                else:
                    total_points += value
            return total_points
        def dice_list__to__value(player_dice_roll):
            playsound('dice.mp3')
            one_two_three = [1, 2, 3]
            zanzaibar = [4, 5, 6]

            player_dice_roll.sort()
            print()
            if player_dice_roll == zanzaibar:
                playsound('Zan.mp3')            #FIXME: MAKE MULTIPROCESS playsound & print
                print(f"ZANZABAR!!!! {zanzaibar}")
                dice_value = 4000

            elif player_dice_roll[0] == player_dice_roll[1] == player_dice_roll[2]:
                playsound('Specia_Roll_Sound.mp3')
                playsound('three_of_kind.mp3')
                print(f"THREE OF A KIND!!!! {player_dice_roll}")
                dice_value = 3000 + (player_dice_roll[0])

            elif player_dice_roll == one_two_three:
                playsound('Specia_Roll_Sound.mp3')
                print(f" You got [1,2,3] !!!")
                dice_value = 2000

            else:
                playsound('worst_roll.mp3')
                print(f"Points Total: {player_dice_roll} = {points_total_roll_value(player_dice_roll)} points")
                dice_value = 1000 + (points_total_roll_value(player_dice_roll))

            # print(f"DICE VALUE IS: {dice_value}")
            return dice_value
        def rng():
            """Retun a list of 3 random numbers from 1 to 6"""
            roll = []
            roll.append(randint(1, 6))
            roll.append(randint(1, 6))
            roll.append(randint(1, 6))
            roll_display(roll)
            return roll
        def initial_player_turn(player):
            intial_roll_counter = 0
            global max_roll

            input("Press Enter to Roll")
            intial_roll_counter += 1

            # print("intial_roll_counter:", intial_roll_counter)  # DEBUG: to show the intial_roll_counter number
            current_dice_roll_value = dice_list__to__value(rng())  # Does RNG and SHow Value and Points

            while intial_roll_counter < 3:
                print(f"You have {3 - intial_roll_counter} re-rolls left")
                reroll_yes_no = input("    Do you want to Reroll? (Y/N) \n"
                                      "    >>> ")  # YES BUTTON

                if reroll_yes_no == "N" or reroll_yes_no == "n" or reroll_yes_no == "no" or reroll_yes_no == "No":
                    break
                # if Yes:

                intial_roll_counter += 1
                # print("intial_roll_counter:", intial_roll_counter)
                current_dice_roll_value = dice_list__to__value(rng())

            dictionary_user_player[player][2] = current_dice_roll_value
            max_roll = intial_roll_counter
        def next_player_turn(player):
            player_roll_counter = 0
            global max_roll

            input("Press Enter to Roll")
            player_roll_counter += 1

            # print("intial_roll_counter:", player_roll_counter)  # DEBUG: to show the intial_roll_counter number
            current_dice_roll_value = dice_list__to__value(rng())  # Does RNG and SHow Value and Points

            while player_roll_counter < max_roll:
                reroll_yes_no = input("    Do you want to Reroll? (Y/N) \n"
                                      "    >>> ")  # YES BUTTON
                if reroll_yes_no == "N" or reroll_yes_no == "n" or reroll_yes_no == "no" or reroll_yes_no == "No":
                    break


                player_roll_counter += 1

                # print("intial_roll_counter:", player_roll_counter)  # DEBUG: to show the intial_roll_counter number
                current_dice_roll_value = dice_list__to__value(rng())

            dictionary_user_player[player][2] = current_dice_roll_value
        def determine_round_winner():
            round_scores_dict = {}
            round_winners = []
            for i in range(1, num_of_players + 1):
                player = f'player_{i}'
                round_scores_dict[player] = dictionary_user_player[player][2]
            round_winner = max(round_scores_dict, key=lambda x: round_scores_dict[x])

            for i in range(1, num_of_players + 1):
                if round_scores_dict[f'player_{i}'] == round_scores_dict[round_winner]:
                    round_winners.append(f'player_{i}')

            for i in range(len(round_winners)):
                a = round_winners[i]
                dictionary_user_player[a][3] += 1

            return round_winners
        def print_round_winner_names(list_of_round_winners):
            list_of_round_winner_names = []
            for player in list_of_round_winners:
                list_of_round_winner_names.append(dictionary_user_player[player][0]) # Find all Player names

            if len(list_of_round_winner_names) > 1:
                print(f"Round Winners are: {', '.join(list_of_round_winner_names)}")

            else:
                print(f"Round Winner is: {list_of_round_winner_names[0]}")
        def print_round_loser_names(list_of_round_losers):
            list_of_round_loser_names = []
            for player in list_of_round_losers:
                list_of_round_loser_names.append(dictionary_user_player[player][0]) # Find all Player names

            if len(list_of_round_loser_names) > 1:
                print(f"Round Losers are: {', '.join(list_of_round_loser_names)}")

            else:
                print(f"Round loser is: {list_of_round_loser_names[0]}")
        def determine_round_loser():
            round_scores_dict = {}
            round_losers = []
            for i in range(1, num_of_players + 1):
                player = f'player_{i}'
                round_scores_dict[player] = dictionary_user_player[player][2]
            round_loser = min(round_scores_dict, key=lambda x: round_scores_dict[x])

            for i in range(1, num_of_players + 1):
                if round_scores_dict[f'player_{i}'] == round_scores_dict[round_loser]:
                    round_losers.append(f'player_{i}')

            # print("Round losers are:", round_losers)
            # print(dictionary_user_player)       #DEBUG

            return round_losers
        def chip_distribution(round_winner_list, round_losers_list):
            """
            Title: chip_distrubion

            Parameters: round winner string, round loser string
            example1: ["player_1"], ["player_2"]
            example2: ["player_2"], ["player_4","player_1"]
            example3: ["player_4","player_1"], ["player_2"]

            Output: edit dictionary (view round score, and change each players chip amount)
            Description: A loop that finds the round winner's(if mutiple they have have the
            same round_score so look at the frist one in the list) dictionary_user_player,
            takes their round_score, and finds out the chips need to move by round_score//1000.
            Then take that amount of chips from non-losers and give them to the round losers.
            Also acounting for mutiple losers, and  acount for no losers by giveing out no chips.
            """

            round_winner_player = round_winner_list[0]  # Floor divide to get frist digit
            chip_amount = int((dictionary_user_player[round_winner_player][2]) // 1000)  # without the int, we have 3.0
            print(f"Moveing {chip_amount} chip(s) from Non_losers to Losers")  # DEBUG - Remove latter

            non_loser_list = []  # Create list

            # CREATE NOLOSER LIST ----------------------------------------------------
            for player in list_players:  # We look at each player in the game
                if not (player in round_losers_list):  # And if it isnt a loser
                    non_loser_list.append(player)  # We add them to the loser list

            # print(non_loser_list)    #DEBUG - Remove latter

            # TAKE CHIPS FROM NON-LOSERS ---------------------------
            for player in non_loser_list:
                dictionary_user_player[player][1] -= chip_amount * len(round_losers_list)  # Incase we have mutiple losers

            # GIVE CHIPS TO LOSSERS ----------------------------- Loser says what...
            for player in round_losers_list:
                dictionary_user_player[player][1] += chip_amount * len(non_loser_list)  # We give chips from each player
        def game_winner___Tie_Breaker(prama_winner_list):
            """We find the winner of a tie by seeing if a player got
            rid of all thier chips 'fist', which means if they went into
            negtive chips.

            We find the least chips (negtive chips too)

            if 2 players have the same amout of least chips, we then cheack who had the most round wins
            """
            rounds_won_dict = {}
            same_chip_player_list = []
            chip_list = []

            for player in prama_winner_list:
                chip_list.append(dictionary_user_player[player][1])
            min_chip = min(chip_list)

            for player in prama_winner_list:
                if dictionary_user_player[player][1] == min_chip:
                    same_chip_player_list.append(player)

            if len(same_chip_player_list) > 1:  # If we got more then one player that is in the mins
                for player in same_chip_player_list:
                    rounds_won_dict[player] = dictionary_user_player[player][3]
                winner_name = max(rounds_won_dict, key=lambda x: rounds_won_dict[x])

            else:
                winner_name = same_chip_player_list[0]

            return winner_name


        while not has_anyone_won_game():
            amount_of_rounds += 1
            print("\n" + "-"*40 + f' ROUND {amount_of_rounds} ' + "-"*40)

            round_list = create_round_turn_order(initial_round_player)
            player_names = []    # Reset it per round

            for player in round_list:
                player_names.append(f"{dictionary_user_player[player][0]}")  # Turn Player Names to

            print(f"ROUND {amount_of_rounds}'s Turn Order:" + " "*24, " --> ".join(player_names))
            print()
            for index, player in enumerate(round_list):
                if index == 0:
                    print(f"---------------------------- FRIST PLAYER IS: {dictionary_user_player[player][0]}")
                    initial_player_turn(player)

                else:
                    print(f"\n---------------------------- NEXT PLAYER IS: {dictionary_user_player[player][0]}")
                    next_player_turn(player)

            round_winners = determine_round_winner()  # Find Round winners
            print("\n" + "-"*30 + f" Round {amount_of_rounds} is Over " + "-"*30)  # DEBUG

            print_round_winner_names(round_winners)


            initial_round_player = round_winners[0]  # Getg the intail player, frist winner found by system
            round_losers = determine_round_loser()  # Find Round loser
            print_round_loser_names(round_losers)

            chip_distribution(round_winners, round_losers)  # Hand out chips

            update_chips_scoreborde()
            # print("\n######### Everyone Has had their turn #######")  # DEBUG

        game_is_over = "GAME IS OVER"
        print("##########################################################################\n"
              f"{game_is_over:^68}")

        # ------------------------ GAME SET DOWN ------------------------------

        for player in list_players:
            if dictionary_user_player[player][1] <= 0:  # Chekc each players chip amount and if they got equal or less then 0 they are considred a winner
                game_winner_list.append(player)

        game_winner_player_name = dictionary_user_player[game_winner___Tie_Breaker(game_winner_list)][0]   # We choose a random person in the winner list

        print(f"THE GAME WINNER IS: {game_winner_player_name}")

        run_victory(game_winner_player_name)
        playsound("win_sound.mp3")
        print("\n\n")
        menu()

    else:                                           # This is wreid but it for the starting input
        print("Invaild Input, Please Try again")
        playsound('invalid_input.mp3')