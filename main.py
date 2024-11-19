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


#create a function to be called when the check button is called against the computer
def check_vs_computer_guess():
    global message, msg, difference,vs_computer_guess_entry, vs_computer_guess, computer_guess, check_button , trials, players_round, current_player, rounds_left, player1_score, pturn, current_turn_var, player2_score, guess_entry, status_var, random_number

    if current_player == player1_name:
        try:
            guess = int(guess_entry.get())
        except ValueError:
            status_var.set("Invalid input!")
            return
    else:
        guess = int(vs_computer_guess_entry.get())
        msg = ""
        alert.set(msg)
        vs_computer_guess_entry.delete(0, tk.END)
        
    #increase the number of trials after each check
    trials += 1

    #set the conditions for both when the number of trials left is and is not zero and when the users gues is either too large, too small or close
    if guess == random_number:
        update_score()
        message = f"Correct! {current_player.capitalize()} wins!"
        pturn = f"Player: {current_player.capitalize()}'s Turn"
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
            #make sure the players do not use more than ten trials in total since there are only ten digits
            message = "Too many attemps! Begin Next Round!"
            status_var.set(message)
            #disable the entry box and check button until the next round button is clicked
            guess_entry.config(state='readonly')
            check_button.config(state="disabled")

    if rounds_left == 0:
            gameOver()

    #disable the users entry when is it the computers turn and select and display computer's guess
    if current_player == player2_name and guess != random_number:
        guess_entry.config(state="readonly")
        computer_guess = random.randint(0, 9)

        #change the computers guess if it is the same wrong thing as player 1 guessed
        while computer_guess == guess:
            computer_guess = random.randint(0, 9)

        guess = computer_guess
        msg = f"Computer Played {computer_guess}, Check!"
        alert.set(msg)
        vs_computer_guess.set(guess)
    elif current_player == player1_name:
        guess_entry.config(state="normal")
        vs_computer_guess_entry.delete(0, tk.END)


#create a function that calls for a rematch in the gameover phase
def rematch():
    global player1_score,current_player, player2_score, rounds_left
    start_game()

    update_board()
    rounds_left_var.set(f"Rounds Left: {rounds_left}")
    player1_score_var.set(f"{player1_name.capitalize()}: {player1_score}")
    player2_score_var.set(f"{player2_name.capitalize()}: {player2_score}")
    current_turn_var.set(f"Player: {current_player.capitalize()}'s Turn")


#define a function which is connected to the Next round button and resets the game round
def reset_round():
    global current_player,guess, trials, players_round, rounds_left, random_number
    rounds_left -= 1
    players_round = player2_name if players_round == player1_name else player1_name
    current_player = players_round
    current_turn_var.set(f"Player: {current_player.capitalize()}'s Turn")
    rounds_left_var.set(f"Rounds Left: {rounds_left}")
    guess_entry.config(state='normal')
    guess_entry.delete(0, tk.END)
    check_button.config(state="normal")
    random_number = random.randint(0, 9)
    trials = 0
    status_var.set("")

    if rounds_left == 0:
        return gameOver()
           

    if current_player == player2_name and game_mode == 1:
        guess_entry.config(state="readonly")
        computer_guess = random.randint(0, 9)
        guess = computer_guess
        msg = f"Computer Played {computer_guess}, Check!"
        alert.set(msg)
        vs_computer_guess.set(guess)
    elif current_player == player1_name and game_mode == 1:
        guess_entry.config(state="normal")
        vs_computer_guess_entry.delete(0, tk.END)


#the start game phase which is to be called when the start button is clicked
def start_game():
    if game_mode == 2:
        open_phase_2()
    elif game_mode == 1:
        open_phase_3()


#create a game over function which determines the winner
def gameOver():
    # Transition to Phase 4: Game Over screen
    for widget in phase_window.winfo_children():
        widget.destroy()

    phase_window.title("Game Over")
    
    final_message = ""
    if player1_score > player2_score:
        final_message += f"{player1_name.capitalize()} wins!"
    elif player2_score > player1_score:
        final_message +=f"{player2_name.capitalize()} wins!"
    else:
        final_message += " It's a tie!"

    p1 = tk.StringVar(value= f"{player1_name.capitalize()}: {player1_score}")
    p2 = tk.StringVar(value= f"{player2_name.capitalize()}: {player2_score}")

    game_over_label = tk.Label(phase_window, text = "Game Over!")
    game_over_label.pack(pady=10)

    #create a frame to keep both players final score in the gameover  phase
    final_score = tk.Frame(phase_window)
    final_score.pack(pady=20)

    player1_score_label = tk.Label(final_score, textvariable=p1)
    player1_score_label.pack(side="left", padx=5)

    player2_score_label = tk.Label(final_score, textvariable=p2)
    player2_score_label.pack(side="right", padx=5)
    
    final_label = tk.Label(phase_window, text=final_message)
    final_label.pack(pady=20)

    exit_button = tk.Button(phase_window, text="Exit", command=phase_window.quit)
    exit_button.pack(pady=20)

    rematch_button = tk.Button(phase_window, text="Rematch", command=rematch)
    rematch_button.pack(pady=20)

    home_button = tk.Button(phase_window, text="Main Menu", command=return_to_phase_1)
    home_button.pack(pady=20)

    apply_styles(phase_window)
    
    pass
    

#define a function which handles the phase phase of the game i.e phase1
def open_phase_1():
    global phase_window
    phase_window = tk.Tk()
    phase_window.title("Zigla's Guess Game")
    phase_window.geometry(f"{window_width}x{window_height}")
    phase_window.resizable(False, False)

    #define the widgets in phase1
    welcome_label = tk.Label(phase_window, text="WELCOME TO ZIGLA'S GUESS GAME")
    welcome_label.pack(pady=30)

    game_mode_frame = mod_label = tk.Frame(phase_window)
    game_mode_frame.pack(pady=50)

    mod_label = tk.Label(game_mode_frame, text="SELECT GAME MODE")
    mod_label.pack(pady=5)

    two_players_button = tk.Button(game_mode_frame, text=" TWO PLAYERS", command=select_two_players)
    two_players_button.pack(pady=20)

    vs_computer_button = tk.Button(game_mode_frame, text="VS COMPUTER",command=select_vs_computer)
    vs_computer_button.pack(pady=20)

    settings_button = tk.Button(phase_window, text="SETTINGS", command=settings)
    settings_button.pack(pady=15)

    start_button = tk.Button(phase_window, text="START", command=start_game)
    start_button.pack(pady=20)


    #Apply styles to all widgets
    apply_styles(phase_window)

    phase_window.mainloop()


#define the phase 2 which begins the game with two players
def open_phase_2():
    global current_player, rounds_left, player1_score, player2_score, random_number
    # Clear the window for Phase 2
    for widget in phase_window.winfo_children():
        widget.destroy()

    phase_window.title("Two-Player Game")
    
    random_number = random.randint(0, 9)
    global check_button, status_var, rounds_left, player1_score_var, player2_score_var, rounds_left_var, current_turn_var, guess_entry
    
    status_var = tk.StringVar()
    player1_score_var = tk.StringVar(value=f"{player1_name.capitalize()}: {player1_score}")
    player2_score_var = tk.StringVar(value=f"{player2_name.capitalize()}: {player2_score}")
    rounds_left_var = tk.StringVar(value=f"Rounds Left: {rounds_left}")
    current_turn_var = tk.StringVar(value=f"Player: {current_player.capitalize()}'s Turn")
    # Frame for Player Scores
    score_frame = tk.Frame(phase_window)
    score_frame.pack(pady=15)

    score_label = tk.Label(score_frame, text="SCORES: ")
    score_label.pack(side=tk.LEFT)
    
    player1_label = tk.Label(score_frame, textvariable=player1_score_var)
    player1_label.pack(side=tk.LEFT)
    
    player2_label = tk.Label(score_frame, textvariable=player2_score_var)
    player2_label.pack(side=tk.RIGHT)
    
    rounds_left_label = tk.Label(phase_window, textvariable=rounds_left_var)
    rounds_left_label.pack(pady=8)
    
    turn_label = tk.Label(phase_window, textvariable=current_turn_var)
    turn_label.pack(pady=8)
    
    instruction_label = tk.Label(phase_window, text="Select a random number 0-9")
    instruction_label.pack(pady=5)
    
    guess_entry = tk.Entry(phase_window)
    guess_entry.pack(pady=10)
    
    check_button = tk.Button(phase_window, text="Check", command=check_guess)
    check_button.pack(pady= 20)
    
    status_checker = tk.Entry(phase_window, width=30, textvariable=status_var, state="readonly", justify='center')
    status_checker.pack(pady= 5)

    next_round_button = tk.Button(phase_window, text="Next Round", command=reset_round)
    next_round_button.pack(pady=20)
    
    exit_button = tk.Button(phase_window, text="Exit", command=return_to_phase_1)
    exit_button.pack(pady=30)

    #apply the styles to the widgets
    apply_styles(phase_window)


def return_to_phase_1():
    global status_var
    # Clear the window for Phase 1
    for widget in phase_window.winfo_children():
        widget.destroy()

    phase_window.title("Guess Game")

    #define the widgets in phase1
    welcome_label = tk.Label(phase_window, text="WELCOME TO ZIGLA'S GUESS GAME")
    welcome_label.pack(pady=30)

    game_mode_frame = mod_label = tk.Frame(phase_window)
    game_mode_frame.pack(pady=50)

    mod_label = tk.Label(game_mode_frame, text="SELECT GAME MODE")
    mod_label.pack(pady=5)

    two_players_button = tk.Button(game_mode_frame, text=" TWO PLAYERS", command=select_two_players)
    two_players_button.pack(pady=20)

    vs_computer_button = tk.Button(game_mode_frame, text="VS COMPUTER",command=select_vs_computer)
    vs_computer_button.pack(pady=20)

    settings_button = tk.Button(phase_window, text="SETTINGS", command=settings)
    settings_button.pack(pady=15)

    start_button = tk.Button(phase_window, text="START", command=start_game)
    start_button.pack(pady=20)

    #apply the styles to the widgets
    apply_styles(phase_window)

    update_board()


#define the third phasse which opens when the user clicks on Vs computer
def open_phase_3():
    global current_player, rounds_left, player1_score, player2_score, random_number
    # Clear the window for Phase 2
    for widget in phase_window.winfo_children():
        widget.destroy()

    phase_window.title("Vs Computer")
    
    random_number = random.randint(0, 9)
    global check_button,vs_computer_guess, alert, vs_computer_guess_entry, status_var, rounds_left, player1_score_var, player2_score_var, rounds_left_var, current_turn_var, guess_entry
    
    status_var = tk.StringVar()
    alert = tk.StringVar()
    player1_score_var = tk.StringVar(value=f"{player1_name.capitalize()}: {player1_score}")
    player2_score_var = tk.StringVar(value=f"{player2_name.capitalize()}: {player2_score}")
    rounds_left_var = tk.StringVar(value=f"Rounds Left: {rounds_left}")
    current_turn_var = tk.StringVar(value=f"Player: {current_player}'s Turn")
    vs_computer_guess = tk.StringVar()

    # Frame for Player Scores
    score_frame = tk.Frame(phase_window)
    score_frame.pack(pady=15)

    score_label = tk.Label(score_frame, text="SCORES: ")
    score_label.pack(side=tk.LEFT)
    
    player1_label = tk.Label(score_frame, textvariable=player1_score_var)
    player1_label.pack(side=tk.LEFT)
    
    player2_label = tk.Label(score_frame, textvariable=player2_score_var)
    player2_label.pack(side=tk.RIGHT)
    
    # Labels and Entries
    rounds_left_label = tk.Label(phase_window, textvariable=rounds_left_var)
    rounds_left_label.pack(pady=8)
    
    turn_label = tk.Label(phase_window, textvariable=current_turn_var)
    turn_label.pack(pady=8)
    
    instruction_label = tk.Label(phase_window, text="Select a random number 0-9")
    instruction_label.pack(pady=5)

    vs_computer_frame = tk.Frame(phase_window)
    vs_computer_frame.pack(pady=10)

    p1_frame = tk.Frame(vs_computer_frame)
    p1_frame.pack(side="left")

    p1_label = tk.Label(p1_frame, text="Player1")
    p1_label.pack(side="top")
    
    guess_entry = tk.Entry(p1_frame)
    guess_entry.pack(side="bottom")

    p2_frame = tk.Frame(vs_computer_frame)
    p2_frame.pack(side="right")

    p2_label = tk.Label(p2_frame, text="Computer")
    p2_label.pack(side="top")

    vs_computer_guess_entry = tk.Entry(p2_frame, textvariable=vs_computer_guess, state="readonly")
    vs_computer_guess_entry.pack(side="bottom")

    alert_label = tk.Label(phase_window, textvariable=alert, width=20)
    alert_label.pack()
    
    check_button = tk.Button(phase_window, text="Check", command=check_vs_computer_guess)
    check_button.pack(pady= 10)
    
    status_checker = tk.Entry(phase_window, width=30, textvariable=status_var, state="readonly", justify='center')
    status_checker.pack(pady=5, padx=30)

    next_round_button = tk.Button(phase_window, text="Next Round", command=reset_round)
    next_round_button.pack(pady=15)
    
    exit_button = tk.Button(phase_window, text="Exit", command=return_to_phase_1)
    exit_button.pack(pady=15)

    #apply the styles to the widgets
    apply_styles(phase_window)


def open_phase_4():
    # Clear the window for Phase 1
    for widget in phase_window.winfo_children():
        widget.destroy()

    phase_window.title("Settings")

    global pn1, pn2, no_rounds
    pn1 = tk.StringVar()
    pn2 = tk.StringVar()
    pn1.set(f"{player1_name.capitalize()}")
    pn2.set(f"{player2_name.capitalize()}")
    no_rounds = tk.IntVar()

    # Recreate Phase 1 content
    settings_label = tk.Label(phase_window, text="Remeber to Click the save button to apply the changes made")
    settings_label.pack(pady=20)

    change_player_name_label = tk.Label(phase_window, text="Change player names")
    change_player_name_label.pack(pady=5)

    player1_name_frame = tk.Frame(phase_window)
    player1_name_frame.pack(pady=10)

    player1_name_label = tk.Label(player1_name_frame, text="Input Player1 Name")
    player1_name_label.pack(side="left")

    player1_name_entry = tk.Entry(player1_name_frame, textvariable=pn1)
    player1_name_entry.pack(side="right")

    player2_name_frame = tk.Frame(phase_window)
    player2_name_frame.pack(pady=10)

    player2_name_label = tk.Label(player2_name_frame, text="Input Player2 Name")
    player2_name_label.pack(side="left")

    player2_name_entry = tk.Entry(player2_name_frame, textvariable=pn2)
    player2_name_entry.pack(side="right")

    no_rounds_frame = tk.Frame(phase_window)
    no_rounds_frame.pack(pady=10)

    no_rounds_label = tk.Label(no_rounds_frame, text="Number Of Rounds: ")
    no_rounds_label.pack(side="left")

    no_rounds_spinbox = tk.Spinbox(no_rounds_frame, values=(2, 4,6, 8, 10, 16, 32, 64, 1), textvariable=no_rounds)
    no_rounds_spinbox.pack(side="right")

    save_changes_button = tk.Button(phase_window, text="SAVE", command=save_changes)
    save_changes_button.pack(pady=30)

    main_menu_button = tk.Button(phase_window, text="MAIN MENU", command=return_to_phase_1)
    main_menu_button.pack(pady=40)

    #apply the styles to the widgets
    apply_styles(phase_window)
    

# Start the game
open_phase_1()