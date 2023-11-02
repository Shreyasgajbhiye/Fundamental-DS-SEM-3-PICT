cricket = ['adi','ram','shyam','lakhan','pratham']
batminton = ['adi','shyam','ram']
football = ['chetan','ram','chaitanya']
def C_B():
    res = []
    for students in cricket:
        if students in batminton:
            res.append(students)
    return res

def Either_C_B():
    res=[]
    for students in cricket:
        if students not in batminton:
            res.append(students)
    return res
    for students in batminton:
        if students not in cricket:
            res.append(students)
        return
    return res

def nither_C_B():
    res=[]
    for students in football:
        if students not in cricket and students not in batminton:
            res.append(students)
        return res

def both_C_F():
    res=[]
    for students in cricket:
        if students in football:
            res.append(students)
    return res

print(both_C_F())