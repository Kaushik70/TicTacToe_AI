from tkinter import *
from tkinter import messagebox
import tkinter
from random import*
import random as r

root = Tk()
h=w=400/3
hel = 999
cp =r.choice([1,0])
players = ['AI','human']
print(players[cp])

arr = [['','',''],
       ['','',''],
       ['','','']]
board = [['A','B','C'],
       ['F','E','D'],
       ['G','H','I']]


flag = 0

def button(frame):          #Function to define a button
    b=Button(frame,padx=1,bg="BLACK",width=3,text="   ",font=('arial',60,'bold'),relief="sunken",bd=10)
    return b


b=[[],[],[]]
for i in range(3):
        for j in range(3):
                b[i].append(button(root))
                b[i][j].config(command= lambda row=i,col=j:click(row,col))
                b[i][j].grid(row=i,column=j)
label1 = Label(root, font=("Purisa",25),text="")
label1.grid()


def switch():
    global cp 
    if cp == 0:
        cp = 1
    elif cp == 1:
        cp = 0


def minimax(board,deapth,isAI):
    hel = checkWinner()
    if (hel != None):
        return hel
    elif isAI :
        bestScore = -999
        for i in range(3):
            for j in range (3):
                if arr[i][j] == '':
                    board[i][j] = 'X'
                    arr[i][j] = 1
                    score = minimax(board,deapth+1,False)
                    #print(score)
                    board[i][j] = ''
                    arr[i][j] = ''
                    if (score>bestScore):
                        #print(score,'in max')
                        bestScore = score
        #print(bestScore,'in max')
        return bestScore
    else :
        bestScore = 999
        for i in range(3):
            for j in range (3):
                if arr[i][j] == '':
                    board[i][j] = 'O'
                    arr[i][j] = 1
                    score = minimax(board,deapth+1,True)
                    board[i][j] = ''
                    arr[i][j] = ''
                    if (score<bestScore):
                        #print(score,' score in min')
                        bestScore = score
        #print(bestScore,'in min')
        return bestScore


def nextTurn(cp) :
    label1.config(text="CPU turn")
    print(cp)
    global flag
    global hel 
    hel = 999
    print("In NextTurn")
    print(players[cp])
    if flag == 0:
        if board == [[1, 2, 3], [4, 5, 6], [7, 8, 9]]:
            ibest = 0
            jbest = 0
        else:
            bestScore = -999
            #print(hel,"  hel in PC")
            for i1 in range (3):
                for j1 in range(3):
                    if (arr[i1][j1]==''):
                        print(i1,"   ",j1)
                        board[i1][j1] = 'X'
                        arr[i1][j1] = 1
                        score1 = minimax(board,0,False)
                        board[i1][j1] = ''
                        arr[i1][j1] = ''
                        if (score1>bestScore):
                            #print("here")
                            bestScore = score1
                            ibest = i1
                            jbest = j1
        #print(hel,"  hel in PC")
        
        arr[ibest][jbest]=1
        #print("herere   ",ibest,"  ",jbest)
        board[ibest][jbest] = 'X'
        #print(board)
        root.update()
        root.after(100)
        b[ibest][jbest].config(text='X',state=DISABLED,disabledforeground="BLUE")
        hel = checkWinner()
        #print(hel,"  hel in PC")
        if hel == 1:
            root.update()
            tkinter.messagebox.showinfo("Congrats!!"," 'AI' has won")
            #print("won")
            root.update()
            flag = 1
            root.after(100)
            reset(cp)
        elif hel == 0:
            tkinter.messagebox.showinfo("Congrats!!","Its a Tie")
            flag = 1
            reset(cp)
        elif hel == None:
            #print("Hereree")
            switch()
            label1.config(text="Player turn")
        #print("exit next turn \n")


def checkWinner():
    #print(players[cp])
    flaaag = 0
    for i in range(3):
        if ((board[i][0] == board[i][1] and board[i][0] == board[i][2] and board[i][2] == 'X' ) or (board[0][i] == board[1][i] and board[2][i] == board[1][i] and board[2][i] == 'X' ) or 
            (board[0][0] == board[1][1] and board[0][0] == board[2][2] and board[0][0] == 'X') or (board[0][2] == board[1][1] and board[0][2] == board[2][0] and board[0][2] == 'X')):
            #print(players[cp])
            return 1
        elif ((board[i][0] == board[i][1] and board[i][0] == board[i][2] and board[i][2] == 'O' ) or (board[0][i] == board[1][i] and board[2][i] == board[1][i] and board[2][i] == 'O' ) or 
            (board[0][0] == board[1][1] and board[0][0] == board[2][2] and board[2][2] == 'O') or (board[0][2] == board[1][1] and board[0][2] == board[2][0] and board[0][2] == 'O')): 
            return -1
        else:
            for i in range(3):
                for j in range(3):
                    if arr[i][j] == '':
                        flaaag =1 
            if flaaag == 0 :
                return 0

def reset(cp):
    print('######## in reset ##########')
    global flag
    global hel
    temp = 1
    flag = 0
    hel = 990
    for i in range(3):
        for j in range(3):
                b[i][j].config(text = " ",state = NORMAL)
                board[i][j] = temp
                temp+=1
                arr[i][j] = ''
    print(board)
    root.update()
    root.after(100)
    cp =r.choice([1,0])
    print(cp)
    hel = 990
    if cp == 0:
        print("here as CPU turn")
        label1.config(text="CPU's turn")
        print(players[cp])
        nextTurn(cp)
        print('######## out reset ##########')
    else:
        print(players[cp])
        print("here as player turn")
        label1.config(text="player turn")
        print('######## out reset ##########')

def click(row,col):
        global hel
        global flag
        #print("\n in clicked")
        #print(players[cp])
        b[row][col].config(text='O',state=DISABLED,disabledforeground="RED")
        arr[row][col] = 1
        board[row][col] = 'O'
        #print(hel,"  hel in human")
        hel = checkWinner()
        #print(hel," hel in human")
        if hel == -1:
            root.update()
            tkinter.messagebox.showinfo("Congrats!!","human has won")
            #print("won in hel -1")
            root.update()
            root.after(100)
            hel = 4
            reset(cp)
        elif hel == 0:
            tkinter.messagebox.showinfo("Congrats!!","Its a Tie")
            flag = 1
            reset(cp)
        elif hel == None:
            #print("Hereeeeeeee")
            switch()
            label1.config(text="CPU's turn")
            if flag == 0:
                nextTurn(cp)
        #print("exit click \n")



'''cp =r.choice([1,0])
if cp == 0:
    label1.config(text="CPU's turn")
    nextTurn(cp)
else:
    label1.config(text="player turn")'''
reset(cp)

root.mainloop()