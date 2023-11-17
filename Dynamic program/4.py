


def enigma(s : str, numb : int):
    if numb == 1:
        return s
    else:
        string = list(s)
        answer = ''
        if numb % 2 == 1:
            shift = numb // 2
            for i in range(shift):
                for j in range(len(string)):
                    k = i + (numb+1) * j
                    if k >= len(string):
                        break
                    answer += string[k]


            for i in range(0,len(string)):
                k = shift  + i * (shift + 1)
                if k >= len(string):
                    break
                answer += string[k]

            for i in range(shift + 1, numb ):
                for j in range(len(string)):
                    k = i + j * (numb + 1)
                    if k >= len(string):
                        break
                    answer += string[k]

            return answer
        else:
            shift = int(numb / 2 - 1)
            answer = ''
            for i in range(shift):
                for j in range(len(string)):
                    k = i + (2 + numb) * j
                    if k >= len(string):
                        break
                    answer += string[k]

            flag = False
            flag1 = False
            flag2 =False

            k1 = 0
            k2 = 0

            for i in range(len(string)):
                if flag == False:
                    flag = True
                    k = shift + k1 * (numb + 2)
                    k1 += 1
                    if k >= len(string):
                        flag1 = True
                    if flag1 == False:
                        print(k)
                        answer += string[k]
                    else:
                        break

                elif flag == True:
                    flag = False
                    k = numb +1 + k2 * (numb + 2)
                    k2 += 1
                    if k >= len(string):
                        flag2 = True
                    if flag2 == False:
                        print(k)
                        answer += string[k]
                    else:
                        break

            k1 = 0
            k2 = 0

            flag = False
            flag1 = False
            flag2 = False

            for i in range(len(string)):
                if flag == False:
                    flag = True
                    k = (numb - (shift + 1)) + k1 * (numb + 2)
                    k1 += 1
                    if k >= len(string):
                        flag1 = True
                    if flag1 == False:
                        print(k)
                        answer += string[k]
                    else:
                        break

                elif flag == True:
                    flag = False
                    k = numb + k2 * (numb + 2)
                    k2 += 1
                    if k >= len(string):
                        flag2 = True
                    if flag2 == False:
                        print(k)
                        answer += string[k]
                    else:
                        break

            for i in range(shift + 2, numb):
                for j in range(len(string)):
                    k = i + j * (numb + 2)
                    if k > len(string):
                        break
                    answer += string[k]


            return answer

print(enigma("ABC", 3))

