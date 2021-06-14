from collections import defaultdict
def solution(genres, plays):
    genere_play_tot = defaultdict(int)
    genere_play_cnt = defaultdict(list)
    
    for idx, li in enumerate(zip(genres, plays)):
        genere_play_tot[li[0]] += li[1]
        genere_play_cnt[li[0]].append([li[1], idx])

    genere_play_tot = sorted(genere_play_tot.keys(), key=lambda x: genere_play_tot[x], reverse=True)
    
    answer = []
    for gen in genere_play_tot:
        order = sorted(genere_play_cnt[gen], key=lambda x: (-x[0], x[1]))
        if len(order) == 1:
            answer.append(order[0][1])
        else:
            answer.append(order[0][1])
            answer.append(order[1][1])
    return answer


if __name__=="__main__":
    print(solution(["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500]))