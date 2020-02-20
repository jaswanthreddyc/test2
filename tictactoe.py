from tkinter import *
def callback(r,c):
    global player
    if player =='X' and states[r][c]==0 and stop_game==False:
        b[r][c].configure(text='X')
        states[r][c]='X'
        player='O'
    if player =='O' and states[r][c]==0 and stop_game==False:
        b[r][c].configure(text='O')
        states[r][c]='O'
        player='X'
    check_winner()

def check_winner():
    global stop_game
    #row wise check
    for i in range(3):
        if states[i][0]==states[i][1]==states[i][2]!=0:
            b[i][0].configure(bg='grey')
            b[i][1].configure(bg='grey')
            b[i][2].configure(bg='grey')
            stop_game=True
    #column wise check
    for j in range(3):
        if states[0][j]==states[1][j]==states[2][j]!=0:
            b[0][j].configure(bg='grey')
            b[1][j].configure(bg='grey')
            b[2][j].configure(bg='grey')
            stop_game=True

    #first diagonal
    if states[0][0]==states[1][1]==states[2][2]!=0:
        b[0][0].configure(bg='grey')
        b[1][1].configure(bg='grey')
        b[2][2].configure(bg='grey')
        stop_game=True

    #second diagonal 
    if states[0][2]==states[1][1]==states[2][0]!=0:
        b[0][2].configure(bg='grey')
        b[1][1].configure(bg='grey')
        b[2][0].configure(bg='grey')
        stop_game=True    

player='X'
stop_game = False

b=[[0,0,0],
   [0,0,0],
   [0,0,0]]

states=[[0,0,0],
        [0,0,0],
        [0,0,0]]

root = Tk()
root.title("Tic-Tac-Toe")
for i in range(3):
    for j in range(3):
        b[i][j] = Button(font=('Verdana',56),width=3,bg='yellow',command=lambda r=i,c=j:callback(r,c))
        b[i][j].grid(row=i,column=j)

mainloop()