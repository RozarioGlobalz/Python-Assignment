def average(number_one, *numbers):

    total = number_one

    for number in numbers:
    
        total += number
    
    count = 1 + len(numbers)

    return total / count


print(average(10, 5))
print(average(10, 20, 40, 50))
