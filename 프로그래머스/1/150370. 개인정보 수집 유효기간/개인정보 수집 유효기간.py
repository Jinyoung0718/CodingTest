def date_to_day(date):
    year, month, day = map(int, date.split("."))
    return (year * 12 * 28) + (month * 28) + day
    
def solution(today, terms, privacies):
    answer = []
    today = date_to_day(today)
    terms_dic = {}
    
    for term in terms:
        plan, time = term.split()
        terms_dic[plan] = int(time)
        
    for idx, privacy in enumerate(privacies):
        date, plan = privacy.split()
        
        term_month = terms_dic[plan]
        expire_date = date_to_day(date) + (term_month * 28)
        
        if expire_date <= today:
            answer.append(idx + 1)
    
    return answer