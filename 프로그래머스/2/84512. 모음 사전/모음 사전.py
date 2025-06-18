def solution(words):
    answer = 0
    word_list = []
    alpha = "AEIOU"
    
    def dfs(depth, word):
        
        if depth == 5:
            return
        
        for i in range(5):
            word_list.append(word + alpha[i])
            dfs(depth + 1, word + alpha[i])
            
            
    
    dfs(0, "")
    
    return word_list.index(words) + 1