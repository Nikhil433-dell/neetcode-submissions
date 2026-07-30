class Solution:
    def isValid(self, s: str):

        myDict = {
            "]": "[",
            "}": "{",
            ")": "("
        }

        myStack = []
        
        for i in s:
            if i in myDict:
                if myStack and myStack[-1] == myDict[i]:
                    myStack.pop()
                else:
                    return False
            else:
                myStack.append(i)
                
            

        return not myStack



