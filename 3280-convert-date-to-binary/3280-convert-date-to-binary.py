class Solution:
    def convertDateToBinary(self, date: str) -> str:

        def binary(num : str) -> str:
            intNum = int(num)
            binaryNum = ""

            while(intNum > 0) :
                binaryNum = str(intNum % 2) + binaryNum
                intNum //= 2
            
            return binaryNum

        year , month , date = date.split("-")

        return f"{binary(year)}-{binary(month)}-{binary(date)}"
        