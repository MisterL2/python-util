def take(lst,amount):
    if amount > len(lst):
        return lst
    new = []
    for i in range(amount):
        new.append(lst[i])
    if isinstance(lst,str):
        return "".join(new)
    return new

def drop(lst,amount):
    if amount > len(lst):
        return lst
    new = []
    for i in range(len(lst)-amount,len(lst)):
        new.append(lst[i])
    if isinstance(lst,str):
        return "".join(new)
    return new
     
def head(lst):
    return lst[0]

def last(lst):
    return lst[-1]

def init(lst):
    return lst[:-1]

def tail(lst):
    return lst[1:]

def product(lst):
    product = lst[0]
    for number in lst[1:]:
        product *= number
    return product            

def cycle(thing,amount):
    lst = []
    while True:
        for item in thing:
            if len(lst) < amount:
                lst.append(item)
            else:
                if isinstance(thing, str):
                    return "".join(lst)
                return lst

def replicate(thing,amount):
    lst = []
    for i in range(amount):
        lst.append(thing)
    return lst
