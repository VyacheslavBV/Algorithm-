class Solution:
    def longestPalindrome(self, s: str) -> str:
        startmax = 0
        string = list(s)
        ret = ""
        maxsd = 0
        answer = ""

        for i in range(len(string)):
            l, r = i, i
            while l >= 0 and r < len(string) and string[r] == string[l]:
                answer = string[l:r+1]
                l -= 1
                r += 1
            else:
                if startmax < len(answer):
                    ret = answer
                    startmax = len(answer)
                answer = ""

            l, r = i, i+1
            while l >= 0 and r < len(string) and string[r] == string[l]:
                answer = string[l:r + 1]
                l -= 1
                r += 1
            else:
                if startmax < len(answer):
                    ret = answer
                    startmax = len(answer)
                answer = ""


            ln = ""
            for i in range(len(ret)):
                ln += ret[i]

        return ln
t = Solution
print(Solution.longestPalindrome(t,"babad"))