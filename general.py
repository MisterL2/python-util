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
    if times == 0:
        return None
    
    result = args
    results = []
    for i in range(times):
        if i!=0 and (isiterable(result) and not (isiterable(args) and len(args)==len(result) and getType(result)==getType(args))):
            pass
        else:
            result = func(result)
        if isiterable(result) and not (isiterable(args) and len(args)==len(result) and getType(result)==getType(args)): #If the function returns more values than it accepts as parameter, it loops through them in the recursive procedure
            for item in result:
                if getType(item)==getType(args) and (not isiterable(args) or (isiterable(args) and len(item)==len(args))):
                    res = dorec(func,(times-i-1),item) #Does recursion, but only to the specified remaining depth (times-i)
                    if res is not None and not (isiterable(res) and len(res)==0): #No empty list or None
                        results.append(res) 
    if len(results)==0:
        return result
    else:
        return results

def isiterable(item):
    return isinstance(item,(list,tuple,dict))

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

def getType(item):
    return item.__class__.__name__

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
    
    if isiterable(iterable):
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
        if isiterable(member) or isstring(member):
            if item == member: #e.g. inside a string that's inside a list
                return True
            
            if isstring(iterable) and isstring(item):
                if item in iterable:
                    return True
                
            if isiterable(member):
                if item in member:
                    return True
            
        if isdict(member): #The item can only be in values, as keys are called in the previous "in"
            if item in member.values():
                return True
            else:
                for submember in member.values():
                    if isiterable(submember):
                        result = inany(submember,item) #Calls itself to infinitely check sublists
                        if result: #Returns if True, otherwise keeps searching
                            return True
                        
        elif isinstance(member,(list,tuple)):
            result = inany(member,item) #Calls itself to infinitely check sublists
            if result: #Returns if True, otherwise keeps searching
                return True

    return False #If Nothing was found previously

 
#b = {"test" : 3, "other" : [1,2,[3,{"yo" : [3,"MisterL"]},4],5]}    


def allIn(lst,otherlst): #all items of the first list in the second list
    for item in lst:
        if item not in otherlst:
            return False
    return True

def anyIn(lst,otherlst): #any item from the first list in the second list
    for item in lst:
        if item in otherlst:
            return True
    return False

def toDict(lst,otherlst): #Returns a dictionary with the first lst as keyset and the otherlst as valueset
    if len(lst)<len(otherlst): #If the second list is longer, excess values are discarded silently
        print("First list is shorter than the second list!")
        raise Exception
    d = {}
    for i in range(len(lst)):
        d[lst[i]]=otherlst[i]
    return d
    
def numparse(string,decimals=False,decimalPoint='.'): #Returns a list of all numbers found in a string
    result = []
    currentNum = ""
    for item in string:
        if item in ["1","2","3","4","5","6","7","8","9","0"]:
            currentNum+=item
        elif decimals and item == decimalPoint:
            currentNum+=item
        else:
            if currentNum!="":
                result.append(float(currentNum))
                currentNum = ""
                
    if len(currentNum>0):
        result.append(float(currentNum))
    if len(result>1):
        return result
    else:
        return result[0]

def timeparse(time):
    import datetime
    parsedTime = time.split(":")
    if len(parsedTime) == 3:
        return time(int(parsedTime[0]),int(parsedTime[1]),int(parsedTime[2]))
    return time(int(parsedTime[0]),int(parsedTime[1]))
    

def dateparse(date,seperator='-',reverse=False):
    import datetime
    parsedDate = date.split(seperator)
    if reverse:
        parsedDate = list(reversed(parsedDate))
    return datetime.date(int(parsedDate[0]),int(parsedDate[1]),int(parsedDate[2]))
