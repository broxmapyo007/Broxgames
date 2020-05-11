from tkinter import *
from tkinter import messagebox
import random as r

def button(frame):          #Function to define a button
    b=Button(frame,bg="black",width=2,text="   ",font=('arial',20,'bold'))
    return b
    
def change_a():             #Function to change the operand for the next player
    global a
    for i in ['O','X']:
        if not(i==a):
            a=i
            break
            
def reset():                #Resets the game
    global a
    for i in range(3):
        for j in range(3):
                b[i][j]["text"]=" "
                b[i][j]["state"]=NORMAL
    a=r.choice(['O','X'])
    
def check():                #Checks for victory or Draw
    for i in range(3):
            if(b[i][0]["text"]==b[i][1]["text"]==b[i][2]["text"]==a or b[0][i]["text"]==b[1][i]["text"]==b[2][i]["text"]==a):
                    messagebox.showinfo("Congrats!!","'"+a+"' has won")
                    reset()
    if(b[0][0]["text"]==b[1][1]["text"]==b[2][2]["text"]==a or b[0][2]["text"]==b[1][1]["text"]==b[2][0]["text"]==a):
        messagebox.showinfo("Congrats!!","'"+a+"' has won")
        reset()   
    elif(b[0][0]["state"]==b[0][1]["state"]==b[0][2]["state"]==b[1][0]["state"]==b[1][1]["state"]==b[1][2]["state"]==b[2][0]["state"]==b[2][1]["state"]==b[2][2]["state"]==DISABLED):
        messagebox.showinfo("Draw!!","The match ended in a draw")
        reset()
        
def click(row,col):
        b[row][col].config(text=a,state=DISABLED,disabledforeground=colour[a])
        check()
        change_a()
        label.config(text=a+"'s Chance")
        

root=Tk()             #Window defined
root.title("Tic-Tac-Toe")
root.geometry("1000x1500")   #Title given
a=r.choice(['O','X'])       #Two operators defined
colour={'O':"red",'X':"green"}
b=[[],[],[]]
for i in range(3):
		for j in range(3):
			b[i].append(button(root))
			b[i][j].config(command= lambda row=i,col=j:click(row,col))
			b[i][j].grid(row=i,column=j)
label=Label(text=a+"'s Chance",font=('arial',5,'bold'))
label.grid(row=4,column=1)
root.mainloop()