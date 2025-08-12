def date_to_days(date):
    y, m, d = map(int, date.split('.'))
    return (y * 12 * 28) + (m * 28) + d

def solution(today, terms, privacies):
    today_days = date_to_days(today)
    answer = []
    terms_dic = {}
    
    for n in terms:
        part_1, part_2 = n.split()
        terms_dic[part_1] = int(part_2)
    
    for idx, privacy in enumerate(privacies, start=1):
        date, plan = privacy.split()
        months = terms_dic[plan]
        
        start_days = date_to_days(date)
        expire_days = start_days + (months * 28)
        
        if expire_days <= today_days:
            answer.append(idx)
    
    return answer
