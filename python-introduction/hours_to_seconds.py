hours = int(input("Enter the number of hours: "))
seconds = hours * 3600
hour_label = "hour" if hours == 1 else "hours"

print(hours, hour_label, "is", seconds, "seconds.")