class TreeNode:
    def __init__(self,value=None): #Value is usually a string, but can be anything that support slicing and length, as well as == comparisons between its elements (chars, list elements, etc)
        if value is not None: #Value should not exist for masternode
            self.value = value #A valid value for all subnodes, None for masternode
        self.subNodes = {}

    def addValue(self,valueiterable):
        firstValue, valueiterable = valueiterable[0],valueiterable[1:] #Can never be empty, unless an empty list is passed to masternode
        if firstValue in self.subNodes:
            nextNode = self.subNodes[firstValue]
        else:
            nextNode = TreeNode(firstValue)
            self.subNodes[firstValue] = nextNode
            
        if len(valueiterable) > 0 : #Not Empty
            nextNode.addValue(valueiterable) #First index was removed

    def findValue(self,searchedValue,returnNode=False):
        nextCharacter, searchedValue = searchedValue[0],searchedValue[1:]
        if nextCharacter in self.subNodes:
            if len(searchedValue) == 0:
                if returnNode:
                    return self.subNodes[nextCharacter]
                return True
            else:
                return self.subNodes[nextCharacter].findValue(searchedValue,returnNode)
        else:
            if returnNode:
                return None
            return False

    def findNode(self,searchedValue):
        return self.findValue(searchedValue,True)

    def getSubNodeKeys(self):
        return list(self.subNodes.keys())

#Testing
'''
master = TreeNode()
master.addValue("hello")
master.addValue("hey")
master.addValue("hi")
master.addValue("howdy")
'''