import random
from re import A
import time
import os
from battleshipai import *

def place_boats():
    ''' () -> list
    Generates a grid with boats placed at random coordinates horizontally or vertically.
    '''
    grid = [[" ", " ", " ", " ", " "], [" ", " ", " ", " ", " "], [" ", " ", " ", " ", " "], [" ", " ", " ", " ", " "], [" ", " ", " ", " ", " "]] 
    boats_and_lengths = [1, 2, 3] #Number of boats, each of increasing lengths
    for boat in boats_and_lengths:
        row_num = random.randint(0,4)
        column_num = random.randint(0,4)
        direction = random.randint(1,2) #If direction = 1, the boat is placed horizontal, if direction = 2, the boat is placed vertical
        
        if direction == 1:
            while column_num + boat > 4: #Checks if the boat can fit on the board at the specified coordinate
                column_num = random.randint(0,4) #If the above is true, the boat will be placed in a new column
            
            for i in range(boat): #Checks if there is already a boat placed at the coordinates
                    if grid[row_num][column_num+i] != "#":
                        continue
                    else:
                        row_num = random.randint(0,4) #Choose a different row to place the boat if the above is true
            for i in range(boat): #Places the boat, which is represented by "#"
                grid[row_num][column_num+i] = "#"
            
        if direction == 2: 
            while row_num + boat > 4: 
                row_num = random.randint(0,4) #If the above is true, the boat will be placed in a new row
            
            for i in range(boat): 
                    if grid[row_num+i][column_num] != "#":
                        continue
                    else:
                        column_num = random.randint(0,4) #Chooses a different column to place the boat if the above is true
            for i in range(boat):
                grid[row_num+i][column_num] = "#"
    return grid


def show_grid(grid):
    ''' (list) -> None
    Takes a nested list with elements representing different markings of the game and prints out a proper, labelled grid.
    '''
    player_field = "  12345\n" #Creates the top coordinates for the grid
    for index, row in enumerate(grid): #Creates a blank grid with letter coordinates on the lefthand side
        if index == 0:
            player_field += ("A" + "|")
        if index == 1:
            player_field += ("B" + "|")
        if index == 2:
            player_field += ("C" + "|")
        if index == 3:
            player_field += ("D" + "|")
        if index == 4:
            player_field += ("E" + "|")
        
        for spot in row: #Prints out a grid with markings representing the boats and hits
            if spot == " ":
                player_field += " "
            if spot == "o":
                player_field += "o"
            if spot == "#":
                player_field += "#"
            if spot == "x":
                player_field += "x"
        player_field += "|\n"
    print(player_field)
    
    
def hit_board(hit_grid, user_input, battlefield): #A grid to show the player their plays. A "x" is placed if the player hits and an "o" is placed if the player misses
    '''(list, str, list) -> list
    Returns a nested list representing the grid that shows a player's hits and misses.
    '''
    if user_input[0].upper() == "A": #Checks the row
        if battlefield[0][int(user_input[1])-1] == "x": #An "x" on the opponent's battlefield shows that it has been hit 
            hit_grid[0][int(user_input[1])-1] = "x" #Add a "x" to the player's hit board to inform them that they have hit the opponent's boat
        else:
            hit_grid[0][int(user_input[1])-1] = "o" #If the above is false, then add an "o" to inform them that their hit was a miss
    
    elif user_input[0].upper() == "B":
        if battlefield[1][int(user_input[1])-1] == "x":
            hit_grid[1][int(user_input[1])-1] = "x"
        else:
            hit_grid[1][int(user_input[1])-1] = "o"
            
    elif user_input[0].upper() == "C":
        if battlefield[2][int(user_input[1])-1] == "x":
            hit_grid[2][int(user_input[1])-1] = "x"
        else:
            hit_grid[2][int(user_input[1])-1] = "o"
        
    elif user_input[0].upper() == "D":
        if battlefield[3][int(user_input[1])-1] == "x":
            hit_grid[3][int(user_input[1])-1] = "x"
        else:
            hit_grid[3][int(user_input[1])-1] = "o"
        
    elif user_input[0].upper() == "E":
        if battlefield[4][int(user_input[1])-1] == "x":
            hit_grid[4][int(user_input[1])-1] = "x"
        else:
            hit_grid[4][int(user_input[1])-1] = "o"
    
    return hit_grid
    
 
def hit_boat(grid, user_input):
    '''(list, str) -> list
    Returns a nested list representing the opponent's battlefield with a marking if their boat has been hit.
    Informs the player if their play was a hit or a miss.
    '''
    if user_input[0].upper() == "A": #Checks the row
        if grid[0][int(user_input[1])-1] in ["#", "x"]: #If there is a "#" present at the coordinate, that means a boat is present 
            print("Hit!")
            grid[0][int(user_input[1])-1] = "x" #Change the "#" at the coordinate to a "x" representing a hit
        else:
            print("Miss!")    
    
    elif user_input[0].upper() == "B":
        if grid[1][int(user_input[1])-1] in ["#", "x"]:
            print("Hit!")
            grid[1][int(user_input[1])-1] = "x"
        else:
            print("Miss!")
            
    elif user_input[0].upper() == "C":
        if grid[2][int(user_input[1])-1] in ["#", "x"]:
            print("Hit!")
            grid[2][int(user_input[1])-1] = "x"
        else:
            print("Miss!")
        
    elif user_input[0].upper() == "D":
        if grid[3][int(user_input[1])-1] in ["#", "x"]:
            print("Hit!")
            grid[3][int(user_input[1])-1] = "x"
        else:
            print("Miss!")
        
    elif user_input[0].upper() == "E":
        if grid[4][int(user_input[1])-1] in ["#", "x"]:
            print("Hit!")
            grid[4][int(user_input[1])-1] = "x"
        else:
            print("Miss!")
    
    return grid


def end_game(player_1_field, player_2_field):
    ''' (list, list) -> None
    Checks if all of player 1 and player 2's boats have sunk and prints out a end-game message.
    '''
    if "#" in str(player_1_field) and "#" not in str(player_2_field):
        print("All of Player 2's ships have sunk.")
        show_grid(player_2_field)
        print("Player 1 is the winner!")
        
    elif "#" in str(player_2_field) and "#" not in str(player_1_field):
        print("All of Player 1's ships have sunk.")
        show_grid(player_1_field)
        print("Player 2 is the winner!")
        
    else:
        print("All of the players' ships have sunk.")
        print("Player 1 and Player 2 has tied!")


def ai_end_game(player_field, ai_field):
    if "#" in str(player_field) and "#" not in str(ai_field):
        print("All of the AI's ships have sunk.")
        show_grid(ai_field)
        print("You are the winner!")
        
    elif "#" in str(ai_field) and "#" not in str(player_field):
        print("All of your ships have sunk.")
        show_grid(player_field)
        print("The AI is the winner!")
        
    else:
        print("Everyone's ships have sunk.")
        print("The game has tied!")


def two_player():
    player_1_field = place_boats()
    while str(player_1_field).count("#") != 6:
        player_1_field = place_boats()
    print("Player 1, this is your battlefield.")
    show_grid(player_1_field)
    new_field = input("Are you satisfied with the placement of your ships? Input yes or no: ")
    while "no" in new_field:
        player_1_field = place_boats()
        while str(player_1_field).count("#") != 6:
            player_1_field = place_boats()
        show_grid(player_1_field)
        new_field = input("Are you satisfied with the placement of your ships? Input yes or no: ")
    
    os.system("cls")
    print("\nPass to player 2.\n")
    time.sleep(5.0)
    os.system("cls")
    
    player_2_field = place_boats()
    while str(player_2_field).count("#") != 6:
        player_2_field = place_boats()
    print("Player 2, this is your battlefield.")
    show_grid(player_2_field)
    new_field = input("Are you satisfied with the placement of your ships? Input yes or no: ")
    while "no" in new_field:
        player_2_field = place_boats()
        while str(player_2_field).count("#") != 6:
            player_2_field = place_boats()
        show_grid(player_2_field)
        new_field = input("Are you satisfied with the placement of your ships? Input yes or no: ")
    
    player_1_hit_board = [[" ", " ", " ", " ", " "], [" ", " ", " ", " ", " "], [" ", " ", " ", " ", " "], [" ", " ", " ", " ", " "], [" ", " ", " ", " ", " "]]
    player_2_hit_board = [[" ", " ", " ", " ", " "], [" ", " ", " ", " ", " "], [" ", " ", " ", " ", " "], [" ", " ", " ", " ", " "], [" ", " ", " ", " ", " "]]
    
    os.system("cls")
    print("\nPass to player 1 to start the game.")
    time.sleep(5.0)
    os.system("cls")
    
    while "#" in str(player_1_field) and "#" in str(player_2_field):
        show_field = input("\nPlayer 1, would you like to see your battlefield again? Input yes or no: ")
        if "yes" in show_field:
            print("This is your battlefield.")
            show_grid(player_1_field)
        
        print("Player 1, ready your aim.")

        show_grid(player_1_hit_board)
        user_input = input("Please input the coordinate to aim your hit: ")
        while user_input[0].upper() not in "ABCDE" or user_input[1] not in "12345" or len(user_input) != 2:
            user_input = input("Please input a valid coordinate: ")
        
        player_2_field = hit_boat(player_2_field, user_input)
        print("This is where you have hit.")
        player_1_hit_board = hit_board(player_1_hit_board, user_input, player_2_field)
        show_grid(player_1_hit_board)
        
        time.sleep(5.0)
        os.system("cls")
        print("Pass to player 2.")
        time.sleep(5.0)
        os.system("cls")
        
        show_field = input("\nPlayer 2, would you like to see your battlefield again? Input yes or no: ")
        if "yes" in show_field:
            print("This is your battlefield.")
            show_grid(player_2_field)
        
        print("Player 2, ready your aim.")
        show_grid(player_2_hit_board)
        user_input = input("Please input the coordinate to aim your hit: ")
        while user_input[0].upper() not in "ABCDE" or user_input[1] not in "12345" or len(user_input) != 2:
            user_input = input("Please input a valid coordinate: ")
        
        player_1_field = hit_boat(player_1_field, user_input)
        print("This is where you have hit.")
        player_2_hit_board = hit_board(player_2_hit_board, user_input, player_1_field)
        show_grid(player_2_hit_board)

        time.sleep(5.0)
        os.system("cls")
        print("Pass to player 1.")
        time.sleep(5.0)
        os.system("cls")
    
    end_game(player_1_field, player_2_field)


def single_player():
    player_field = place_boats()
    while str(player_field).count("#") != 6:
        player_field = place_boats()

    ai_field = place_boats()
    while str(ai_field).count("#") != 6:
        ai_field = place_boats()

    ai_possible_hits = all_ai_possible_hits()
    all_ai_hits = []
    
    print("This is your battlefield.")
    show_grid(player_field)
    new_field = input("Are you satisfied with the placement of your ships? Input yes or no: ")
    while "no" in new_field:
        player_field = place_boats()
        while str(player_field).count("#") != 6:
            player_field = place_boats()
        show_grid(player_field)
        new_field = input("Are you satisfied with the placement of your ships? Input yes or no: ")
    
    player_hit_board = [[" ", " ", " ", " ", " "], [" ", " ", " ", " ", " "], [" ", " ", " ", " ", " "], [" ", " ", " ", " ", " "], [" ", " ", " ", " ", " "]]

    os.system("cls")
    print("\nGenerating AI Battlefield...\n")
    time.sleep(5.0)
    os.system("cls")

    while "#" in str(player_field) and "#" in str(ai_field):
        show_field = input("\nWould you like to see your battlefield again? Input yes or no: ")
        if "yes" in show_field:
            print("This is your battlefield.")
            show_grid(player_field)
        
        print("Ready your aim.")

        show_grid(player_hit_board)
        user_input = input("Please input the coordinate to aim your hit: ")
        while user_input[0].upper() not in "ABCDE" or user_input[1] not in "12345" or len(user_input) != 2:
            user_input = input("Please input a valid coordinate: ")
        
        ai_field = hit_boat(ai_field, user_input)
        print("This is where you have hit.")
        player_hit_board = hit_board(player_hit_board, user_input, ai_field)
        show_grid(player_hit_board)

        time.sleep(2.0)
        os.system("cls")
        print("AI is playing...")
        time.sleep(5.0)
        os.system("cls")

        ai_coord = ai_main(player_field, all_ai_hits, ai_possible_hits)
        print("The AI aims at " + ai_coord + "\n")
        player_field = hit_boat(player_field, ai_coord)
        if ai_coord in ai_possible_hits:
            ai_possible_hits.remove(ai_coord)
        recording_ai_hits(all_ai_hits, ai_coord, player_field)
    
    ai_end_game(player_field, ai_field)


def play_game(): 
    ''' () -> None
    When run, allows players to play the battleship game.
    '''
    print("***WELCOME TO BATTLESHIP***")
    time.sleep(1.0)
    print("Each player has three ships of lengths 1, 2, and 3 on a 5x5 board.\nThe goal of the game is to sink all of your opponent's ships to take the victory.\n")
    time.sleep(5.0)
    num_player = input("Choose the number of players (type one or two): ")
    while "one" not in num_player and "two" not in num_player:
        num_player = input("Choose the number of players (type one or two): ")
    
    if num_player == "two":
        os.system("cls")
        two_player()

    else:
        os.system("cls")
        single_player()

play_game()


