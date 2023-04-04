"""Given a date, return the corresponding day of the week for that date.

The input is given as three integers representing the day, month and year respectively.

Return the answer as one of the following values {"Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"}."""
class Solution:
    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        week = {0:'Friday', 1:'Saturday', 2:'Sunday', 3:'Monday', 4:'Tuesday',  5:'Wednesday', 6:'Thursday'}
        dic = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30}
        
        leap_num = 1 + (year-1973)//4 if year > 1971 else 0
        yearTot = (year-1971)*365 + leap_num
        monthTot = sum([dic[i] for i in dic if i < month])
     
        if (year % 4 == 0 and year % 100 or year % 400 == 0) and month > 2:
            x = yearTot + monthTot + day + 1
        else:
            x = yearTot + monthTot + day

        return week[(x-1) % 7]
