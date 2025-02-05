def solution(genres, plays):
    answer = []
    genre_songs = {}
    genre_play_count = {}
    
    for index, (genre, play) in enumerate(zip(genres, plays)):
        genre_songs.setdefault(genre, []).append((index, play))
        genre_play_count[genre] = genre_play_count.get(genre, 0) + play
    
    sorted_genres = sorted(genre_play_count.items(), key=lambda x : x[1], reverse = True)
    for genre, total_play in sorted_genres:
        top_songs = sorted(genre_songs[genre], key=lambda x: x[1], reverse = True)[:2]
        for index, play in top_songs:
            answer.append(index)
    
    return answer