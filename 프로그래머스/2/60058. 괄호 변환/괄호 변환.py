def solution(p):
    # 올바른 괄호인지 확인
    def is_correct(s):
        cnt = 0
        for ch in s:
            if ch == '(':
                cnt += 1
            else:
                cnt -= 1
                if cnt < 0:
                    return False
        return cnt == 0

    # 메인 변환 함수
    def transform(w):
        if not w:
            return ""
        # 균형잡힌 u, v 분리
        balance = 0
        for i, ch in enumerate(w):
            balance += 1 if ch == '(' else -1
            if balance == 0:
                u, v = w[:i+1], w[i+1:]
                break
        # u가 올바르면 v를 재귀 변환 후 붙임
        if is_correct(u):
            return u + transform(v)
        # u가 올바르지 않으면 규칙 4 수행
        s = "(" + transform(v) + ")"
        flipped = "".join('(' if c == ')' else ')' for c in u[1:-1])
        return s + flipped

    return p if is_correct(p) else transform(p)
