# python-util

## General


### Functional Programming




#### do(func, times, showResult=True)

Executes the specified parameter function `func` `times` amount of times. If showResult=True, it returns a list of the results.

Example usage:

```python
do(lambda : print("hello"), 5) #Will print "hello" 5 times
```

#### doall(func, args=[], showResult=True)

Executes the given function for a list of arguments.

Example usage:

```python
do(addFive, [1,2,3],True) #Returns [6,7,8]
```


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





#### numparse(string, decimals=False, decimalPoint='.', negatives=True)
Parses all numbers out of a given string and returns them in a list.
If negatives=False, all `-` signs will be ignored and only positive numbers returned.
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


## Files
Shorthands for simple file operations.
### Shorthands

#### fileappend(filename, thing)
Will open the file and append the `thing` to the end of the file. Will convert to string if necessary and close file after use.

#### fileoverwrite(filename, thing)
Will open the file and overwrite the file contents with the `thing`. Will convert to string if necessary and close file after use.

#### filereplace(filename, regexToReplace, replacementString)
Will open the file and replace anything that matches the regex `regexToReplace` with the `replacementString`. Closes file after use.

## Haskell
Implements common Haskell convenience features

### List features
All except `product` work on strings as well.

#### take(lst, amount)
Returns the first `amount` indexes of the `lst`

#### drop(lst,amount)
Returns the last `amount` indexes of the `lst`

#### last(lst)
Returns the last index of `lst`

#### head(lst)
Returns the first index of `lst`

#### init(lst)
Returns all indexes of `lst` except for the last.

#### tail(lst)
Returns all indexes of `lst` except for the first.

#### product(lst)
Returns the product of all members of the list multiplied together. Somewhat similar to built-in function `sum()`

#### cycle(thing, amount)
Cycles a list or string and returns the first `amount` characters from it.
```python
cycle("TEST",3)
```
is effectively equal to
```haskell
take 3 (cycle "TEST")
```

Example usage:
```python
cycle("TEST ",17) #Returns 'TEST TEST TEST TE'
cycle([1,2,3,4],10) #Returns [1, 2, 3, 4, 1, 2, 3, 4, 1, 2]
```

#### replicate(thing, amount)
Replicates the given thing and returns a list containing the object `amount` times.

Example usage:
```python
replicate(15,3) #Returns [15, 15, 15]
replicate(True,3) #Returns [True, True, True]
replicate("Hello",5) #Returns ['Hello', 'Hello', 'Hello', 'Hello', 'Hello']
replicate([1,2,3,4],3) #Returns [[1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4]]
```


## Math
An extension to the built-in math module

### Numbers

#### isPrime(num)
Checks if the given number is a prime.

#### findPrimes(minimum,maximum)
Returns all in `range(minimum,maximum)`

#### findFactors(num)
Returns a list of all factors of the given number, including 1 and the number itself.
Example usage:
```python
findFactors(120) #Returns [1, 120, 2, 60, 3, 40, 4, 30, 5, 24, 6, 20, 8, 15, 10, 12]
findFactors(67) #Returns [1, 67]
```

#### findFactorTuples(num)
Returns all factors of the given number in a list of tuples, including 1 and the number itself.
Example usage:
```python
findFactors(120) #Returns [(1, 120), (2, 60), (3, 40), (4, 30), (5, 24), (6, 20), (8, 15), (10, 12)]
findFactors(67) #Returns [(1, 67)]
```

#### findIntegerRoot(num,power=2)
Finds the integer x, such that x \*\* `power` is equal to `num`. Returns None if there is no integer root.
Example usage:
```python
findIntegerRoot(100) #Returns 10
findIntegerRoot(27,3) #Returns 3
findIntegerRoot(16807,5) #Returns 7
findIntegerRoot(13) #Returns None
```

### 2D Linear equations

#### findIntersect(eq1,eq2)
Expects two equations in the tuple form (m,c) aka (gradient,start) for a linear equation of type `y = mx + c`.
Returns a tuple with values (x,y) representing the Cartesian coordinates at which these two equations are equal.

#### findGradient(coord1,coord2)
Expects two position vectors in tuple form (x,y).
Returns the gradient of the line connecting them

### 2D Geometry

#### circlePerimeter(radius)
Returns the perimeter of a circle with given `radius`.

#### triangleArea(a,b,c=None)
**Either** expects three parameters representing the three sides of the triangle,
**or** expects two parameters representing the base length and height of the triangle.
Returns the area of the triangle.

#### circleArea(radius)
Returns the area of a circle with given `radius`.

#### trapezoidArea(a,b,d)
Expects the lengths of the parallel sides `a` and `b`, as well as the distance between them `d`.
Returns the area of the trapezoid.

### 3D Geometry

#### sphereVolume(radius)
Returns the volume of a sphere with the given `radius`.

#### prismVolume(a,b,c=None)
**Either** expects three parameters representing length, width and height of the prism,
**or** expects two parameters representing the area of the base and the height of the prism
Returns the volume of the prism.

#### cylinderVolume(radius, height)
Returns the volume of a cylinder with given `radius` and `height`.

#### pyramidVolume(area, height)
Returns the volume of a pyramid with given `area` and `height`.

#### coneVolume(area, height)
Returns the volume of a cone with given `area` and `height`.

## Data structures
Additional complex data structures for Python.

### TreeNode

### Methods

#### Node.addValue(self,valueiterable)
Adds all values of the valueiterable to the tree, **starting from that Node**

#### Node.findValue(self,value,returnNode=False)
Returns True if the `value` can be found **downwards of that Node**, False if it cannot.
If returnNode=True, it instead returns the Node with that value, or None.

#### Node.findNode(self,value)
Shorthand for Node.findValue(self,value,returnNode=True)

#### Node.getSubNodeKeys(self)
Returns a list of all the values of the subNodes

### Fields

#### Node.subNodes
Returns a dictionary of {value:SubNode}


### Explanation

For example, the string "TEST" has 4 elements and would be converted into a tree with 4 Nodes:

    "T" -> "E" -> "S" -> "T"
    
    Node(value="T") ---> Node(value="E") ---> Node(value="S") ---> Node(value="T")

If we now add the string "TEA" to the same tree, we get:

    "T" -> "E" -> "S" -> "T"
               -> "A"

The second Node (with value "E") now has two SubNodes, one with value "S" and one with value "A"
The values "T" and "E" are not added a second time, as they are already in the tree.

### Full example

```python
#Create TreeNode object
master = TreeNode()

#Add values to the tree
master.addValue("hello")
master.addValue("hey")
master.addValue("hi")
master.addValue("howdy")
```

Now our tree looks like this:

    "h" -> "e" -> "l" -> "l" -> "o"
               -> "y"
        -> "i"
        -> "o" -> "w" -> "d" -> "y"
 

```python
#Check if "hey" is really in the tree
master.findValue("hey") #Returns True

#Get the Node that contains the 'd' in "howdy"
node = master.findNode("howd")

#Get the Node that contains the 'e' in "hey" (and also the 'e' in "hello")
otherNode = master.findNode("he")
```

If we call a method on a node of the tree, we call it **from that position**
So, for example:

```python
master.findValue("hello") #Returns True

otherNode.findValue("hello") #Returns False
#There is no "hello" downwards of "he".
#So if we wanted to get to "hello" from "he", we would need to search for "llo"

otherNode.findValue("llo") #Returns True

#The same applies to adding values, so the following two calls are identical:
master.addValue("here")
otherNode.addValue("re")
```

Now our tree looks like this:

    "h" -> "e" -> "l" -> "l" -> "o"
               -> "y"
               -> "r" -> "e"
        -> "i"
        -> "o" -> "w" -> "d" -> "y"
        
What if we want to find all SubNodes of a Node, e.g. of the "e" from "he" (which would be 'l', 'y', 'r')

```python
otherNode.subNodes
#Returns {'l':<TreeNode Object>, 'y':<TreeNode Object>, 'r':<TreeNode Object>}

#If we wanted to get the Node of the 'r' that follows this Node, we could do the following
yetAnotherNode = otherNode.subNodes['r']

#This achieves the same as calling
yetAnotherNode = otherNode.findNode("r")
```

What if we just want the values of the SubNodes, without dealing with the objects themselves?

```python
otherNode.getSubNodeKeys()
#Returns ['l','y','r']
```
