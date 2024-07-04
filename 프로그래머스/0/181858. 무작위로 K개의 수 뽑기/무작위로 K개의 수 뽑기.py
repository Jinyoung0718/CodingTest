def solution(arr, k):
    result = []
    
    # arr의 길이만큼 반복
    # arr의 원소를 순서대로 뽑아서 result안에 있는지 확인
    for i in range(len(arr)):
    	# 만약 안에 없다면, result에 추가
        if arr[i] not in result:
            result.append(arr[i])
        else:
            pass
            
    # 만들어진 result의 길이가 k보다 작다면
    # 길이의 차이만큼 뒤쪽으로 -1을 추가
    if len(result) < k:
        diff = k - len(result)
        for _ in range(diff):
            result.append(-1)
        answer = result
    # 만약 k보다 크다면, k개까지만큼 잘라주기
    else:
        answer = result[:k]
        
    return answer