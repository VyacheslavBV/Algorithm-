s = str(input())
string = list(s)

def check(s):
    string = list(s)
    ln = len(string) // 2
    left = string[:ln]
    right = string[-ln:]
    right.reverse()
    ln = len(s)
    if left == right:
        return True
    else:
        return False

startmax = 1
answer = string[0]

for i in range(len(string)):
    temp = ""
    for j in range(i, len(string)):
        temp += str(string[j])
        ln = len(temp)
        flag = check(temp)
        if flag == True and ln > startmax:
            answer = temp
            startmax = ln
            flag = False
print(answer)


