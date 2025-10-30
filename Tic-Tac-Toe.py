'''
Created on 2019 M04 29
@author: Manav Dharmesh Desai
'''



print("Welcome to tic tac toe in python")
print('Rules:')
print('while you input, it is row collum sequence')
print('have fun')
X = 'X'
O = 'O'
def win(rows,row2):
    if rows[0][0] == rows[0][1] and rows[0][1] == rows[0][2]:
        return True
    elif row2[0][0] == row2[0][1] and row2[0][1] == row2[0][2]:
        return True
    elif row3[0][0] == row3[0][1] and row3[0][1]  == row3[0][2]:
        return True
                                              
                                              
    
     
def display(rows,row2,row3):
    check = True
    checkers = True
    for k in range(0,3):
        if check and checkers:
            for l in range(0,3):
                print(rows[k][l], end = " ")
                check = False
                
        elif check == False:
            for l in range(0,3):
                print(row2[k][l],  end = " ")
                check = True
                checkers = False
               
        elif checkers == False:
            for l in range(0,3):
                print(row3[k][l],  end = " ")
                checkers = True
                
            
        print()
        


rows = []
for i in range(3):
    rows.append(["g","l","s"])
row2 = []
for i in range(3):
    row2.append(["v","m","g"])
row3 = []
for i in range(3):
    row3.append(["m","g","p"])





left = True
win = False
over = False
player1 = 'X'
player2 = 'O'
while win is False and over is False:
    if left:
        user = input('where to? with a space row collum ')
        input = user.split(' ')
        if input[0] == 0:
            rows[input[1]].insert(player1)
        elif input[0] == 1:
            row2[input[1]].insert(player1)
        elif input[0] == 2:
            row3[input[1]].insert(player1)
        display(rows,row2,row3)    
        win(rows,row2)
        
        not left
    else:
        user = input('where to? with a space row collum')
        input = user.split(' ')
        if input[0] == 0:
            rows[input[1]].insert(player2)
        elif input[0] == 1:
            row2[input[1]].insert(player2)
        elif input[0] == 2:
            row3[input[1]].insert(player2)
        display(rows,row2,row3)    
        win(rows,row2)
        print('lol')
        
        not left
