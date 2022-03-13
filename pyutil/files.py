def fileappend(filename,thing):
    a = open(filename, 'a')
    a.write(str(thing))
    a.close()

def fileoverwrite(filename,thing):
    a = open(filename, 'w')
    a.write(str(thing))
    a.close()

def filereplace(filename, patternToReplace, replacementString, out=None, regex=False):
    with open(filename, 'r+') as f:
        file_content = f.read()
        if regex:
            from re import sub
            new_content = sub(patternToReplace,replacementString,file_content)
        else:
            new_content = file_content.replace(patternToReplace,replacementString)
        if out is None:
            f.seek(0)
            f.truncate(0)
            f.write(new_content)
        else:
            with open(out, 'w') as out_file:
                out_file.write(new_content) # Opening as 'w' means I overwrite all content in that file

def filereplace_multi(filename, replacementMap, out=None):
    from re import compile, sub, escape
    with open(filename, 'r+') as f:
        file_content = f.read()
        regex_pattern = compile(f"({'|'.join(map(escape, replacementMap.keys()))})")
        new_content = regex_pattern.sub(lambda match_object: replacementMap[match_object.string[match_object.start():match_object.end()]], file_content)
        if out is None:
            f.seek(0)
            f.truncate(0)
            f.write(new_content)
        else:
            with open(out, 'w') as out_file:
                out_file.write(new_content) # Opening as 'w' means I overwrite all content in that file
    