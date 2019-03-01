def fileappend(filename,thing):
    a = open(filename, 'a')
    if not isinstance(thing, str):
        thing = str(string)
    a.write(thing)
    a.close()

def overwrite(filename,thing):
    a = open(filename, 'w')
    if not isinstance(thing, str):
        thing = str(string)
    a.write(thing)
    a.close()

def readAll(filename):
    a = open(filename, 'r')
    string = ""
    for line in a:
        string+=line
    a.close()
    return string
