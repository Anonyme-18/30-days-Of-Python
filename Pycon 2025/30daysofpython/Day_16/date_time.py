from datetime import datetime, timedelta

#Get the current day, month, year, hour, minute, and timestamp
now = datetime.now()
print("Current day:", now.day)
print("Current month:", now.month)
print("Current year:", now.year)
print("Current hour:", now.hour)
print("Current minute:", now.minute)
print("Current timestamp:", now.timestamp())
print()

#Format the current date
formatted_date = now.strftime("%m/%d/%Y, %H:%M:%S")
print("Formatted current date:", formatted_date)
print()

#Convert a given date string to a datetime object
date_string = "5 December, 2019"
converted_date = datetime.strptime(date_string, "%d %B, %Y")
print(f"Converted '{date_string}' to datetime object:", converted_date)
print()

#Calculate time difference between now and next New Year
next_new_year = datetime(year=now.year + 1, month=1, day=1)
time_to_new_year = next_new_year - now
print(f"Time remaining until New Year {next_new_year.year}:", time_to_new_year)
print()

#Calculate time difference between 1 January 1970 and now
epoch_start = datetime(year=1970, month=1, day=1)
time_since_epoch = now - epoch_start
print("Time elapsed since January 1, 1970:", time_since_epoch)
print()

#Examples of datetime module usage
print("Possible uses of the datetime module:")
print("- Time series analysis (e.g., stock prices over time)")
print("- Logging timestamps for user activities in an application")
print("- Scheduling content publishing (e.g., blog posts, social media)")
print("- Calculating deadlines and reminders")
print("- Tracking events in scientific experiments")
