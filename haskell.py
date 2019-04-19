def take(lst,amount):
    if amount > len(lst):
        return lst
    new = []
    for i in range(amount):
        new.append(lst[i])
    return new

def drop(lst,amount):
    if amount > len(lst):
        return lst
    new = []
    for i in range(amount):
        new.append(lst.pop())
    return new
        
def init(lst):
    return lst[:-1]

def last(lst):
    return lst[-1]

def head(lst):
    return lst[0]

def tail(lst):
    return lst[1:]

def product(lst):
    product = lst[0]
    if len(lst) == 1:
        return product
    else:
        for number in lst[1:]:
            product *= number
        return product            

def replicate(amount,thing):
    lst = []
    if isinstance(thing, list):
        while True:
            for item in thing:
                if len(lst) < amount:
                    lst.append(item)
                else:
                    return lst
    else:
        for i in range(amount):
            lst.append(thing)
        return lst

def replicate_string(amount,string):
    new = string
    while len(new)<amount:
        new+=string
    return new[:amount]
