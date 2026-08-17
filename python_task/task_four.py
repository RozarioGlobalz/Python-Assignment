def fahrenheit(celsius):

    fahrenheit = (9 / 5) * celsius + 32

    return fahrenheit

print("celsius  fahrenheit")
    
for celsius in range(0, 101):

    print(f"{celsius: > 7}  {fahrenheit(celsius): }")
