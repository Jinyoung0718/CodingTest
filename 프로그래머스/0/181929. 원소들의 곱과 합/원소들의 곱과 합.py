def solution(num_list):
    
    multiple = 1
    square  = 0
    
    for i in range(0, len(num_list)):
        multiple *= num_list[i]
        
    for i in range(0, len(num_list)):
        square  += num_list[i]
    
    square = square**2
    
    if multiple > square:
        return 0
    
    if multiple < square:
        return 1
    