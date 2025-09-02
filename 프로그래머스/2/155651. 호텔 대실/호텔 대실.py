import heapq

def time_to_minute(time):
    hour, minute = map(int, time.split(":"))
    return (hour * 60) + minute
    
def solution(book_time):
    book_time = [(time_to_minute(start), time_to_minute(end) + 10) for start, end in book_time]
    book_time.sort()
    heap = []
    
    for start, end in book_time:
        if heap and heap[0] <= start:
            heapq.heappop(heap)
        
        heapq.heappush(heap, end)
    
    return len(heap)