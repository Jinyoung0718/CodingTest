from itertools import permutations

def solution(k, dungeons):
    answer = []

    for perm in permutations(dungeons):
        total = 0
        k_copy = k
        for i, j in perm:
            if i > k_copy:
                break
            k_copy -= j
            total += 1
        answer.append(total)

    return max(answer)
