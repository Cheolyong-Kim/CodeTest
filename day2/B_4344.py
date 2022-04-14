testcase_num = int(input())

def avg(list):
    avg_num = sum(list[1:]) / list[0]
    return avg_num

for i in range(testcase_num):
    score_list = list(map(int, input().split()))
    score_over_avg = [score for score in score_list[1:] if score > avg(score_list)]
    ratio_of_student_over_avg = (len(score_over_avg) / score_list[0]) * 100
    print(f"{ratio_of_student_over_avg:.03f}%")
