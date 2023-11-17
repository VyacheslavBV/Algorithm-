class Solution:
    @staticmethod
    def addTwoNumbers(l1, l2):
        l1 = l1.reverse()
        l2 = l2.reverse()

        L1 = ""
        for i in range(len(l1)):
            L1 += str(l1[i])
        L1 = int(L1)

        L2 = ""
        for i in range(len(l2)):
            L2 += str(l2[i])
        L2 = int(L2)

        summ = L1 + L2
        answer = list(str(summ))
        answer = answer.reverse()

        return answer


if __name__ == '__main__':
    print(Solution.addTwoNumbers([2,4,3], [5,6,4]))
