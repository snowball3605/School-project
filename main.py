def Input_Name(name):
    side = len(name)
    name = list(name)
    for i in range(side):
        if name[i].isnumeric():
            return False
        elif name[i].isalpha():
            return False
    return True

print(Input_Name(""))