# dictionary comprehension

weather = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24,
}

weather_F = {day: (temp*9/5)+32 for (day,temp) in weather.items()}
print(weather_F)