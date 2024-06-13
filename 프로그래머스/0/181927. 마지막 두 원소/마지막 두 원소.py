def solution(num_list):
    
    sum = []
    
    for i in range(0, len(num_list)):
        sum.append(num_list[i])
    
    if num_list[-1] > num_list[-2]:
        sum.append(num_list[-1] - num_list[-2])
    elif num_list[-1] < num_list[-2] or num_list[-1] == num_list[-2]:
        sum.append(num_list[-1]*2)
    
    return sum