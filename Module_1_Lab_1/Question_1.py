import sys
import re
def doSomething(inval):
    length = len(inval)
    
    upper = len(re.findall(r'[A-Z]',inval))
    lower = len(re.findall(r'[a-z]',inval))
    digit = len(re.findall(r'\d',inval))
    symbols = length - upper - lower - digit
    
    print(round((upper/length)*100,3),"%",
    round((lower/length)*100,3),"%",
    round((digit/length)*100,3),"%",
    round((symbols/length)*100,3),"%")
    
    return 0
    
inputVal = input()    
doSomething(inputVal)