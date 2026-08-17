def seconds_since_midnight(minutes, hours, seconds):
   
    hours_in_seconds = hours * 3600
    minutes_in_second = minutes * 60
    return hours_in_seconds +  minutes_in_second  + seconds   


total_seconds = seconds_since_midnight(1,2,3)



print(total_seconds)
