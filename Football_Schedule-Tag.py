
# https://stackoverflow.com/questions/20822553/align-tabs-from-right-to-left-using-ttk-notebook-widget
import tkinter as tk
from tkinter import ttk


root = tk.Tk()
root.title("Seahawks Schedule")
root.minsize(300, 300)
root.geometry("1000x700")

style = ttk.Style()
style.configure('TNotebook', tabposition='nw') #'nw' as in compass direction

planner = ttk.Notebook(root, width=1000, height=650)

# Create the frames of different colours that are 200*200 pixels in dimensions

tab1 = tk.Frame(planner, bg='lime green', width=800, height=800)
tab2 = tk.Frame(planner, bg='navy blue', width=800, height=800)


# Add the tabs/frames to the notebook object called "planner" 

#Defining the different buttons for the schedule
def b1game():
    print("executing 1st_game_command")
# Giving information regarding the game when the button is clicked


def b2game():
    print("executing 2nd_game_command")

    Label2 = tk.Label(tab2, text = "Home, Seahawks W 35-30 TOP PLAYER: Cam Newton 3 TDS 444 YDS")

def b3game():
    print("executing 3rd_game_command")

    Label3 = tk.Label(tab2, text = "Home, Seahawks W 38-31 TOP PLAYER: Russel Wilson 5 TDs 315 YDS")

def b4game():
    print("executing 4th_game_command")

    Label4 = tk.Label(tab2, text = "Away, Seahawks W 31-23 TOP PLAYER: Russel Wilson 2 TDS 360 YDS")

def b5game():
    print("executing 5th_game_command")

    Label5 = tk.Label(tab2, text = "Home, Seahawks W 27-26 TOP PLAYER: DK Metcalf 2 TDS 93 YDS")

def b6game():
    print("executing 6th_game_command")

    Label6 = tk.Label(tab2, text = "Away, Seahawks L 34-37 TOP PLAYER : Kyler Murray 4 TDS 427 YDS")

def b7game():
    print("executing 7th_game_command")

    Label7 = tk.Label(tab2, text = "Home, Seahawks W 37-27 TOP PLAYER : Russel Wilson 4 TDS 261 YDS")

def b8game():
    print("executing 8th_game_command")

    Label8 = tk.Label(tab2, text = "Away, Seahawks L 44-34 TOP PLAYER : Josh Allen 3 TDS 415 YDS")

def b9game():
    print("executing 9th_game_command")

    Label9 = tk.Label(tab2, text = "Away, Seahawks L 23-16 TOP PLAYER : Jared Goff 302 YDS")

def b10game():
    print("executing 10th_game_command")

    Label10 = tk.Label(tab2, text = "Home, Seahawks W 28-21 TOP PLAYER : D.J Reed Jr 11 tackles 1 PD")

def b11game():
    print("executing 11th_game_command")

    Label11 = tk.Label(tab2, text = "Away, Seahawks W 23-17 TOP PLAYER : DK Metcalf 10 REC 177 YDS")

def b12game():
    print("executing 12th_game_command")

    Label12 = tk.Label(tab2, text = "Home, Seahawks L 17-12 TOP PLAYER : Blake Martinez 10 TOT 5 SOLO 5 TFL 1 PD 1")

def b13game():
    print("executing 13th_game_command")

    Label13 = tk.Label(tab2, text = "Home, Seahawks W 40-3 TOP PLAYER : Russel Wilson 4 TDS 206 YDS 1 INT")

def b14game():
    print("executing 14th_game_command")

    Label14 = tk.Label(tab2, text = "Away, Seahawks W 20-15 TOP PLAYER : Bobby Wagner 13 TOT 7 SOLO 1 PD")

def b15game():
    print("executing 15th_game_command")

    Label15 = tk.Label(tab2, text = "Home, Seahawks W 20-9 TOP PLAYER : Russel Wilson 1 TD 225 YDS")

def b16game():
    print("executing 16th_game_command")

    Label16 = tk.Label(tab2, text = "Away, Seahawks W 26-23 TOP PLAYER : Tyler Lockett 2 TDS 12 REC 90 YDS")

Label1 = tk.Label(tab2, text = "Away, Seahawks W 38-25 TOP PLAYER: Russel Wilson 4 TDS 351 YDS" )



planner.add(tab1, text='Home')
planner.add(tab2, text='Schedule')


def print_answer(event, answer): 
    if (answer[-1] == "*"):
     print("you are right!")
    else:
        print("sorry, incorrect")

class Question:
   def __init__(self, question):
       self.question = question
       self.label = tk.Label(tab1, text=question)
       self.label.pack()


class Answer:
   def __init__(self, answer):
       self.answer = answer 
       self.label = tk.Label(tab1, text=self.answer[:-1])
       self.label.bind("<Button-1>", lambda event: print_answer(event, self.answer))
       self.label.pack()



 
q1 = Question("What year did the Seahawks join the NFL?")
q1a1 = Answer("1. 1976*")
q1a2 = Answer("2. 1990-")
q1a3 = Answer("3. 1969-")
q1a4 = Answer("4. 2000-")

q2 = Question("Which Seahawks RB was nicknamed Beast Mode?")
q2a1 = Answer("1. Shaun Alexander-")
q2a2 = Answer("2. Marshawn Lynch*")
q2a3 = Answer("3. Curt Warner-")
q2a4 = Answer("4. Chris Warren-")







#Giving roles to each button

Seahawks_game1 = tk.Button(tab2, text = "Game 1 Seahawks vs Hawks", height = 5, width = 25, command = b1game)

Seahawks_game2 = tk.Button(tab2, text = "Game 2 Seahawks vs Patriets", height = 5, width = 25, command = b2game)

Seahawks_game3 = tk.Button(tab2, text = "Game 3 Seahawks vs Cowboys", height = 5, width = 25, command = b3game)

Seahawks_game4 = tk.Button(tab2, text = "game 4 Seahawks vs Dolphins", height = 5, width = 25, command = b4game)

Seahawks_game5 = tk.Button(tab2, text = "game 5 Seahawks vs Dolphins", height = 5, width = 25, command = b5game)

Seahawks_game6 = tk.Button(tab2, text = "game 6 Seahawks vs Cardinals", height = 5, width = 25, command = b6game)

Seahawks_game7 = tk.Button(tab2, text = "game 7 Seahawks vs 49ers", height = 5, width = 25, command = b7game)

Seahawks_game8 = tk.Button(tab2, text = "gamee 8 Seahawks vs Bills", height = 5, width = 25, command = b8game)

Seahawks_game9 = tk.Button(tab2, text = "game 9 Seahawks vs Rams", height = 5, width = 25, command = b9game)

Seahawks_game10 = tk.Button(tab2, text = "game 10 Seahawks vs Cardinals", height = 5, width = 25, command = b10game)

Seahawks_game11 = tk.Button(tab2, text = "game 11 Seahawks vs Eagles", height = 5, width = 25, command = b11game)

Seahawks_game12 = tk.Button(tab2, text = "game 12 Seahawks vs Giants", height = 5, width = 25, command = b12game)

Seahawks_game13 = tk.Button(tab2, text = "game 13 Seahawks vs Jets", height = 5, width = 25, command = b13game)

Seahawks_game14 = tk.Button(tab2, text = "game 14 Seahawks vs Washington", height = 5, width = 25, command = b14game)

Seahawks_game15 = tk.Button(tab2, text = "game 15 Seahawks vs Rams", height = 5, width = 25, command = b15game)

Seahawks_game16 = tk.Button(tab2, text = "game 16 Seahawks vs 49ers", height = 5, width = 25, command = b16game)



# Tabs will be added to the "top" of the "frame"
#planner.pack(side=tk.TOP)

planner.pack()

Label1.grid(row=1, column=0)

Seahawks_game1.grid(row=0, column=0)

Seahawks_game2.grid(row=0, column=2)

Seahawks_game3.grid(row=0, column=4)

Seahawks_game4.grid(row=3, column=0)

Seahawks_game5.grid(row=3, column=2)

Seahawks_game6.grid(row=3, column=4)

Seahawks_game7.grid(row=6, column=0)

Seahawks_game8.grid(row=6, column=2)

Seahawks_game9.grid(row=6, column=4)

Seahawks_game10.grid(row=9, column=0)

Seahawks_game11.grid(row=9, column=2)

Seahawks_game12.grid(row=9, column=4)

Seahawks_game13.grid(row=12, column=0)

Seahawks_game14.grid(row=12, column=2)

Seahawks_game15.grid(row=12, column=4)

Seahawks_game16.grid(row=15, column=0)




root.mainloop()
