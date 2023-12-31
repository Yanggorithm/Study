def solution(genres, plays):
    answer = []
    genreDict = dict()
    lenGenres = len(genres)
    for i in range(lenGenres):
        genre = genres[i]
        play = plays[i]
        if genreDict.get(genre):
            genreDict[genre].append((play, i))
            genreDict[genre][0] += play
        else:
            genreDict[genre] = [play, (play, i)]
    genreList = sorted(list(genreDict.values()), key=lambda x: x[0], reverse=True)

    for g in genreList:
        lenG = len(g)
        ng = sorted(g[1:], key=lambda x: (x[0], -x[1]), reverse=True)
        for i in range(min(2, lenG-1)):
            answer.append(ng[i][1])
    return answer