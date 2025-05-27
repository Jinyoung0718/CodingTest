def solution(genres, plays):
    answer = []
    genre_to_songs = {}       # 장르별로 (고유번호, 재생 수) 튜플 리스트
    genre_total_plays = {}    # 장르별 총 재생 수

    for song_id, (genre, play_count) in enumerate(zip(genres, plays)):
        # 장르별 노래 모음
        if genre not in genre_to_songs:
            genre_to_songs[genre] = [(song_id, play_count)]
        else:
            genre_to_songs[genre].append((song_id, play_count))

        # 장르별 총 재생 수 계산
        if genre not in genre_total_plays:
            genre_total_plays[genre] = play_count
        else:
            genre_total_plays[genre] += play_count

    # 장르를 총 재생 수 기준으로 정렬
    sorted_genres = sorted(genre_total_plays.items(), key=lambda x: x[1], reverse=True)

    for genre, _ in sorted_genres:
        # 해당 장르의 노래들을 재생 수 내림차순, 고유번호 오름차순으로 정렬
        sorted_songs = sorted(genre_to_songs[genre], key=lambda x: (-x[1], x[0]))
        top_two_songs = sorted_songs[:2]  # 최대 2곡까지 수록
        for song_id, _ in top_two_songs:
            answer.append(song_id)

    return answer