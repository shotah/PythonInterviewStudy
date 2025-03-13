# array of logs
# space delimited string
# words seperated by space
# first letter is a unqiue identifier
# 2 types of logs
#  - letters/words lowercase following words,
#  - digit logs identifier all numbers.
# rules:
# letter logs should always be before letter logs
# letter logs lexical graphically - alphabetical order
# digit logs should retain order.
# orginal is a mix..

# Log input example
# ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]

# Question Summary

# There are two types of logs:
# Letter-logs: All words (except the identifier) consist of lowercase English letters.
# Digit-logs: All words (except the identifier) consist of digits.
# Reorder these logs so that:
# The letter-logs come before all digit-logs.
# The letter-logs are sorted lexicographically by their contents. If their contents are the same, then sort them lexicographically by their identifiers.
# The digit-logs maintain their relative ordering.
# Return the final order of the logs.

input = [
    "dig1 8 1 5 1",
    "let1 art can",
    "dig2 3 6",
    "let2 own kit dig",
    "let3 art zero",
]


class DigiLogs:
    def __init__(self) -> None:
        self.logs = {}

    def is_digilog(self, log) -> bool:
        try:
            return str(int(log.split()[1])) == log.split()[1]
        except Exception as _:
            return False

    def process(self, log: str) -> None:
        if not log:
            return
        entries = log.split()
        print(entries)
        id = entries.pop(0)
        self.logs[id] = [int(n) for n in entries]


class LetLogs:
    def __init__(self) -> None:
        self.logs = {}

    def is_letlog(self, log) -> bool:
        try:
            return str(int(log.split()[1])) != log.split()[1]
        except Exception as _:
            return True

    def process(self, log: str) -> None:
        if not log:
            return
        entries = log.split()
        print(entries)
        id = entries.pop(0)
        entries.sort()
        self.logs[id] = entries


class Solution:
    def __init__(self) -> None:
        self.digilogs = DigiLogs()
        self.letlogs = LetLogs()

    def process_logs(self, input) -> list:
        results = []
        for log in input:
            if self.digilogs.is_digilog(log):
                self.digilogs.process(log)
            if self.letlogs.is_letlog(log):
                self.letlogs.process(log)
        for key, value in self.letlogs.logs.items():
            print(key, value)
            results.append([key] + value)
        for key, value in self.digilogs.logs.items():
            print(key, value)
            results.append([key] + value)
        return results


if __name__ == "__main__":
    s = Solution()
    print(s.process_logs(input))
