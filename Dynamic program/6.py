# Leetcode ложиться, когда запускаю прогу
# прошел ~1080/1088 тестов
#
# есть проблемы с нулем в связке с знаком
#


def myAtoi(s):
    znak = None
    numb = "0123456789"
    string = ""
    lst = list(s)
    flag = False
    zeroflag = False
    breakflag = False
    numbflag = False
    flagbbreak = False
    "   +0 123"
    for i in range(len(lst)):
        print(i , flag, breakflag, zeroflag, numbflag, flagbbreak)
        if lst[i] == " " and numbflag == False and zeroflag == False:
            pass
        elif lst[i] == " " and (numbflag == True or zeroflag == True):
            flagbbreak = True
            answer = string
        elif (lst[i] == "+" or lst[i] == "-") and znak == None:
            if zeroflag == True:
                breakflag = True
                break
            znak = True if lst[i] == "+" else False
        elif lst[i] == "0" and string == "":
            zeroflag = True
        elif lst[i] in numb:
            if flag == False and znak == False:
                flag = True
                string += "-"
            string += lst[i]
            numbflag = True
        else:
            break

    if string == "":
        return 0
    else:
        if flagbbreak == True:
            if answer == "":
                return 0
            else:
                return int(answer)
        elif int(string) > 2**31 - 1:
            return 2**31 - 1
        elif int(string) < - 2 ** 31:
            return -2**31
        elif zeroflag == True and breakflag == True:
            return 0
        else:
            return int(string)

print(myAtoi("   +0 123"))