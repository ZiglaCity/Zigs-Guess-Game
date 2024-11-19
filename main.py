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
