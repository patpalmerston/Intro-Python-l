"""
The Python standard library's 'calendar' module allows you to
render a calendar to your terminal.
https://docs.python.org/3.6/library/calendar.html

Write a program that accepts user input of the form
  `14_cal.py month [year]`
and does the following:
 - If the user doesn't specify any input, your program should
   print the calendar for the current month. The 'datetime'
   module may be helpful for this.
 - If the user specifies one argument, assume they passed in a
   month and render the calendar for that month of the current year.
 - If the user specifies two arguments, assume they passed in
   both the month and the year. Render the calendar for that
   month and year.
 - Otherwise, print a usage statement to the terminal indicating
   the format that your program expects arguments to be given.
   Then exit the program.
"""

import sys
import calendar
from datetime import datetime

#y = int(input("Input the year : "))
#m = int(input("Input the month : "))
c = calendar.TextCalendar()
def pats_calendar(*args):
    if len(args) == 0:
        current = datetime.now()
        printDate = c.formatmonth(current.year, current.month)
        print(printDate)
    elif len(args) == 1:
        current = datetime.now()
        printDate = c.formatmonth(current.year, int(args[0]))
        print(printDate)
    elif len(args) == 2:
        printDate = c.formatmonth(int(args[0]), int(args[1]))
        print(printDate)
    else:
        print("please add the four digit year, and a number indicating the month, separated by a comma => cmd: python cal.py [month] [year]")

pats_calendar('1992', '3')