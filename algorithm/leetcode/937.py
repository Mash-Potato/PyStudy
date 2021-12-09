from typing import List


class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        l_l = []
        d_l = []
        for log in logs:
            if log.split()[1].isdigit():
                d_l.append(log)
            else:
                l_l.append(log)

        l_l.sort(key= lambda x: (x.split()[1:], x.split()[0]))
        return l_l + d_l


print(Solution.reorderLogFiles(' ', ["dig1 8 1 5 1", "let1 art can", "dig2 8 1 5 1", "let2 own kit dig", "let3 art zero"]))