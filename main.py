import tkinter as tk
import random

#Global variables initialization
player1_name = "Player1"
player2_name = "Player2"
computer_name = "Computer"
player1_score = 0
player2_score = 0
current_player = player1_name
max_score = 11
trials = 0
game_mod_label = 0
number_of_rounds = 2
players_round = player1_name
message = ""
rounds_left = number_of_rounds
random_number = None
game_mode = 2

# Set a fixed window size
window_width = 600
window_height = 650

#define a fixed style to be used for all the widgets
label_style = {
    "font": ("Arial", 14, "italic"),
    "bg": "#e6e6e6",
    "fg": "#2b2b2b",
    "padx": 8,
    "pady": 8
}

button_style = {
    "font": ("Comic Sans MS", 12, "bold"),
    "bg": "#BBBBBB",
    "fg": "#663399",
    "bd": 3,
    "relief": "ridge"
}

entry_style = {
    "font": ("Comic Sans MS", 12),
    "bg": "#ffebcd",
    "fg": "#8b0000",
    "bd": 2,
    "relief": "groove"
}

frame_style = {
    "bg": "#F5F5F5",
    "bd": 2,
    "relief": "sunken"
}

spinbox_style = {
    "font": ("Arial", 12, "bold"),
    "bg": "#f5f5f5",
    "fg": "#333333",
    "bd": 2,
    "relief": "flat",
    "highlightbackground": "#dcdcdc",
    "highlightcolor": "#4CAF50",
    "highlightthickness": 1,
    "buttonbackground": "#4CAF50",
    "buttondownrelief": "groove",
    "buttonuprelief": "groove"
}

#define a funciton which applies the styles to their respective widgets
def apply_styles(widget):
    #Apply styles to all Button, Label, Entry, and Frame widgets
    if isinstance(widget, tk.Button):
        widget.config(**button_style)
    elif isinstance(widget, tk.Label):
        widget.config(**label_style)
    elif isinstance(widget, tk.Entry):
        widget.config(**entry_style)
    elif isinstance(widget, tk.Frame):
        widget.config(**frame_style)
    elif isinstance(widget, tk.Spinbox):
        widget.config(**spinbox_style)

    # Recursively apply styles to all children
    for child in widget.winfo_children():
        apply_styles(child)


#define the function to handle the command issued when the vs computer button is clicked
def select_two_players():
    global game_mode
    game_mode = 2


#define the function to handle the command issued when the vs computer button is clicked
def select_vs_computer():
    global game_mode, player2_name
    game_mode = 1
    player2_name = "Computer"


#define a function that will called when the settings button is clicked to allow users change some default settings
def settings():
    open_phase_4()


# a function which saves all the changes made by the user
def save_changes():
    global player1_name, player2_name, number_of_rounds, players_round
    player1_name = pn1.get()
    player2_name = pn2.get()
    player2_name.capitalize()
    player1_name.capitalize()
    players_round = player1_name
    number_of_rounds = no_rounds.get()


#create a function to calculate the score of the players
def update_score():
    global player1_score, player2_score,pscore, current_player, pscore, player1_score_var, player2_score_var
    calculated_score = max_score - trials
    if current_player == player1_name:
        player1_score += calculated_score
        pscore = f"{player1_name.capitalize()}: {player1_score}"
        player1_score_var.set(pscore)

    else:
        player2_score += calculated_score
        pscore = f"{player2_name.capitalize()}: {player2_score}"
        player2_score_var.set(pscore)


#define a function which  updates the board including the scores for a new game
def update_board():
    global trials, status_var,player1_score,player2_score, rounds_left, random_number, current_player, guess_entry
    trials = 0
    player1_score = 0
    player2_score = 0
    rounds_left = number_of_rounds
    current_player = player1_name
    random_number = random.randint(0, 9)
   
#define a function which swiches turn after avery tirals 
def switch_turn():
    global current_player
    current_player = player2_name if current_player == player1_name else player1_name


#create a function to be called when the check button is clicked to check for each players guess
def check_guess():
    global message,difference, check_button , trials, players_round, current_player, rounds_left, player1_score, pturn, current_turn_var, player2_score, guess_entry, status_var, random_number

    try:
        guess = int(guess_entry.get())
    except ValueError:
        status_var.set("Invalid input!")
        return

    #increase the number of trials after each check
    trials += 1

    #set the conditions for both when the number of trials left is and is not zero and when the users gues is either too large, too small or close
    if guess == random_number:
        update_score()
        message = f"Correct! {current_player.capitalize()} wins!"
        pturn = f"Player {current_player.capitalize()}'s Turn"
        status_var.set(message)
        #disable the entry box and check button until the next round button is clicked
        guess_entry.config(state='readonly')
        check_button.config(state="disabled")

    else:
        guess_entry.delete(0, tk.END)
        difference = guess - random_number

        if abs(difference) <= 2 and trials != 10:
            switch_turn()
            message = f"Very Close! {current_player.capitalize()} is next"
            pturn = f"Player: {current_player.capitalize()}'s Turn"
            current_turn_var.set(pturn)
            status_var.set(message)

        elif difference <= -3 and trials != 10:
            switch_turn()
            message = f"Too Small! {current_player.capitalize()} is next"
            pturn = f"Player: {current_player.capitalize()}'s Turn"
            current_turn_var.set(pturn)
            status_var.set(message)

        elif difference >= 3 and trials != 10:
            switch_turn()
            message = f"Too large! {current_player.capitalize()} is next"
            pturn = f"Player: {current_player.capitalize()}'s Turn"
            current_turn_var.set(pturn)
            status_var.set(message)

        else:
            message = "Too many attemps! Begin Next Round!"
            status_var.set(message)
            #disable the entry box and check button until the next round button is clicked
            guess_entry.config(state='readonly')
            check_button.config(state="disabled")
    if rounds_left == 0:
            gameOver()