def is_isogram(string):
    name = string.casefold()
    control = 0 
    
    print(name)
    for i in name:
        control += 1
        for j in name[control:]:
            if i == j:
                return False
    else:
        return True