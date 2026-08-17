def temperature_checker(temp):

    unit = input("Enter unit")
    celsius = 0
    fahrenheit = 0
    thrshold = 70

    if(unit == "c"):
        fahrenheit = (temperature * 5/9) + 32
        if (fahrenheit > threshold):
              return " cold Advisory "
        else: 
               return " heat Alert" 
    elif(unit ==  "f"):
        celsius = (temperature - 32) * 5/9
        if (celsius < threshold):
               return " cold Advisory "
        else: 
               return " heat Alert" 

temperature = float(input("Enter temperature:"))
print(temperature_checker(temp))

