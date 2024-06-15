def solution(numLog):
    result = ""
    dict = {1:'w', -1:"s", 10:"d", -10:"a"}
    
    for i in range(1, len(numLog)):
        result += dict[numLog[i] - numLog[i-1]]
    
    return result