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

        d_l.sort(key=lambda x: (x.split()[1:], x.split()[0]))
        return d_l + l_l