def solution(id_list, report, k):
    answer = [0 for _ in id_list]
    reported_dict = {id : 0 for id in id_list}

    for report_data in set(report):
        id, reported_id = report_data.split()
        reported_dict[reported_id] += 1

    for report_data in set(report):
        id, reported_id = report_data.split()
        if reported_dict[reported_id] >= k:
            answer[id_list.index(id)] += 1

    return answer

solution(["muzi", "frodo", "apeach", "neo"], ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"], 2)
solution(["con", "ryan"], ["ryan con", "ryan con", "ryan con", "ryan con"], 3)