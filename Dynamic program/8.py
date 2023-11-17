def search(s):
    if s == [""]:
        return ""
    elif len(s) == 1:
        return s[0]
    else:
        minlen = 100000
        indminlen = 0
        for p in range(len(s)):
            if s[p] == "":
                return ""
            if minlen >= len(s[p]):
                minlen = len(s[p])
                indminlen = p
        mass = []
        answer = ""
        for i in range(len(s[indminlen])):
            string = list(s[indminlen])
            mass.append(string[i])
            for j in range(len(s)):
                ln = list(s[j])
                if mass[i] == ln[i]:
                    pass
                else:
                    flag = False
                    if len(mass) == 1:
                        l = ""
                        return l
                    else:
                        for k in range(len(mass) - 1):
                            answer += mass[k]
                        return answer
        for k in range(len(mass)):
            answer += mass[k]
        return answer

d = [str(x) for x in input().split()]
print(search(d))