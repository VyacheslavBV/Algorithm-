

def poll(x) -> bool:
    string = str(x)
    if len(string) == 1:
        return True
    else:
        ln = len(string) // 2
        string = list(string)
        left = string[:ln]
        right = string[-ln:]
        right.reverse()
        if right == left:
            return True
        else:
            return False

print(poll(1221))
