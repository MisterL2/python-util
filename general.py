def do(func, times, args=None):
    result = None
    for i in range(times):
        if islist(args):
            res = func(*args)
        else:
            if args is None:
                res = func()
            else:
                res = func(args)
                
        if isinstance(res,(list,tuple,str,int,float)):
            if result is None:
                result = res
            else:
                try:
                    result += res
                except TypeError:
                    pass
    return result
    
def doall(func,args=[]): #Somewhat similar to map()
    results = []
    for item in args:
        results.append(func(item))
    return results

def dorec(func,times,args=None): #Recursive
    result = args
    for i in range(times):
        result = func(result)
    return result

def islist(item):
    return isinstance(item,list)

def isint(item):
    return isinstance(item,int)

def isfloat(item):
    return isinstance(item,float)

def isstring(item):
    return isinstance(item,str)

def isdict(item):
    return isinstance(item,dict)

def istuple(item):
    return isinstance(item,tuple)

def setlength(item,length): #Sets a string to a certain length
    if length < len(item):
        return item[:length]
    
    if isstring(item):
        return item + " "*(length-len(item))
    elif islist(item):
        while len(item) < length:
            item.append(None)
        return item

def inany(iterable,item):
    if item == iterable:
        return True
    
    if isinstance(iterable,(list,dict,tuple)):
        if item in iterable:
            return True
        
    if isstring(iterable) and isstring(item):
        if item in iterable:
            return True
        
    if isdict(iterable):
        if item in iterable.values():
            return True
        iterable=iterable.values() #If it's a dictionary, only looks at the values for sublists/dicts/tuples/etc; if the searched value was in the keys, it would be found by the simple "if item in" previously
        
    for member in iterable:
        if isinstance(item,(str,list,dict,tuple)):
            if item == member: #e.g. inside a string that's inside a list
                return True
            
            if isstring(iterable) and isstring(item):
                if item in iterable:
                    return True
                
            if isinstance(member,(list,dict,tuple)):
                if item in member:
                    return True
            
        if isdict(member): #The item can only be in values, as keys are called in the previous "in"
            if item in member.values():
                return True
            else:
                for submember in member.values():
                    if isinstance(submember,(list,dict,tuple)):
                        result = inany(submember,item) #Calls itself to infinitely check sublists
                        if result: #Returns if True, otherwise keeps searching
                            return True
                        
        elif isinstance(member,(list,tuple)):
            result = inany(member,item) #Calls itself to infinitely check sublists
            if result: #Returns if True, otherwise keeps searching
                return True

    return False #If Nothing was found previously

 
#b = {"test" : 3, "other" : [1,2,[3,{"yo" : [3,"MisterL"]},4],5]}    
