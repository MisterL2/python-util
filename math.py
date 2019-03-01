def isPrime(num):
    i = 1
    if num < 0:
        num = abs(num)
    elif num == 0:
        return False

    if num in [1,2]:
        return True

    while num >= i**2: #>= because e.g. 9 -> 3*3
        if i == 1:
            pass
        elif num % i == 0:
            return False
        i+=1 #2 in first iteration, as a number is always divisible by 1.
    return True #if no divisors found, it is a prime
        


def findPrimes(minimum,maximum): #Returns primes within a range
    primes = []
    for i in range(minimum,maximum):
        if isPrime(i):
            primes.append(i)
    return primes


def findFactors(num):
    factors = []
    if isPrime(num):
        factors.append(num)
        return factors

    i = 1
    while num >= i**2: #>= because e.g. 9 -> 3*3
        if num % i == 0 and i!=1:
            factors.append(i)
            factors.append(int(num/i))
        i+=1 #1 in first iteration
    return factors


def findFactorTuples(num):
    factorTuples = []
    if isPrime(num):
        return factorTuples

    i = 1
    while num >= i**2: #>= because e.g. 9 -> 3*3
        if i == 1:
            pass
        elif num % i == 0:
            factorTuples.append((i,int(num/i))) #Convert to int, as the result of an integer division is always a float in python
        i+=1 #2 in first iteration
    return factorTuples
        
def hasRoot(num,power=2): #Similar to math.sqrt() when power == 2
    i = 1
    while num >= i**power:
        if num == i**power:
            return True, i
        i+=1
    return False


def findIntersect(eq1,eq2): #Both equations are tuples of form (gradient,start)
    try:
        intersectX = (eq2[1] - eq1[1])/(eq1[0]-eq2[0])
    except ZeroDivisionError:
        return None
    intersectY = eq1[0]*intersectX + eq1[1]
    return (intersectX,intersectY)


def findGradient(coord1,coord2): #Both coordinates are tuples of form (x,y)
    return (coord2[1]-coord1[1])/(coord2[0]-coord1[0])
    
def circlePerimeter(r):
    from math import pi
    return 2*pi*r

def triangleArea(a,b,c=None):
    if c is None: #first variable refers to base length, second variable refers to height
        return 0.5*a*b
    else: #all 3 variables refer to side lengths
        from math import sqrt
        s = (a+b+c)/2
        return sqrt(s*(s-a)*(s-b)*(s-c))

def circleArea(radius):
    from math import pi
    return r**2*pi


def trapezoidArea(a,b,d): #a and b refer to the parallel sides, d to the distance between them
    return d*(a+b)/2


def sphereVolume(r):
    from math import pi
    return (4/3)*pi*r**3

def prismVolume(a,b,c=None):
    if c is None:
        return cylinderVolume(a,b)
    else:
        return a*b*c

def cylinderVolume(area,height):
    return area*height

def pyramidVolume(area,height):
    return area*height/3

def coneVolume(area,height):
    return pyramidVolume(area,height)
