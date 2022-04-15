f_records = input().split()

players = {
    "Jay" : 0,
    "John" : 0,
    "Jack" : 0,
    "Jo" : 0
}

for f_record in f_records:
    players[f_record] += 1

min_foul = min(players.values())
for player, foul in players.items():
    if foul == min_foul:
        print(player)
print(min_foul)