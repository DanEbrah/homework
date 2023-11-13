'''def board():
    layout_numlist = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']

    TicTacToe = [
            "",
            '    ' + layout_numlist[0] + ' | ' + layout_numlist[1] + ' | ' + layout_numlist[2],
            "    -----------",
            '     ' + layout_numlist[3] + ' | ' + layout_numlist[4] + ' | ' + layout_numlist[5],
            "    -----------",
            '3    ' + layout_numlist[6] + ' | ' + layout_numlist[7] + ' | ' + layout_numlist[8]
            ]

    for row in TicTacToe:
                print(''.join(row))
                

board()
'''

'''
n= 5
layout = [['', '', ''], ['', '', ''], ['', '', '']]
for n in layout:
    if n < 3: 
        n + 1
        print(layout) '''

'''
layout = ['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']
n=3 

for i in range(n):
    r = []
    for i in range(n):
        r.append('-')
        layout.append(r)
        print(layout) '''



'''
layout = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
n = 5
for n in range(2):
    print("\n --- --- ---")
    if n != 5:
        n + 1
        print(n)
    elif n == 5:
        print("board complete")
    
'''





'''
Hint hint:
- store your data points, including `-` and `|` and empty space `" "` into a 2D list/array
- figure out how many columns & row you need (as an equation) to figure out the size of your 2D list/array
- figure out the 4 center points coordinate as you have higher `n`
- figure out where to place your columns + rows
- join all the data points of your 2D list array together, split lines where you need to split lines
'''




n = 2
for i in range(n):
    print(n * " " + "|" + n * " " + "|" + n * " ")
    print ((2 + 3 * n) * "-")


    


    

