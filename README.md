# python-util

Documentation is WIP


## General

### Functional Programming

#### do(func, times, showResult=True)

Executes the specified parameter function `func` `times` amount of times. If showResult=True, it returns a list of the results.
Example usage:

```python
do(lambda : print("hello"), 5)
```
will print "hello" 5 times

#### doall(func, args=[], showResult=True)

Executes the given function for a list of arguments
Example usage:

```python
do(addFive, [1,2,3],True)
```
will return [6,7,8]

#### dorec(func, times, args=None, showResult=True)

Recursively executes the given function, taking the previous output of the parameter function `func` as parameter.

If the args param is not a list, tuple or dictionary, but the return value is, it will loop through all the returned values and apply the parameter function on them recursively until the remaining specified recursion depth is reached.
This is determined by the `times` parameter and the current level of recursion.
For example, if times=10 and the third iteration produces a list, the parameter function will be applied on the contents of that list 7 more times.

### Type Check Shorthands

#### isiter(item) / isiterable(item)
Checks if the item is an iterable


#### islist(item)
```python
isinstance(item,list)
```

#### isint(item)
```python
isinstance(item,int)
```

#### isfloat(item)
```python
isinstance(item,float)
```

#### isstring(item)
```python
isinstance(item,str)
```

#### isdict(item)
```python
isinstance(item,dict)
```

#### istuple(item)
```python
isinstance(item,tuple)
```

#### getType(item)
Returns the type of that item as a string.

### Iterables

#### inany(iterable, item, searchInSubstring=False)
Recursively iterates through the target iterable and all nested iterables, meaning it will also check:

- All sublists, sublists of sublists, etc. for ALL iterables (lists, tuples, user-defined iterables)

- For dictionaries, it checks both the keys and the values, including any nested iterables within the values

- If searchInSubstring=True, it will also check if the `item` is a substring of any element.


Example usage:
```python
b = {"test" : 3, "other" : [1,2,[3,{"yo" : [3,"MisterL"]},4],5]}
inany(b,"ister") #False
inany(b,"ister",True) #True, as "ister" is a substring of "MisterL"
```

#### allIn(lst, otherlst)
Checks if **all** of the elements from `lst` are in `otherlst`

#### anyIn(lst, otherlst)
Checks if **any** of the elements from `lst` are in `otherlst`

#### toDict(lst, otherlst)
Combines two lists into a dictionary, with `lst` as keys and `otherlst` as values.
If the two lists are of different size, the excess values in the longer list are discarded.

### Parsing

#### numparse(string, decimals=False, decimalPoint='.')
Parses all numbers out of a given string and returns them in a list.
If decimals=True, it will also parse out decimals numbers using the `decimalPoint`. `decimalPoint` can also be set to different values, e.g. ',' when parsing German numbers.

Example usage
```python
numparse("oeiajoefijaoi23jjaeofijaeof83fjoaefij9aeoiafj") #Returns [23, 83, 9]
numparse("abaefjoi23.6ojaeoifjaojo36.5152aeof124ijeoafji3oij",True) #Returns [23.6, 36.5152, 124.0, 3.0]
numparse("aojefioeojf23,33joijwoeifjaoiefjaoij99,99eaf,,,.f13",True,",") #Returns [23.33, 99.99, 13.0]
```

#### timeparse(timestring)
Expects a string in format HH:MM or HH:MM:SS
Returns a datetime object (with or without seconds) from the parameter string


#### dateparse(datestring, seperator='-', reverse=False, american=False)
Expects a datestring in a standard format (e.g. YYYY-MM-DD, YY-M-DD, etc.)
The seperator can be changed to parse different notations, e.g. 2019/08/12
If reverse=True, parses a date of format DD-MM-YYYY or similar
If american=True, expects YYYY-DD-MM (or MM-DD-YYYY if reverse=True) or similar format
