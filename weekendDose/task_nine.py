loop_number_of_time = int(input ('Enter number of times you want:'))

total = 0

for count in range (1, loop_number_of_time +1):

    number = int (input( 'enter number:'))

total += number

average = total /number

print ('average of the numbers is' ,average)
