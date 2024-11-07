'''
Python Dates

A date in Python is not a data type of its own, but we can import a module named datetime to work with dates as date objects.
Example

Import the datetime module and display the current date:
'''
import datetime

x = datetime.datetime.now()
print(x) 


'''
Date Output

When we execute the code from the example above the result will be:
2022-10-24 02:20:23.885155

The date contains year, month, day, hour, minute, second, and microsecond.

The datetime module has many methods to return information about the date object.
'''
# Return the year and name of weekday:
import datetime

x = datetime.datetime.now()

print(x.year)
print(x.strftime("%A"))


# Display the name of the month:
import datetime

x = datetime.datetime(2018, 6, 1)

print(x.strftime("%B")) 