import time
import random



# def stress_test() -> bool:
#     with open('todo.txt', "r", encoding="utf-8") as file:
#         if file.readlines[-1] 

#простая функция для вывода текста из документа todo.txt
def output():
    with open("todo.txt", "r", encoding="utf-8") as file:
        for i in file:
            for j in i:
                print(j, end="")
                time.sleep(0.05)


#функция для добавления задачи в документ todo.txt
def write() -> None:
    in_txt = "\n\nПожалуйста, введите новую задачу:"
    #постепенный вывод*
    for i in in_txt:
        print(i, end="")
        time.sleep(0.05)
    #ввод задачи
    inp:str = input()

    with open("todo.txt", "a", encoding="utf-8") as file:
        file.write('\n'+ inp)
    for i in "Задача добавлена":
        print(i, end="")
        time.sleep(0.05)
    print("\n")


#дохера замудррённая функция, изменяющая буквы в todo.txt
def change_letters() -> None:
    #открываем сам файл и считываем его, получая список из ВСЕХ букв
    with open("todo.txt", "r", encoding="utf-8") as file:
        todo: list[str] = list(file.read())

    #цикл, который меняет случайные буквы в todo.txt на хз какие, сам уже запутался
    for i in range(random.randint(2,10)):
        todo[random.randint(0, len(todo)-1)] = chr(ord(todo[random.randint(0, len(todo)-1)]))

    #записываем все изменения в todo.txt, параллельно обьединяя список букв в строку
    with open("todo.txt", "w", encoding="utf-8") as file:
        file.write("".join(todo))    

#дохера замудррённая функция, изменяющая почти все буквы в todo.txt
def hard_change() -> None:
#открываем сам файл и считываем его, получая список из ВСЕХ букв
    with open("todo.txt", "r", encoding="utf-8") as file:
        todo: list[str] = list(file.read())

    #цикл, который меняет случайные буквы в todo.txt на хз какие, сам уже запутался
    for i in range(len(todo) - random.randint(2,10)):
        todo[random.randint(0, len(todo)-1)] = chr(ord(todo[random.randint(0, len(todo)-1)]))

    #записываем все изменения в todo.txt, параллельно обьединяя список букв в строку
    with open("todo.txt", "w", encoding="utf-8") as file:
        file.write("".join(todo))    


#функция для сохранения нынешнего состаяния todo.txt
def save() -> str:
    with open("todo.txt", "r", encoding="utf-8") as file:
        return file.read() 

#возврат к какому-либо сохранению
def reset(save) -> None:
    with open("todo.txt", "w", encoding="utf-8") as file:
        file.write(save)


output()

write()

output()

write()

save_1 = save()

change_letters()

output()

reset(save_1)

write()

output()

write()

output()

write()

output()

save_2 = save()

write()

hard_change()

output()

reset(save_2)

write()

output()



#1) сделать домашнюю работу
#2) помыть посуду
#3) поужинать













