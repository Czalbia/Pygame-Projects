import os
import random

board=[' ',' ',' ',' ',' ',' ',' ',' ',' ']

if random.randint(1,2)==1:
      person = 'X'
      ai = 'O'
else: 
  ai='X'
  person = 'O'



def showBoard(place):
    print(f'''
  _________
  | {place[0]}|{place[1]}|{place[2]} |
  | {place[3]}|{place[4]}|{place[5]} |
  | {place[6]}|{place[7]}|{place[8]} |
  |-------|''')

def someoneWin():

  for i in (0,2,1):
    if board[i] == board [i+3] == board[i+6] == person: return person
    if board[i] == board [i+3] == board[i+6] == ai: return ai
  
  for i in (0,6,3):
    if board[i] == board [i+1] == board[i+2] == person: return person
    if board[i] == board [i+1] == board[i+2] == ai: return ai

  if board[0] == board [4] == board[8] == person: return person
  if board[0] == board [4] == board[8] == ai: return ai
  if board[2] == board [4] == board[6] == person: return person
  if board[2] == board [4] == board[6] == ai: return ai
  
  blanks =0
  for blank in board:
    if blank == ' ':
      blanks+=1
      
  if blanks ==0: 
    return 't'

  return None

def minimax(depth,isMaximizing):
  if person == 'O':
    scores ={
      'X': +1,
      'O':-1,
      't': 0
    }
  if person =='X':
        scores ={
      'X': -1,
      'O':+1,
      't': 0
    }
  result= someoneWin()
  if result != None:
    return scores[result]
    
  
  if isMaximizing:
    bestScore= -1000000
    for place in range( len(board)):
      if board[place] == ' ':
        board[place]=ai
        score = minimax(depth+1,False)
        board[place]=' '
        bestScore= max(score, bestScore)
  
    return bestScore

  else:
    bestScore= 1000000
    for place in range( len(board)):
      if board[place] == ' ':
        board[place]=person
        score = minimax(depth+1,True)
        board[place]=' '
        bestScore= min(score, bestScore)
  
    return bestScore

def bestMove():
  bestScore=-100000
  move=0
  for place in range( len(board)):
    if board[place]==' ':
      board[place]= ai
      score = minimax(0,False)
      board[place]= ' '
      if score > bestScore:
        bestScore=score
        move=place
        
  board[move]=ai

def main():
  if person == 'X':
        print(f'''
        Your Mark: {person}
        You are going First!
        Please choose where you want to set your mark:
    _________
    | 0|1|2 |
    | 3|4|5 |
    | 6|7|8 |
    |-------|
        ''')
  else: print(f'''
        Your Mark: {person}
        You are going Second!
        Please choose where you want to set your mark:
    _________
    | 0|1|2 |
    | 3|4|5 |
    | 6|7|8 |
    |-------|
        ''')
  iter =1 
  while True:
    
    if someoneWin() == None:
      pass
    elif someoneWin()!='t':
        print(someoneWin()," wins!\n")
        break
    elif someoneWin()=='t':
        print("Tie!\n")
        break

    if person == 'X':
      if iter %2!=0:
        place = int(input("Your move:"))
        if board[place] ==' ':
          board[place] = person
        else: continue   
      else:
        bestMove()

    if person == 'O':
      if iter %2==0:
        place = int(input("Your move:"))
        if board[place] ==' ':
          board[place] = person
        else: continue 
      else:
        bestMove()
    
    os.system("clear")
    print(board)
    print('''
  _________
  | 0|1|2 |
  | 3|4|5 |
  | 6|7|8 |
  |-------|''')
    showBoard(board)
    iter +=1


if __name__ == '__main__':
  main()
