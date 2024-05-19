with open("todo.txt", "r", encoding="utf-8") as file:
    todo = list(file.read())

print('\n', len(todo))
