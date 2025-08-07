def time_to_sec(t):
    m, s = map(int, t.split(':'))
    return m * 60 + s

def sec_to_time(s):
    m = s // 60
    s = s % 60
    return f"{m:02d}:{s:02d}"

def solution(video_len, pos, op_start, op_end, commands):
    video_len_sec = time_to_sec(video_len)
    pos_sec = time_to_sec(pos)
    op_start_sec = time_to_sec(op_start)
    op_end_sec = time_to_sec(op_end)

    for cmd in commands:
        # 1차 오프닝 구간 체크
        if op_start_sec <= pos_sec <= op_end_sec:
            pos_sec = op_end_sec

        # 명령 실행
        if cmd == "prev":
            pos_sec = max(0, pos_sec - 10)
            
        elif cmd == "next":
            pos_sec = min(video_len_sec, pos_sec + 10)

        # 2차 오프닝 구간 체크
        if op_start_sec <= pos_sec <= op_end_sec:
            pos_sec = op_end_sec

    return sec_to_time(pos_sec)

