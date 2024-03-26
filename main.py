from tkinter import *
from functools import partial # To prevent unwanted windows
import csv
import random

# users choose 3, 5 0r 10
class ChooseRounds:
  def __init__(self):
    # test 3 input
    self.to_play(3)

  def to_play(self, num_rounds):
    Play(num_rounds)

    # hide intro window
    root.withdraw()

class Play:
  def __init__(self, how_many):
    self.play_box = Toplevel()
    # if users press cross at top, closes help and 'releases' help button
    self.play_box.protocol('WM_DELETE_WINDOW', partial(self.close_play))
    # how many rounds 
    self.round_wanted = IntVar()
    self.round_wanted.set(how_many)
    # how many rounds they play
    self.round_played = IntVar()
    self.round_played.set(0)
    # how many rounds they won
    self.round_won = IntVar()
    self.round_won.set(0)
    #lists score
    user_scores = []
    computer_scores = []

    # get all the colours from the colours file
    self.all_colours = self.get_all_colours()

    self.quest_frame = Frame(self.play_box, padx=10, pady=10)
    self.quest_frame.grid()

    rounds_heading = "Choose - Round 1 of {}".format(how_many)
    self.choose_heading = Label(self.quest_frame, text=rounds_heading, font=("Arial", "16", "bold"))
    self.choose_heading.grid(row=0)
    # ***** row 1 *****
    instructions = "In each round, you will be given six colours. Pick a colour and try to beat the computer. \n results of the round will be shown below."
    self.instructions_label = Label(self.quest_frame, text=instructions, wraplength=300, justify="left")
    self.instructions_label.grid(row=1)
    # ***** row 2 ***** get colours for buttons for first round ...
    button_colours_list = self.get_round_colors()
    print(button_colours_list)
    # create colour buttons (in choice_frame)
    self.choice_frame = Frame(self.quest_frame)
    self.choice_frame.grid(row=2)
    for item in range(0, 6):
      self.colour_button = Button(self.choice_frame, fg=button_colours_list[item][2], bg=button_colours_list[item][0], text="{}".format(button_colours_list[item][]),width=15,command=lambda i=item: self.to_play(button_colours_list[i][3]))
      self.colour_button.grid(row=item // 3, column=item % 3, padx=5, pady=5)
    # ***** row 3 ***** display computer choice
    self.comp_choice_label = Label(self.quest_frame, text="Computer Choice will appea", bg="#C0C0C0", width=51)
    self.comp_choice_label.grid(row=3, pady=10)
    # ***** row 4 ***** rounds results & next button
    self.rounds_frame = Frame(self.quest_frame)
    self.rounds_frame.grid(row=4, pady=5)
    
    self.round_results_label = Label(self.rounds_frame, text="Round Results will appea", width=32, bg="#FFF2CC", font=("Arial", "10"),pady=5)
    self.round_results_label.grid(row=0, column=0, padx=5)
    
    self.next_button = Button(self.rounds_frame, text="Next Round", fg="#FFFFFF", bg="008BFC", font=("Arial", "12","bold"), width=10, state=DISABLED)
    self.next_button.grid(row=0, column=1)
    # ***** row 5 ***** big overall results
    self.game_results_label = Label(self.quest_frame, text="Game Totals: User: - \t Computer: -", bg="#C0C0C0", padx=10, pady=10, font=("Arial", "10"), width=42)
    self.game_results_label.grid(row=5, pady=5)
    # ***** row 6 *****
    self.control_frame = Frame(self.quest_frame)
    self.control_frame.grid(row=6)

    control_buttons = [["#CC6600", "Help", "get help"], ["#004C99", "Statistics", "get stats"], ["#808080", "Start Over", "start over"]]
    for item in range(0, 3):
      self.make_control_button = Button(self.control_frame, fg="#FFFFFF", bg=control_buttons[item][0], text=control_buttons[item][1], width=11, font=("Arial", "12","bold"), command=lambda i=item: self.to_do(control_buttons[i][2]))
    self.make_control_button.grid(row=0, column=item, padx=5, pady=5)

  # retrieve colours from file
  def get_all_colours(self):
    with open("colour_list_hex_v1.py", newline='') as file:
      # Read all rows into a list
      var_all_colors = list(csv.reader(file, delimiter=","))
    # remove the first row (header values)
    var_all_colors.pop(0)
    return var_all_colors

  # randomly choose 6 colours for buttons
  def get_round_colors(self):
    round_colour_list = []
    color_scores = []
    # loop 6 times (6 unique colours)
    while len(round_colour_list) < 6:
      # choose item
      chosen_colour = random.choice(self.all_colours)
      chosen_index = self.all_colours.index(chosen_colour)
      # check score not in list
      if chosen_colour[2] not in color_scores:
        # add item to rounds list
        round_colour_list.append(chosen_colour)
        color_scores.append(chosen_colour[1])
        # remove item from master list
        self.all_colours.pop(chosen_index)
    return round_colour_list
  
  def to_compare(self, user_score):
    print("your score is {}".format(user_score))
  
  def to_do(self, action):
    if action == "get help":
      self.get_help()
    elif action == "get stats":
      self.get_stats()
    else:
      self.close_play()

  def get_help(self):
    pass
  
  def get_stats(self):
    pass
    
  def close_play(self):
    # reshow
    root.deiconify()
    self.play_box.destroy()


#main routine
if __name__ == "__main__":
  root = Tk()
  root.title("Colour Quest Planning")
  ChooseRounds()
  root.mainloop()