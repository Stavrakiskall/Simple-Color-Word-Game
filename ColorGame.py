from tkinter import *
import random
colors = ['white', 'red', 'blue', 'green', 'orange', 'pink', 'purple', 'black']
score = 0
timeleft = 40


#otan sinartisi leitourgei me koumpi apo to pliktrologio
#diladi tin edoly bind
#tote exei san parametro to event



def start(event):
    if timeleft == 40:
        countdown()
    nextColor()


def countdown():
    global timeleft
    if timeleft > 0:
        timeleft -= 1
        timeLabel.configure(text= "Time Left:" + str(timeleft))
        timeLabel.after(1000 ,countdown)
    else:
        timeLabel.configure(text="GAME OVER")
        win.unbind('<Return>')
        e.configure(state="disabled")
def nextColor():
    global score
    if e.get().lower() == colors[1].lower():
        score += 1
        print(score)
    e.delete(0, END)
    random.shuffle(colors)
    label.configure(text=colors[0], fg=colors[1])
    scoreLabel.configure(text = "Score:" + str(score))

win = Tk()
win.title("COLORGAME")
win.geometry("400x200")
instructions = Label(win,text="Type in the colour of the words, and not the word text!",
                             font=('Tahoma', 12))
instructions.pack()
scoreLabel = Label(win,text="Press enter to start", font=('Tahoma', 12))
scoreLabel.pack()
timeLabel = Label(win,text="Time left:" + str(timeleft), font=('Tahoma', 12))
timeLabel.pack()
label = Label(win, font=('Tahoma', 60))
label.pack()
e = Entry(win)
e.pack()
win.bind('<Return>', start) # koumpi apo pliktrologio, ti thelw n kanei

win.mainloop()