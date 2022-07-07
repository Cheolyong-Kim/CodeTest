def solution(lottos, win_nums):
    num_of_z = lottos.count(0)  # lottos의 0 개수를 세둠

    # lottos 원소가 전부 0이면
    if num_of_z == 6:
        top_ranking = 1
        lowest_ranking = 6
        answer = [top_ranking, lowest_ranking]
        return answer

    # lottos 원소가 전부 0이 아니면
    elif num_of_z == 0:
        set_lottos = set(lottos)
        set_win_nums = set(win_nums)
        dif_set = set_lottos - set_win_nums
        for i in dif_set:
            del lottos[lottos.index(i)]
        if len(lottos) == 0 or len(lottos) == 1:
            top_ranking = 6
            lowest_ranking = 6
            answer = [top_ranking, lowest_ranking]
            return answer
        else:
            top_ranking = 7 - len(lottos)
            lowest_ranking = 7 - len(lottos)
            answer = [top_ranking, lowest_ranking]
            return answer
    # 그 외
    else:
        lottos_ex_0 = list(set(lottos))
        lottos_ex_0.remove(0)

        set_lottos_ex_0 = set(lottos_ex_0)
        set_win_nums = set(win_nums)
        dif_set = set_lottos_ex_0 - set_win_nums
        for i in s:
            del lottos[lottos.index(i)]
        top_ranking = 7 - len(lottos)
        lowest_ranking = 7 - (len(lottos) - num_of_z)
        answer = [top_ranking, lowest_ranking]
        return answer