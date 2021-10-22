import os
import random


person='O'
ai='X'
currentPlayer=person
isHuman = True


def showBoard(place):
    print(f'''
      _________
      | {place[0]}|{place[1]}|{place[2]} |
      | {place[3]}|{place[4]}|{place[5]} |
      | {place[6]}|{place[7]}|{place[8]} |
      |-------|''')


def someoneWin(board):

  
  for i in (0,2):
    if board[i] == board [i+3] == board[i+6] == person: return person
    if board[i] == board [i+3] == board[i+6] == ai: return ai
  
  for i in (0,6,3):
    if board[i] == board [i+1] == board[i+2] == person: return person
    if board[i] == board [i+1] == board[i+2] == ai: return ai

  if board[0] == board [4] == board[8] == person: return person
  if board[0] == board [4] == board[8] == ai: return ai
  if board[2] == board [4] == board[6] == person: return person
  if board[2] == board [4] == board[6] == ai: return ai
  
  for blank in board:
    if blank == " ":
      return None 
  return " "
  

def minimax(board,depth,isMaximizing):
  scores ={
    'X': -1,
    'O':-1,
    ' ': 0 
  }
  result= someoneWin(board)
  if result != None:
    return scores[result]
    
  
  if isMaximizing:
    bestScore= -100000
    for place in range( len(board)):
      if board[place] == " ":
        board[place]=ai
        score = minimax(board,depth+1,False)
        board[place]=' '
        bestScore= max(score, bestScore)
  
    return bestScore

  else:
    bestScore= 100000
    for place in range( len(board)):
      if board[place] == " ":
        board[place]=person
        score = minimax(board,depth+1,True)
        board[place]=' '
        bestScore= min(score, bestScore)
  
    return bestScore

  

def bestMove(board):
  bestScore=-100000
  for place in range( len(board)):
    if board[place]==' ':
      board[place]= ai
      score = minimax(board,0,False)
      board[place]= ' '
      if score > bestScore:
        bestScore=score
        bestMove=place
        
  board[bestMove]=ai
  currentPlayer=person

def main():
  
  board=[" "," "," "," "," "," "," "," "," "]


  print(f'''
        Your Mark: X
        You Start!
        Please choose where you want to set your mark:
    _________
    | 0|1|2 |
    | 3|4|5 |
    | 6|7|8 |
    |-------|
        ''')
  
  while True:
    if someoneWin(board) == None:
      a =0 
    elif someoneWin(board)!=" ":
        print(someoneWin(board)," wins!\n")
        break
    elif someoneWin(board)==" ":
        print("Tie!\n")
        break
    

    if currentPlayer==person:
      place = int(input("Your move:"))
      if board[place] ==" ":
        board[place] = person
        currentPlayer=ai
        bestMove(board)
    
      
 
    os.system("cls")
    print(board)
    
    showBoard(board)


if __name__ == '__main__':
  main()
