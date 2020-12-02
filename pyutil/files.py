def fileappend(filename,thing):
    a = open(filename, 'a')
    a.write(str(thing))
    a.close()

def fileoverwrite(filename,thing):
    a = open(filename, 'w')
    a.write(str(thing))
    a.close()

def filereplace(filename, patternToReplace, replacementString, regex=False):
    a = open(filename, 'r+')
    file_content = a.read()
    if regex:
        from re import sub
        new_content = sub(patternToReplace,replacementString,file_content)
    else:
        new_content = file_content.replace(patternToReplace,replacementString)
    a.seek(0)
    a.truncate(0)
    a.write(new_content)
    a.close()
