exit = 'no'

while exit != 'yes':

    balance = 1000

    deposit = int (input ('Enter amount you want to deposit: '))

    balance = balance + deposit

    withdraw = int (input ('Enter amount you want to withdraw:'))

    if withdraw > balance:

        print( 'insufficient funds')

    elif withdraw <= balance:

        balance = balance - withdraw

        print(' your balance is: ',balance)

        exit = input ('enter choice: ')
