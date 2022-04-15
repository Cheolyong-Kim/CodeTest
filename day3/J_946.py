n = int(input())

capital_dic = {}
for i in range(n):
    country, capital = input().split()
    capital_dic[country]=capital

find_capital=input()
print(capital_dic[find_capital] if capital_dic.get(find_capital) else 'Unknown Country')
