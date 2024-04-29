import datetime
import threading

# Constants for days and months names
DAYS = ('Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday')
MONTHS = ('January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December')

# Function to get the year input from the user
def getYearFromUser():
    while True:
        print('Enter the year for the calendar:')
        response = input('> ')

        if response.isdecimal() and int(response) > 0:
            return int(response)

        print('Please enter a numeric year, like 2023.')

# Function to get the month input from the user
def getMonthFromUser():
    while True:
        print('Enter the month for the calendar, 1-12:')
        response = input('> ')

        if response.isdecimal():
            month = int(response)
            if 1 <= month <= 12:
                return month

        print('Please enter a number from 1 to 12.')

# Function to generate the calendar text for the specified year and month
def getCalendarFor(year, month):
    calText = ''

    # Add month and year information
    calText += (' ' * 34) + MONTHS[month - 1] + ' ' + str(year) + '\n'
    calText += '...Sunday.....Monday....Tuesday...Wednesday...Thursday....Friday....Saturday..\n'

    # Separator for weeks
    weekSeparator = ('+----------' * 7) + '+\n'
    # Blank row between weeks
    blankRow = ('|          ' * 7) + '|\n'

    # Get the first day of the month
    currentDate = datetime.date(year, month, 1)
    # Roll back to the previous Sunday
    while currentDate.weekday() != 6:
        currentDate -= datetime.timedelta(days=1)

    # Loop over each week in the month
    while True:
        calText += weekSeparator

        # Generate the row for day numbers
        dayNumberRow = ''
        for i in range(7):
            dayNumberLabel = str(currentDate.day).rjust(2)
            dayNumberRow += '|' + dayNumberLabel + (' ' * 8)
            currentDate += datetime.timedelta(days=1)
        dayNumberRow += '|\n'

        # Add the day number row and 3 blank rows to the calendar text
        calText += dayNumberRow
        for i in range(3):
            calText += blankRow

        # Check if we're done with the month
        if currentDate.month != month:
            break

    # Add the horizontal line at the very bottom of the calendar
    calText += weekSeparator
    return calText

# Function to display the calendar and save it to a text file
def displayCalendar(year, month):
    calText = getCalendarFor(year, month)
    print(calText)

    calendarFilename = 'calendar_{}_{}.txt'.format(year, month)
    with open(calendarFilename, 'w') as fileObj:
        fileObj.write(calText)

    print('Saved to ' + calendarFilename)

# Main function
def main():
    print('Calendar Maker')

    # Get year and month input from the user
    year = getYearFromUser()
    month = getMonthFromUser()

    # Create a separate thread to display the calendar
    threading.Thread(target=displayCalendar, args=(year, month)).start()

if __name__ == '__main__':
    main()
