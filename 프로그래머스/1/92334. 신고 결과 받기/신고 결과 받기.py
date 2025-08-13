def solution(id_list, report, k):
    # 1) 피신고자별 신고자 집합 초기화
    reported_by = {}
    for uid in id_list:
        reported_by[uid] = set()

    # 2) 중복 신고 제거 후 집계
    unique_reports = set(report)
    for entry in unique_reports:
        reporter, target = entry.split()
        reported_by[target].add(reporter)

    # 3) 정지 대상 선별 (신고자 수 >= k)
    suspended = set()
    for uid, reporters in reported_by.items():
        if len(reporters) >= k:
            suspended.add(uid)

    # 4) 메일 수 계산
    mail = {}
    
    # 초기화
    for uid in id_list:
        mail[uid] = 0

    # 정지된 대상의 신고자에게 메일 +1
    for target in suspended:
        reporters = reported_by.get(target, set())
        for reporter in reporters:
            mail[reporter] += 1

    answer = []
    for uid in id_list:
        answer.append(mail[uid])

    return answer

