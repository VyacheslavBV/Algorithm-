

def rreverse(x):
    if x == 0:
        return 0
    else:
        string = list(str(x))
        flagznak = False
        znak = ""
        numb = "0123456789"
        aw = []
        answer = ""

        for i in range(len(string)):
            if flagznak == False and (string[i] == "+" or string[i] == "-"):
                flagznak = True
                if string[i] == "-":
                    znak = "-"
            elif string[i] in numb:
                aw.append(string[i])

        aw.reverse()
        for i in range(len (aw)):
            if aw[i] == "0" and answer == "":
                pass
            elif aw[i] in numb:
                answer += aw[i]

        final = int(znak + answer)
        if final > 2**31 - 1 or final < -2**31:
            return 0
        else:
            return final

print(rreverse(0))

