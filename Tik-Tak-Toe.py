'''
Created on 2019 M04 29

@author: Manav Desai
'''

#tic tac toe frenzy (might change the name later)

print("Welcome to tic tac toe frenzy")
print('Rules:')
print('while you input, it is row collum sequence')
print('have fun')
X = 'X'
O = 'O'
def win(rows,collums):
    if rows[0][0] is X and rows[0][1] is X and rows[0][2]:
        return True
     



# actual game
rows = []
for i in range(3):
    rows.append([])
collums = []
for i in range(3):
    collums.append([])
left = True
win = False
over = False
player1 = 'X'
player2 = 'O'
while win is False and over is False:
    if left:
        user = input('where to? with a space row collum ')
        input = user.split(' ')
        rows.insert(input[1],player1)
        collums.insert(input[0],player1)
        win(rows,collums)
        
        not left
    else:
        user = input('where to? with a space row collum')
        input = user.split(' ')
        rows.insert(input[1],player2)
        collums.insert(input[0],player2)
        win(rows,collums)
        
        not left