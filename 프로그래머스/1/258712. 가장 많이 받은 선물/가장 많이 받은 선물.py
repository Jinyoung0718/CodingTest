def solution(friends, gifts):
    n = len(friends)
    idx = {name: i for i, name in enumerate(friends)}

    sent = [[0] * n for _ in range(n)]  # sent[i][j]: i→j 준 횟수
    out_cnt = [0] * n                   # 준 총합
    in_cnt = [0] * n                    # 받은 총합

    for rec in gifts:
        a, b = rec.split()
        i, j = idx[a], idx[b]
        sent[i][j] += 1
        out_cnt[i] += 1
        in_cnt[j] += 1

    # 선물지수
    gift_idx = [out_cnt[i] - in_cnt[i] for i in range(n)]

    next_recv = [0] * n
    for i in range(n):
        for j in range(i + 1, n):
            
            if sent[i][j] > sent[j][i]:
                next_recv[i] += 1
            
            elif sent[i][j] < sent[j][i]:
                next_recv[j] += 1
            
            else:
                if gift_idx[i] > gift_idx[j]:
                    next_recv[i] += 1
                elif gift_idx[i] < gift_idx[j]:
                    next_recv[j] += 1

    return max(next_recv)