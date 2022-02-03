def getNextLiteral(strValue,idx):
    
    result = ""
    strV = strValue[idx]
    
    if strV in [ '(',')','*','/','-','+' ,'^']:
        return [strV,idx+1]
    else:
        while strV in [str(i) for i in range(0,10)]:
            result = result+strV
            idx = idx + 1
            if idx >= len(strValue):
                break
            strV = strValue[idx]
      
    
    return [result,idx]
    

def getListFromExpression(getListFromExpression):
    result = []
    idx =0
    while idx < len(getListFromExpression):
        strValue,idx = getNextLiteral(getListFromExpression,idx)
        result.append(strValue)
        
    return result