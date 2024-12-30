def solution(genres, plays):
    answer = []

    genre_songs = {}  # 각 장르별 (재생 목록 인덱스, 재생 횟수) 리스트
    genre_play_count = {}  # 각 장르별 총 재생 횟수

    # 1. 장르별로 노래 정보와 총 재생 횟수 저장
    for index, (genre, play) in enumerate(zip(genres, plays)):
        genre_songs.setdefault(genre, []).append((index, play))

        genre_play_count[genre] = genre_play_count.get(genre, 0) + play

    # 2. 장르별 총 재생 횟수를 기준으로 정렬
    sorted_genres = sorted(genre_play_count.items(), key=lambda x: x[1], reverse=True)

    # 3. 각 장르에서 재생 횟수가 많은 노래 최대 2곡 선택
    for genre, _ in sorted_genres:
        top_songs = sorted(genre_songs[genre], key=lambda x: x[1], reverse=True)[:2]
        answer.extend(index for index, _ in top_songs)

    return answer


