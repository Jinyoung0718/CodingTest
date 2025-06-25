def solution(genres, plays):
    
    answer = []
    genre_total = {}
    genre_plays = {}
    
    for idx, (genre, play) in enumerate(zip(genres, plays)):
        
        if genre not in genre_plays:
            genre_plays[genre] = [(idx, play)]
        else:
            genre_plays[genre].append((idx, play))
        
        
        if genre not in genre_total:
            genre_total[genre] = play
        else:
            genre_total[genre] += play
    
    sort_genre_total = sorted(genre_total.items(), key = lambda x : x[1], reverse = True)
    
    for key, _ in sort_genre_total:
        sort_genre_plays = sorted(genre_plays[key], key = lambda x : (-x[1], x[0]))
        for idx, _ in sort_genre_plays[:2]:
            answer.append(idx)
    
    return answer