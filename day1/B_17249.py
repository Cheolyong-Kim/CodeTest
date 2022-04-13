taebo=input()

face=taebo.index('(')
print(taebo[:face].count('@'),taebo[face:].count('@'))