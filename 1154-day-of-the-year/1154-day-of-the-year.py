class Solution:
    def dayOfYear(self, date: str) -> int:
        def isleapyear(year):
            return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)



        year , month , day = map( int , date.split("-"))

        days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        return day + (sum(days[ : month - 1])  + ( 1 if month > 2 and isleapyear(year) else 0) )