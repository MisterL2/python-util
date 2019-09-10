def do(func, times,showResult=True):
    result = []
    for _ in range(times):
        result.append(func())
    if showResult:
        return result


def doall(func,args,showResult=True): #Somewhat similar to map()
    if showResult:
        results = []
        for item in args:
            results.append(func(item))
        return results
    else:
        for item in args:
            func(item)


def dorec(func,times,args=None,showResult=True): #Recursive
    if times == 0:
        return None
    result = args
    results = []
    for i in range(times):
        if not (i!=0 and (isiterable(result) and not (isiterable(args) and len(args)==len(result) and getType(result)==getType(args)))):
            result = func(result)
        if isiterable(result) and not (isiterable(args) and len(args)==len(result) and getType(result)==getType(args)): #If the function returns more values than it accepts as parameter, it loops through them in the recursive procedure
            for item in result:
                if getType(item)==getType(args) and (not isiterable(args) or (isiterable(args) and len(item)==len(args))):
                    res = dorec(func,(times-i-1),item) #Does recursion, but only to the specified remaining depth (times-i)
                    if res is not None and not (isiterable(res) and len(res)==0): #No empty list or None
                        results.append(res)
    if showResult:
        if len(results)==0:
            return result
        return results

def isiter(item): #Alias
    return isiterable(item)

def isiterable(item):
    try:
        iter(item)
        return True
    except TypeError:
        return False

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

def getType(item): #Returns the name in readable form such as 'int', rather than <class 'int'> from type()
    return item.__class__.__name__

def inany(iterable,item,searchInSubstring=False):
    if item == iterable:
        return True
    
    if isiterable(iterable):
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
            
            if isstring(member) and searchInSubstring==False:
                continue
            
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
                        result = inany(submember,item,searchInSubstring) #Calls itself to infinitely check sublists
                        if result: #Returns if True, otherwise keeps searching
                            return True
                        
        elif isinstance(member,(list,tuple)):
            result = inany(member,item,searchInSubstring) #Calls itself to infinitely check sublists
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

#Similar to zip, but returns a dictionary rather than a list of tuples
def toDict(lst,otherlst): #Returns a dictionary with the first lst as keyset and the otherlst as valueset
    size = min(len(lst),len(otherlst))
    return {lst[i]:otherlst[i] for i in range(size)}
    
def numparse(string,decimals=False,decimalPoint='.',negatives=True) -> list: #Returns a list of all numbers found in a string
    result = []
    currentNum = ""
    for item in string:
        if item in ["1","2","3","4","5","6","7","8","9","0"]:
            currentNum+=item
        elif decimals and item == decimalPoint and currentNum != "":
            currentNum+='.' #Otherwise conversion doesnt work
        elif item == '-' and negatives:
            if currentNum != "":
                #Add previous number first, e.g. in case eiojasoefij23-25 would save 23, -25
                if decimals:
                    result.append(float(currentNum))
                else:
                    result.append(int(currentNum))
                currentNum = ""
            currentNum += item
        else:
            if currentNum not in ["","-"]:
                if decimals:
                    result.append(float(currentNum))
                else:
                    result.append(int(currentNum))
                currentNum = ""
                
    if len(currentNum)>0:
        if decimals:
            result.append(float(currentNum))
        else:
            result.append(int(currentNum))
    return result

def timeparse(timestring):
    import datetime
    parsedTime = timestring.split(":")
    if len(parsedTime) == 3:
        return datetime.time(int(parsedTime[0]),int(parsedTime[1]),int(parsedTime[2]))
    return datetime.time(int(parsedTime[0]),int(parsedTime[1]))
    

def dateparse(datestring,seperator='.',reverse=False,american=False):
    import datetime
    parsedDate = datestring.split(seperator)
    if reverse:
        parsedDate = list(reversed(parsedDate))
    if american:
        return datetime.date(int(parsedDate[0]),int(parsedDate[2]),int(parsedDate[1]))
    else:
        return datetime.date(int(parsedDate[0]),int(parsedDate[1]),int(parsedDate[2]))

def intput(msg,error=None) -> int:
    response = None
    while response is None:
        try:
            response = int(input(msg))
        except Exception: #Catches both ValueError and UnicodeExceptions
            if error is not None:
                print(error)
    return response
        
