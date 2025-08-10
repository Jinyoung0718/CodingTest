from itertools import permutations

def check(users, banned_id):
    
    for i in range(len(users)):
        if len(users[i]) != len(banned_id[i]):
            return False 
        
        for j in range(len(users[i])):    
            if banned_id[i][j] == '*':
                continue
            
            if users[i][j] != banned_id[i][j]:
                return False
    
    return True

def solution(user_id, banned_id):
    
    perm = permutations(user_id, len(banned_id))
    ban_set = []
    
    for users in perm:
        
        if check(users, banned_id):
            users = set(users)
            if users not in ban_set:
                ban_set.append(users)
        else:
            continue    
    
    return len(ban_set)