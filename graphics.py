# Add the graphics (turtle) related code in this file
import turtle
import random
from main import gotiyanList
from main import validWords,alphabetScore


def displayGameOver(message):
    gameOverTurtle = turtle.Turtle()
    gameOverTurtle.hideturtle()
    gameOverTurtle.penup()
    gameOverTurtle.goto(300,-240)
    gameOverTurtle.color("red")
    gameOverTurtle.write("GAME OVER", align="center", font=("Arial", 24, "bold"))
    gameOverTurtle.goto(300,-250)
    gameOverTurtle.write(message, align="center", font=("Arial", 16, "normal"))
    
    wn.onclick(None)
    wn.onkey(None, "c")
    wn.bye()
    
def gettingScoreForEachLetter(letter):
    for letters in alphabetScore:
        if letters["alphabet"]==letter.lower():
            return letters["score"]
    return 0

def checkGameOver():
    allTurnsComplete=True
    for turn in turnsTaken:
        if turn<maxTurns:
            allTurnsComplete=False
            break
        
    if allTurnsComplete:
        displayGameOver("All players have completed their turns!")
        return True
    if len(gotiyanList)==0:
        displayGameOver("No more tiles left!")
        return True
    return False


colors = ["white", "#FFB6C1", "#90EE90", "#ADD8E6", "#FF6347", "orange"]

wn = turtle.Screen()
wn.setup(height=700, width=1000)
wn.bgcolor("black")

tut = turtle.Turtle()
tut.hideturtle()
tut.speed(0)

timerTurtle=turtle.Turtle()
timerTurtle.hideturtle()
timerTurtle.penup()
timerTurtle.goto(400,330)
timerTurtle.color("orange")

playerTurtle = turtle.Turtle()
playerTurtle.hideturtle()
playerTurtle.speed(0)

checkingTurtle=turtle.Turtle()
checkingTurtle.hideturtle()
checkingTurtle.speed(0)

scoreTut = turtle.Turtle()
scoreTut.hideturtle()
scoreTut.speed(0)


cellSize=40
gridSize=15
gap=1
board = [[None for j in range(gridSize)] for i in range(gridSize)]
player1 = [None for i in range(7)]
player2 = [None for i in range(7)]
player3 = [None for i in range(7)]
player4 = [None for i in range(7)]

scores=[0,0,0,0]
turnsTaken = [0, 0, 0, 0]
maxTurns = 5

valueCopied=None
currentPlayer=1
copyMode=True
Timer=90
indexOfPlayerTile=None


def writingInSquare(value,color):
    tut.begin_fill()
    for _ in range(4):
        tut.forward(cellSize)
        tut.right(90)
    tut.end_fill()
    tut.penup()
    tut.forward(cellSize / 2)
    tut.right(90)
    tut.forward(cellSize / 2)
    tut.color(color)
    tut.write(value, align="center", font=("Arial", 12, "normal"))
    tut.backward(cellSize / 2)
    tut.left(90)
    tut.backward(cellSize / 2)
    tut.pendown()
def writingInSquare2(x,y,value,color):
    
    tut.goto(x,y)
    tut.penup()
    tut.begin_fill()
    for _ in range(4):
        tut.forward(cellSize)
        tut.right(90)
    tut.end_fill()
    tut.forward(cellSize / 2)
    tut.right(90)
    tut.forward(cellSize / 2)
    tut.color(color)
    tut.write(value, align="center", font=("Arial", 12, "normal"))
    tut.backward(cellSize / 2)
    tut.left(90)
    tut.backward(cellSize / 2)
    tut.pendown()
    print("Pasted on grid")
    
def moveToNextRow():
    tut.penup()
    tut.backward((cellSize + gap) * gridSize)
    tut.right(90)
    tut.forward(cellSize + gap)
    tut.left(90)
    
def drawingSquare(x,y,color):
    tut.penup()
    tut.goto(x, y)
    tut.pendown()
    tut.color("black", color)
    tut.begin_fill()
    for _ in range(4):
        tut.forward(cellSize)
        tut.right(90)
    tut.end_fill()
    
coordinatesForTheGrid = [[None for j in range(gridSize)] for i in range(gridSize)]
originalColorsOfMyGrid = [[None for j in range(gridSize)] for i in range(gridSize)]
coordsForP1=[]
coordsForP2=[]
coordsForP3=[]
coordsForP4=[]
tut.penup()
tut.goto(-500,300)
initVal='__'
def drawingGrid():
    for i in range(gridSize):
        for j in range(gridSize):
            x,y=tut.position()
            coordinatesForTheGrid[i][j]=(x,y)
            color=random.choice(colors)
            originalColorsOfMyGrid[i][j]=color
            board[i][j]=initVal
            drawingSquare(tut.xcor(),tut.ycor(),color)
            tut.penup()
            tut.forward(cellSize+gap)
        moveToNextRow()

def takingCoordsForPlayer(x,y,coords):
   coords.append((x,y))
    
def takingInputFromUser(initX,initY,coords,player):
    gap2=2
    message = wn.textinput("Input", "Enter your name:")
    tut.goto(initX,initY)
    tut.color("#FF0000")
    tut.write(message,align="center", font=("Arial", 11, "normal"))
    for i in range(7):
        x,y=tut.position()
        takingCoordsForPlayer(x, y, coords)
        color="white"
        if len(gotiyanList)>0:
            tile=random.choice(gotiyanList)
            gotiyanList.remove(tile)
            player[i]=tile
        else:
            player[i]=None
            
        drawingSquare(tut.xcor(),tut.ycor(),color)
        writingInSquare(player[i],"#000000")
        tut.penup()
        tut.forward(cellSize+gap)
        
def copyingFromTheTiles(x,y):
    global valueCopied
    global currentPlayer
    global copyMode
    global indexOfPlayerTile
    if not copyMode:
        return
    
    tempCords=[]
    tempPlayer=[]
    
    if currentPlayer==1:
        tempCords=coordsForP1
        tempPlayer=player1
        
    elif currentPlayer==2:
        tempCords=coordsForP2
        tempPlayer=player2
        
    elif currentPlayer==3:
        tempCords=coordsForP3
        tempPlayer=player3
        
    elif currentPlayer==4:
        tempCords=coordsForP4
        tempPlayer=player4
    
    for i in range(len(tempCords)):
        topLeftXOfSq,topLeftYOfSq=tempCords[i] 
       
        if topLeftXOfSq<=x<=topLeftXOfSq+cellSize and topLeftYOfSq-cellSize<=y<=topLeftYOfSq:
            valueCopied=tempPlayer[i]
            indexOfPlayerTile=i
            print("Copied value is",valueCopied)
            copyMode=False
            return
        
        
def eraseTile(coords,player,index):
    x,y=coords[index]
    drawingSquare(x,y,"black")
    player[index]=None
    midX=x+cellSize/2          
    midY=y-cellSize/2
    tut.penup()
    tut.goto(midX,midY)
    tut.write("", align="center", font=("Arial", 12, "normal"))
    
currentCoordinatesOfGrid=[]              
def pastingOnTheBoard(x,y):
    global valueCopied
    global copyMode
    global indexOfPlayerTile
    if copyMode:
        return
    if valueCopied is not None:
        for i in range(gridSize):
            for j in range(gridSize):
                topLeftXOfSq,topLeftYOfSq=coordinatesForTheGrid[i][j]
               
                if topLeftXOfSq<=x<=topLeftXOfSq+cellSize and topLeftYOfSq-cellSize<=y<=topLeftYOfSq:
                    currentCoordinatesOfGrid.append((topLeftXOfSq,topLeftYOfSq))
                    
                    if board[i][j] != "__":
                        print("This cell is already occupied!")
                        checkingTurtle.clear()
                        checkingTurtle.penup()
                        checkingTurtle.goto(300, -190)
                        checkingTurtle.pendown()
                        checkingTurtle.color("red")
                        checkingTurtle.write("This cell is already occupied!", align="center", font=("Arial", 16, "normal"))
                        wn.ontimer(clearMessage, 2000)
                        return
                    
                    color = originalColorsOfMyGrid[i][j]
                    board[i][j]=valueCopied
                    drawingSquare(topLeftXOfSq,topLeftYOfSq,color)
                    writingInSquare2(topLeftXOfSq,topLeftYOfSq,valueCopied,"#000000")
                    if currentPlayer==1:
                        eraseTile(coordsForP1,player1,indexOfPlayerTile)
                    elif currentPlayer==2:
                        eraseTile(coordsForP2,player2,indexOfPlayerTile)
                    elif currentPlayer==3:
                        eraseTile(coordsForP3,player3,indexOfPlayerTile)
                    elif currentPlayer==4:
                        eraseTile(coordsForP4,player4,indexOfPlayerTile)
                    
                    valueCopied=None
                    copyMode=True
                    break
        
def moveToNextPlayer():
    global currentPlayer
    global Timer
    
    turnsTaken[currentPlayer-1]+=1
    
    if checkGameOver():
        return
    
    currentPlayer+=1
    if currentPlayer>4:
        currentPlayer=1
    Timer=90
    print(f"Switching to Player {currentPlayer}")
    playerTurtle.clear()
    checkingTurtle.clear()
    playerTurtle.penup()
    playerTurtle.goto(300,-160)
    playerTurtle.pendown()
    playerTurtle.color("red")
    playerTurtle.write(f"Player {currentPlayer}'s turn", align="center", font=("Arial", 16, "normal"))
    
    wn.update()
    
    wn.ontimer(moveToNextPlayer, 90000)  
    
def updatingMyTimer():
    global currentPlayer
    global Timer
    if Timer>0:
        Timer-=1
        timerTurtle.clear()
        timerTurtle.write(f"Time left: {Timer} seconds", align="center", font=("Arial", 16, "normal"))
        
        wn.ontimer(updatingMyTimer, 1000)
    else:
        moveToNextPlayer()

def checkIfWordIsValid(arr,word):
    start=0
    end=len(arr)-1
    while start<=end:
        mid=(start+end)//2
        if arr[mid] <word:
            start=mid+1
        elif arr[mid]>word:
            end=mid-1
        else:
            return mid
    return -1
    
    
def checkingWordInGridHorizontallY(x,y):
    row,col=None,None
    for i in range(gridSize):
            for j in range(gridSize):
                topLeftXOfSq,topLeftYOfSq=coordinatesForTheGrid[i][j]
               
                if topLeftXOfSq<=x<=topLeftXOfSq+cellSize and topLeftYOfSq-cellSize<=y<=topLeftYOfSq:
                    row=i
                    col=j
                    break
            if row is not None:
                break
            
    if row is None or col is None:
        return
    
    word=[]
    StartingCol=col
    while StartingCol>0 and board[row][StartingCol-1]!="__":
        StartingCol-=1
    
    EndingCol=col
    while EndingCol<gridSize-1 and board[row][EndingCol+1]!="__":
        EndingCol+=1
    
    for i in range(StartingCol,EndingCol+1):
        if board[row][i]!="__":
            word.append(board[row][i])
        
    wordFormed=''.join(word)
    print(f"word horizontally found: {wordFormed}")
    check=checkIfWordIsValid(validWords,wordFormed)
    if check!=-1:
        updatingTheScoreBasedOnWord(wordFormed)
        return wordFormed
    else:
        return None
    
        

def checkingWordInGridVertically(x,y):
    row,col=None,None
    for i in range(gridSize):
            for j in range(gridSize):
                topLeftXOfSq,topLeftYOfSq=coordinatesForTheGrid[i][j]
               
                if topLeftXOfSq<=x<=topLeftXOfSq+cellSize and topLeftYOfSq-cellSize<=y<=topLeftYOfSq:
                    row=i
                    col=j
                    break
            if row is not None:
                break
            
    if row is None or col is None:
        return
    
    word=[]
    StartingRow=row
    EndingRow=col
    
    while StartingRow>0 and board[StartingRow-1][col]!="__":
        StartingRow-=1
    
    while EndingRow<gridSize-1 and board[StartingRow+1][col]!="__":
        EndingRow+=1
    
    for i in range(StartingRow,EndingRow+1):
        if board[i][col]!="__":
            word.append(board[i][col])
            
    wordFormed=''.join(word)
    print(f"Word vertically found: {wordFormed}")
    
    check=checkIfWordIsValid(validWords,wordFormed)
    if check!=-1:
        updatingTheScoreBasedOnWord(wordFormed)
        return wordFormed
    else:
        return None

def movingTilesBackToTheirRack(coordList):
    global currentPlayer
    tempCoordsOfPlayer=[]
    tempPlayer=[]
    
    if currentPlayer == 1:
        tempCoordsOfPlayer = coordsForP1
        tempPlayer = player1
    elif currentPlayer == 2:
        tempCoordsOfPlayer = coordsForP2
        tempPlayer = player2
    elif currentPlayer == 3:
        tempCoordsOfPlayer = coordsForP3
        tempPlayer = player3
    elif currentPlayer == 4:
        tempCoordsOfPlayer = coordsForP4
        tempPlayer = player4
    
    for coord in coordList:
        boardX,boardY=coord
        foundTile=False
        for i in range(gridSize):
            for j in range(gridSize):
                
                topLeftXOfSq,topLeftYofSq=coordinatesForTheGrid[i][j]
                if topLeftXOfSq<=boardX<=topLeftXOfSq+cellSize and topLeftYofSq-cellSize<=boardY<=topLeftYofSq:
                    boardX=i
                    boardY=j
                    foundTile=True
                    break
            if foundTile:
                break
        
        titleVal=board[boardX][boardY]
        
        if titleVal=="__":
            continue
        
        for i in range(len(tempPlayer)):
            if tempPlayer[i] is None:
               
                tempPlayer[i]=titleVal
                
                playerTileX,playerTileY=tempCoordsOfPlayer[i]
                
                drawingSquare(playerTileX, playerTileY, "white")  
                writingInSquare2(playerTileX,playerTileY,tempPlayer[i],"black")  
                
                board[boardX][boardY]="__"
                xCord,yCord=coordinatesForTheGrid[boardX][boardY]
               
                
                drawingSquare(xCord,yCord,originalColorsOfMyGrid[boardX][boardY])
                break
            
            
def gettingNewTilesForPlayerRack():
    global currentPlayer
    tempCoordsOfPlayer=[]
    tempPlayer=[]
    
    if currentPlayer == 1:
        tempCoordsOfPlayer = coordsForP1
        tempPlayer = player1
    elif currentPlayer == 2:
        tempCoordsOfPlayer = coordsForP2
        tempPlayer = player2
    elif currentPlayer == 3:
        tempCoordsOfPlayer = coordsForP3
        tempPlayer = player3
    elif currentPlayer == 4:
        tempCoordsOfPlayer = coordsForP4
        tempPlayer = player4
    for i in range(len(tempPlayer)):
        if tempPlayer[i] is None:
           if len(gotiyanList)>0:
                tile=random.choice(gotiyanList)
                gotiyanList.remove(tile)
                tempPlayer[i]=tile
                playerTileX,playerTileY=tempCoordsOfPlayer[i]
                drawingSquare(playerTileX, playerTileY, "white")  
                writingInSquare2(playerTileX,playerTileY,tempPlayer[i],"black")
           else:
               print("No more tiles left in the gotiyan List")
               break
            
            
        
def updatingTheScoreBasedOnWord(word):
    
    global currentPlayer
    totalScore=0
    for letter in word:
        letterScore=gettingScoreForEachLetter(letter)
        totalScore+=letterScore
    
    scores[currentPlayer-1]+=totalScore
    m=f"Score for player{currentPlayer} is {scores[currentPlayer-1]}"
   
    
   
    scoreTut.penup()
    scoreTut.goto(300,-200)
    scoreTut.pendown()
    scoreTut.color("red")
    scoreTut.clear()
    scoreTut.write(m, align="center", font=("Arial", 16, "normal"))
    wn.ontimer(clearMessage,5000)
        
def checkingForWord(coordList):
    checkingTurtle.clear()  
    validWord = False
    for coord in coordList:
        x,y=coord
        
        wordFormed=checkingWordInGridHorizontallY(x,y)
        if wordFormed:
            checkingTurtle.penup()
            checkingTurtle.goto(300, -190)
            checkingTurtle.pendown()
            checkingTurtle.color("red")
            checkingTurtle.write(f"Valid word formed: {wordFormed}", align="center", font=("Arial", 16, "normal"))
            wn.ontimer(clearMessage, 5000)
            gettingNewTilesForPlayerRack()
            moveToNextPlayer()
            currentCoordinatesOfGrid.clear()
            return  
        wordFormed=checkingWordInGridVertically(x,y)
        if wordFormed:
            checkingTurtle.penup()
            checkingTurtle.goto(300, -190)
            checkingTurtle.pendown()
            checkingTurtle.color("red")
            checkingTurtle.write(f"Valid word formed: {wordFormed}", align="center", font=("Arial", 16, "normal"))
            wn.ontimer(clearMessage, 5000)
            gettingNewTilesForPlayerRack()
            moveToNextPlayer()
            currentCoordinatesOfGrid.clear()
            return  
    
    checkingTurtle.penup()
    checkingTurtle.goto(400, -180)
    checkingTurtle.pendown()
    checkingTurtle.color("red")
    checkingTurtle.write("No valid word formed!", align="center", font=("Arial", 16, "normal"))
    wn.ontimer(clearMessage, 5000)
    movingTilesBackToTheirRack(coordList)
    moveToNextPlayer()
    currentCoordinatesOfGrid.clear()
        
        
        
       
def clearMessage():
    checkingTurtle.clear()
def clearScoreDisplay():
    scoreTut.clear()
        
def checkGridWhenButtonPressed():
    checkingForWord(currentCoordinatesOfGrid)
    print("C is pressed!,verifying the word")
    currentCoordinatesOfGrid.clear()

drawingGrid()

takingInputFromUser(300,300,coordsForP1,player1)
takingInputFromUser(300,200,coordsForP2,player2)
takingInputFromUser(300,100,coordsForP3,player3)
takingInputFromUser(300,0,coordsForP4,player4)

wn.onclick(copyingFromTheTiles, btn=1)  
wn.onclick(pastingOnTheBoard, btn=3)    

wn.ontimer(updatingMyTimer, 1000)
wn.ontimer(moveToNextPlayer, 90000)  


wn.listen()
wn.onkey(checkGridWhenButtonPressed,"c")


wn.update()
wn.mainloop()
