class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        d_dict = {
            '2': ['abc'],
            '3': ['def'],
            '4': ['ghi'],
            '5': ['jkl'],
            '6': ['mno'],
            '7': ['pqrs'],
            '8': ['tuv'],
            '9': ['wxyz']
        }
        answer = []

        def dfs(L, str):
            if len(str) == len(digits):
                answer.append(''.join(str))
                return

            for i in range(L, len(digits)):
                for j in d_dict[digits[i]]:
                    dfs(i+1, str + j)

        dfs(0, '')

        return answer