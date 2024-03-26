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

    self.control_frame = Frame(self.quest_frame)
    self.control_frame.grid(row=6)

    self.start_over_button = Button(self.control_frame, text="Start Over", command=self.close_play)
    self.start_over_button.grid(row=0, column=2)

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