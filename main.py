from tkinter import *

class ChooseRounds:
  def __init__(self):
    button_fg = "white"
    button_font_small = ("Arial", "13", "bold")
    button_font_big = ("Arial", "16", "bold")
    
    # Set up GUI Frame
    self.intro_frame = Frame(padx=10, pady=10)
    self.intro_frame.grid()

    # heading and brief instructions
    self.intro_heading_label = Label(self.intro_frame, text="Colour Quest", font=button_font_big)
    self.intro_heading_label.grid(row=0)
    
    choose_instructions_txt = " In each rounds, you will be given six dif colours. pick a colour and try to beat the coumputer. \n \n To begin, choose how many rounds you'd like to play \n Good luck! \n p.s. don't feel frustrated if you can't understand the rules i can't even understand the rules or even the purpose of this game."
    self.choose_instructions_label = Label(self.intro_frame, text=choose_instructions_txt, wraplength=300, justify="left")
    self.choose_instructions_label.grid(row=1)

    #Rounds Buttons...
    self.how_many_frame = Frame(self.intro_frame)
    self.how_many_frame.grid(row=2)
    # list set up rounds button. first coulour, second number of rounds.
    btn_color_value = [["#CC0000", 3],["#009900", 5],["#000099", 10]]

    for item in range(0, 3):
      self.rounds_button = Button(self.how_many_frame, fg=button_fg, bg=btn_color_value[item][0], text="{} Rounds".format(btn_color_value[item][1]), font=button_font_small, width=10, command=lambda i=item: self.to_play(btn_color_value[i][1]))
      self.rounds_button.grid(row=0, column=item, padx=5, pady=5)

  def to_play(self, num_rounds):
    Play(num_rounds)
    
    # hide intro window
    root.withdraw()

class Play:
  def __init__(self, how_many):
    self.play_box = Toplevel()
    # if users press cross at top, closes help and 'releases' help button
    self.play_box.protocol('WM_DELETE_WINDOW', partial(self.close_play))
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
    
    
    

if __name__ == "__main__":
  root = Tk()
  root.title("Colour Quest Planning")
  ChooseRounds()
  root.mainloop()