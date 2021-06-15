from tkinter import *
from random import*
h=w=400/3
arr = [['','',''],
       ['','',''],
       ['','','']]
board = [['A','B','C'],
       ['B','E','F'],
       ['I','H','G']]

i=0
j=0
depth=9
flag = 0
currentPlayer=1

'''
def clicked(currentPlayer):
    nextTurn(currentPlayer,depth,0,0,flag)
    currentPlayer=0
'''


root = Tk()
root.geometry("400x450")
c = Canvas(root,bg="Blue",height=400,width=400)
c.create_line(0, h, 400, h,width = 4)
c.create_line(0, h*2, 400, h*2,width = 4)
c.create_line(w, 0, w, 400,width = 4)
c.create_line(w*2, 0, w*2, 400,width = 4)
#bt = Button(root,text="enter",command=clicked)
#bt.pack()

c.pack()



def checkWinner():
    for i in range(3):
        if ((board[i][0] == board[i][1] and board[i][0] == board[i][2]) or (board[0][i] == board[1][i] and board[2][i] == board[1][i]) or 
            (board[0][0] == board[1][1] and board[0][0] == board[2][2]) or (board[0][2] == board[1][1] and board[0][2] == board[2][0])):
            return(True)


def nextTurn(currentPlayer,depth,i,j,flag) :
    if (depth!=0 and flag == 0):
        if  (currentPlayer == 1):
            i = randint(0,2)
            j = randint(0,2)
            if (arr[i][j]==1):
                while(arr[i][j]==1):
                    i = randint(0,2)
                    j = randint(0,2)
            arr[i][j]=1
            print(board)
            root.update()
            c.after(1000)
            c.create_text(j*w + h/2,i*h + h/2 , font=("Purisa",55),text="X")
            board[i][j]='X'
            if (checkWinner() == True) :
                label1 = Label(root, font=("Purisa",25),text="Winner is X")
                label1.pack()
                flag = 1
            currentPlayer = 0
            depth=depth-1
            c.after(100,nextTurn(currentPlayer,depth,0,0,flag))
        else :
            i = randint(0,2)
            j = randint(0,2)
            if (arr[i][j]==1):
                while(arr[i][j]==1):
                    i = randint(0,2)
                    j = randint(0,2)
            arr[i][j]=1
            print(board)
            root.update()
            c.after(1000)
            c.create_text(j*w + h/2,i*h + h/2 , font=("Purisa",55),text="O")
            board[i][j]='O'
            if (checkWinner() == True) :
                label2 = Label(root, font=("Purisa",25),text="Winner is O")
                label2.pack()
                flag = 1
            currentPlayer = 1
            depth=depth -1
            c.after(100,nextTurn(currentPlayer,depth,0,0,flag))
    elif(depth==0 and flag == 0):
        label2 = Label(root, font=("Purisa",25),text="TIE")

nextTurn(currentPlayer,depth,0,0,flag)
root.mainloop()



'''
for i in range(3):
    for j in range(3):
        if (arr[i][j] == 'X'):
            c.create_text(j*w + h/2,i*h + h/2 , font=("Purisa",55),text="X")
            print("here")
        elif (arr[i][j] =='O'):
            c.create_text(j*w + h/2,i*h + h/2 , font=("Purisa",55),text="O")
            print("here")
'''
