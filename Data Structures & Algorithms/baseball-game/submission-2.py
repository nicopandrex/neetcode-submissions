class Solution:
    def calPoints(self, operations: List[str]) -> int:
        records = []

        for i in range(len(operations)):
            print(records)
            if operations[i] == '+':
                last = int(records[len(records) - 1])
                print(last)
                second_last = int(len(records) -2)
                records.append(int(records[len(records) - 1]) + int(records[len(records) -2]))
            elif operations[i] == "D":
                double = records[len(records)- 1] * 2
                records.append(int(records[len(records)- 1]) * 2)
            elif operations[i] == "C":
                records.pop()
                
            else:
                records.append(int(operations[i]))

        print(records)

        return sum(records)

        