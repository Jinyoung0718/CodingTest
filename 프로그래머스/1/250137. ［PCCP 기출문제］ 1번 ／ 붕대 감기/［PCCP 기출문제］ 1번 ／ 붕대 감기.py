def solution(bandage, health, attacks):
    combo = 0
    t, x, y = bandage
    max_hp = health
    hp = health
    last_time = attacks[-1][0]
    
    attacks_dic = {time : damege for time, damege in attacks}
    
    for sec in range(1, last_time + 1):
        if sec in attacks_dic.keys():
            combo = 0
            hp -= attacks_dic[sec]
            if hp <= 0:
                return -1
        else:
            combo += 1
            hp = min(max_hp, hp + x)
            
            if combo == t:
                combo = 0
                hp = min(max_hp, hp + y)
    
    return hp