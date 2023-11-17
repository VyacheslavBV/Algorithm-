class Solution(object):
    def lengthOfLongestSubstring(self, s):
        string = list(s)
        answer = 0
        for j in range(len(string)):
            temp = set()
            count = 0
            for i in range(j, len(string)):
                if string[i] in temp:
                    answer = max(count, answer)
                    del temp
                    break
                else:
                    count += 1
                    temp.add(string[i])
            else:
                del temp
                answer = max(count, answer)

        return answer