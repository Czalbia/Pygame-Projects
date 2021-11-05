import os
import random
import visual

board=[' ',' ',' ',' ',' ',' ',' ',' ',' ']
if random.randint(1,2)==1:
      person = 'X'
      ai = 'O'
else: 
  ai='X'
  person = 'O'

def checkPosition():
    while True:
        pos=visual.pygame.mouse.get_pos()
        x = pos[0]
        y = pos[1]
        for event in visual.pygame.event.get():
            if event.type == visual.pygame.QUIT:
                exit()
            if event.type == visual.pygame.MOUSEBUTTONDOWN:
                if x>0 and x <240 and y<240:
                    return 0
                if x>240 and x<480 and y<240:
                    return 1
                if x>480 and x<720 and y<240:
                    return 2
                if x>0 and x <240 and y>240 and y<480:
                    return 3
                if x>240 and x<480 and y>240 and y<480:
                    return 4
                if x>480 and x<720 and y>240 and y<480:
                    return 5

                if x>0 and x <240 and y>480 and y<720:
                    return 6
                if x>240 and x<480 and y>480 and y<720:
                    return 7
                if x>480 and x<720 and y>480 and y<720:
                    return 8

def someoneWin():

  for i in (0,2,1):
    if board[i] == board [i+3] == board[i+6] == person: 
      return person
    if board[i] == board [i+3] == board[i+6] == ai: 
      return ai
  
  for i in (0,6,3):
    if board[i] == board [i+1] == board[i+2] == person: 
      return person
    if board[i] == board [i+1] == board[i+2] == ai: 
      return ai

  if board[0] == board [4] == board[8] == person: 
    return person
  if board[0] == board [4] == board[8] == ai: 
    return ai
  if board[2] == board [4] == board[6] == person: 
    return person
  if board[2] == board [4] == board[6] == ai: 
    return ai
  
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
  iter =1 
  if person=='X':
    visual.showText("You start!")
  else:
    visual.showText("Computer starts!")
  while True:
    visual.main(board)
    result = someoneWin()
    if result==person:
        visual.showWinner(person)
        break
    if result==ai:
        visual.showWinner(ai)
        break
    if result=='t':
        visual.showTie()
        break

    if person == 'X':
      if iter %2!=0:
        place = checkPosition()
        if board[place] ==' ':
          board[place] = person
        else: continue   
      else:
        bestMove()
    if person == 'O':
      if iter %2==0:
        place = checkPosition()
        if board[place] ==' ':
          board[place] = person
        else: continue 
      else:
        bestMove()

    iter +=1

if __name__ == '__main__':
  main()
