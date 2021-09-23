#Alexander den Otter  -  9067410
Dagen = [
    "maandag",
    'dinsdag',
    'woensdag',
    'donderdag',
    'vrijdag',
    'zaterdag',
    'zondag'
]


Dag = int(input('-----------------\nOp welke dag van de week ben je vrij?\n-----------------\nTyp 1 voor Maandag\nTyp 2 voor Dinsdag\nTyp 3 voor Woensdag\nTyp 4 voor Donderdag\nTyp 5 voor Vrijdag\nTyp 6 voor Zaterdag\nTyp 7 voor Zondag\n-----------------\n--->'))

a = Dag

i = 1
while i <= a:
    print(str(Dagen[i-1]))
    i = i + 1


