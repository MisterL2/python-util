def fileappend(filename,thing):
    a = open(filename, 'a')
    a.write(str(thing))
    a.close()

def fileoverwrite(filename,thing):
    a = open(filename, 'w')
    a.write(str(thing))
    a.close()

def filereplace(filename,regexToReplace,replacementString):
    a = open(filename, 'r+')
    file_content = a.read()    
    from re import sub
    a.seek(0)
    a.write(sub(regexToReplace,replacementString,file_content))
    a.close()
