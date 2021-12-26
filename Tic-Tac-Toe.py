board = [ ] 

for i in range(0,3):
  board.append([ ])
  for j in range(0,3):
    board[i].append('-')



def boardPrint():
  for i in range(0,3,1):#height
    for j in range(0, 3 ,1):#width
      print (board[i][j], end = ' ') 
    print()

  
boardPrint()


#now we want to loop the turns
#make a safe input function where is anything but 0,1,2 is entered, it prints an error
activePlayer = 'X'

def safeInput(prompt):
  while(True):
    temp = input(prompt)
    if temp == '1' or temp == '2' or temp == '3': 
      return int(temp) - 1
    
    else: 
      print('Error, not a valid move')
      





for turn in range(0,8):
  #if active player is x then swap to o
  
  r = safeInput(activePlayer +' turn,row(Height)')
  c = safeInput(activePlayer +' turn,column(Width)') 

  if board[r][c] == '-':
    

    board[r][c]= activePlayer

    boardPrint()

    if board[0][0] == board[1][1] == board[2][2] == activePlayer: 
      print(activePlayer + ' has won the game!!!')

      break

    if board[0][2] == board[1][1] == board[2][0] == activePlayer:
      print(activePlayer + ' has won the game!!!')

      break

    if board[r][0] == board[r][1] == board[r][2] == activePlayer:
      print(activePlayer + ' has won the game!!!')

      break

    if board[0][c] == board[1][c] == board[2][c] == activePlayer:
      print(activePlayer + ' has won the game!!!')

      break
    
    
    if activePlayer == 'X':#asking if its equal
      activePlayer = 'O'#assigning it equal 

    elif activePlayer == 'O':#asking if its equal
      activePlayer = 'X'#assigning it equal
  
  elif not board[r][c] == '-':
    print('Cannot Move Here')

