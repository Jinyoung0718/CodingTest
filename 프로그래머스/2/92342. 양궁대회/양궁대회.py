def solution(n, info):
    answer = []
    
    # 10, 9, 8, ... , 0
    ryan = [0] * 11
    diff = 0


    # m: 쏜 화살 수, idx: 현재 탐색하는 과녁 번호
    def dfs(m, idx):
        nonlocal answer, diff, ryan

        if m == n:
            r = 0
            a = 0

            for j in range(11):
                # 라이언이 더 많이 맞췄으면 → 라이언 점수 획득
                if ryan[j] > info[j]:
                    r += 10 - j
                
                # 어피치가 같거나 더 많이 맞췄으면 → 어피치 점수 획득
                elif info[j] != 0 and ryan[j] <= info[j]:
                    a += 10 - j
                    
			# 라이언이 점수가 더 높을 때
            if r > a:
                
            	# 격차가 더 크다면 바로 갱신
                if diff < r - a:
                    diff = r - a
                    answer = ryan[:]
                    
				# 격차가 같다면 낮은 점수를 더 많이 쏜 걸로 갱신
                elif diff == r - a:
                    # 0부터 비교함 -> 낮은 점수부터 체크
                    for i in range(10, -1, -1):
                        
                        # 현재 배열이 기존 답보다 낮은 점수에 덜 쐈다면 그대로 종료. 기존 답이 우선
                        if ryan[i] < answer[i]:
                            break
                        
                        #현재 배열이 기존 답보다 낮은 점수에 더 많이 쐈다면 교체.
                        if ryan[i] > answer[i]:
                            answer = ryan[:]
                            break
            
            return

        for i in range(idx, 11):
            ryan[i] += 1
            dfs(m + 1, i)
            ryan[i] -= 1


    dfs(0, 0)

    return answer if answer else [-1]