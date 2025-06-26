import heapq

def solution(jobs):
    
    answer = 0
    count = 0
    start = -1
    now = 0
    heap = []
    
    while count < len(jobs):
        
        for req_num, job_num in jobs:
            if start < req_num <= now:
                heapq.heappush(heap, (job_num, req_num))
        
        if heap:
            cur_job_num, cur_req_num = heapq.heappop(heap)
            start = now
            now += cur_job_num
            answer += now - cur_req_num
            count += 1
        else:
            now += 1
    
    return answer // len(jobs)