def solution(genres, plays):
    answer = []
    
    genre_to_songs = {}
    genre_to_total = {}
    
    for idx, (genre, play) in enumerate(zip(genres, plays)):
        
        if genre not in genre_to_songs:
            genre_to_songs[genre] = [(idx, play)]
        else:
            genre_to_songs[genre].append((idx, play))
        
        if genre not in genre_to_total:
            genre_to_total[genre] = play
        else:
            genre_to_total[genre] += play
    
    sorted_genre_to_total = sorted(genre_to_total.items(), key=lambda x : x[1], reverse = True)
    
    for genre, _ in sorted_genre_to_total:
        sorted_genre_to_songs = sorted(genre_to_songs[genre], key=lambda x : (-x[1], x[0]))
        top_two_songs = sorted_genre_to_songs[:2]
        
        for idx, _ in top_two_songs:
            answer.append(idx)
    
    return answer