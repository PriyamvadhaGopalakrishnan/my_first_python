def main():
    board = Board()
    turn='X'
    playing= True
    while(playing):
        board.print_board()
        print("it's your turn, " + turn)
        x= int(input("x position? "))
        y= int(input("y position? "))
        board.set_piece(x,y,turn)
        
        if turn == 'X':
            turn= 'O'

        else:
            turn = 'X'
        
class Board:
    def __init__(self):
        self._layout=[['_','_','_'],['_','_','_'],['_','_','_']]

    def print_board(self):
        for i in range(0,len(self._layout)):
            for j in range(0,len(self._layout[i])):
                print(self._layout[i][j]+" ",end='')
            print()

    def set_piece(self,x,y,turn):
        self._layout[y][x] = turn
main()
