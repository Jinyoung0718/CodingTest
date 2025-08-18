def solution(lottos, win_nums):
    zero_cnt = lottos.count(0)
    match_cnt = len(set(lottos) & set(win_nums))
    
    def to_rank(c):
        if c >= 2:
            return 7 - c  # ex) 2개가 매개변수로 들어오면 5등 반환
        
        return 6
    
    best = to_rank(match_cnt + zero_cnt)
    worst = to_rank(match_cnt)
    return [best, worst]