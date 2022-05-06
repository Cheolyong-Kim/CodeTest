# 3진법 변환 후 뒤집기 함수
def ternary_conversion_and_flip_over(l, n):
    if n < 3:
        l.append(int(n))
        return n

    a = int(n % 3)
    l.append(a)

    return ternary_conversion_and_flip_over(l, n / 3)

# 3진법 -> 10진법 변환 함수
def decimal_conversion(l):
    len_l = len(l)
    sum = 0

    for i in range(1, len_l + 1):
        sum += (l.pop() * (3 ** (i - 1)))

    return sum

def solution(n):
    answer = 0
    l = []
    ternary_conversion_and_flip_over(l, n)
    answer = decimal_conversion(l)

    return answer