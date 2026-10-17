class Solution:
    def calPoints(self, operations: list[str]) -> int:
        record = []

        for i in range(len(operations)):
            if operations[i] == '+'   :
                record.append(record[~0] + record[~1])
            elif operations[i] == 'D' :
                record.append(record[~0] * 2)
            elif operations[i] == 'C' :
                record.pop()
            else:
                record.append(int(operations[i]))
        
        return sum(record)