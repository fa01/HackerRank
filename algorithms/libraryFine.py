
# Your local library needs your help! Given the expected and actual return dates for a library book, create a program that calculates the fine(if any). The fee structure is as follows:

# If the book is returned on or before the expected return date, no fine will be charged(i.e.: fine = 0)
# If the book is returned after the expected return day but still within the same calendar month and year as the expected return date, (15 * (returned - due date))
# If the book is returned after the expected return month but still within the same calendar year as the expected return date, the . (500 * (returned - due date))
# If the book is returned after the calendar year in which it was expected, there is a fixed fine of fine = 10000
# Charges are based only on the least precise measure of lateness. For example, whether a book is due January 1, 2017 or December 31, 2017, if it is returned January 1, 2018, that is a year late and the fine would be .

# Function Description
# libraryFine has the following parameter(s):

# d1, m1, y1: returned date day, month and year
# d2, m2, y2: due date day, month and year

# Output Format
# Print a single integer denoting the library fine for the book received as input.

def libraryFine(d1, m1, y1, d2, m2, y2):
    if(y1 < y2):
        return 0
    elif(y1 < y2 and m1 < m2):
        return 0
    elif(y1 <= y2 and m1 <= m2 and d1 <= d2):
        return 0
    elif(y1 > y2):
        return 10000
    elif(m1 > m2):
        print('month')
        return 500 * (m1 - m2)
    elif(m1 == m2 and d1 > d2):
        print('day')
        return 15 * (d1 - d2)
    else:
        return 0
