def solution(genres, plays):
    answer = []
    genre_to_total = {}
    genre_to_plays = {}
    
    for idx, (genre, play) in enumerate(zip(genres, plays)):
        genre_to_total[genre] = genre_to_total.get(genre, 0) + play
        genre_to_plays[genre] = genre_to_plays.get(genre, []) + [(idx, play)]
    
    sorted_genre_to_total = sorted(genre_to_total.items(), key = lambda x : x[1], reverse = True)
    
    for genre, _ in sorted_genre_to_total:
        sorted_genre_to_plays = sorted(genre_to_plays[genre], key = lambda x : (-x[1], x[0]))
        top_two_songs = sorted_genre_to_plays[:2]
        
        for idx, _ in top_two_songs:
            answer.append(idx)
    
    return answer