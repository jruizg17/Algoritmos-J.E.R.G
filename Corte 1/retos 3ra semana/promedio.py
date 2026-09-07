def media(notas, i):
    return sum(notas[i]) / len(notas[i])

notas = [
    [4.0, 3.5, 4.5, 2.0, 5.0, 3.8, 4.2, 3.0, 4.0, 4.5],
    [3.0, 4.0, 3.0, 3.5, 4.5, 2.5, 3.5, 4.0, 5.0, 4.0],
    [5.0, 4.8, 4.2, 3.9, 4.0, 3.5, 4.5, 4.0, 3.8, 4.1]
]

for i in range(3):
    print(f"media asignatura {i+1}: {media(notas, i)}")