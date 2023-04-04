"""Given a date string in the form Day Month Year, where:

Day is in the set {"1st", "2nd", "3rd", "4th", ..., "30th", "31st"}.
Month is in the set {"Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"}.
Year is in the range [1900, 2100].
Convert the date string to the format YYYY-MM-DD, where:

YYYY denotes the 4 digit year.
MM denotes the 2 digit month.
DD denotes the 2 digit day.
"""
class Solution:
    def reformatDate(self, date: str) -> str:

        Day = ["1st", "2nd", "3rd", "4th", "5th", "6th", "7th", "8th", "9th", "10th", "11th", "12th", "13th", "14th", "15th",
               "16th", "17th", "18th", "19th", "20th", "21st", "22nd", "23rd", "24th", "25th", "26th", "27th", "28th", "29th", "30th", "31st"]
        Month = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
        Year = range(1900, 2100)

        a = date.split(' ')
        date_day = str(a[0])
        date_month = str(a[1])
        date_year = int(a[2])

        D_D = str((Day.index(date_day)) + 1)
        M_M = str((Month.index(date_month)) + 1) 

        if len(D_D) == 1:
            D_D = "0" + str(D_D)
        if len(M_M) == 1:
            M_M = "0" + str(M_M)
        DD = str(D_D) 
        MM = str(M_M) + "-"
        YYYY = str(date_year) + "-"

        return YYYY + MM + DD
