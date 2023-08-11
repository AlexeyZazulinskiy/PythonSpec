
import model

def menu():
    """Основное меню программы"""
    choice = -1
    data = model.readFile()
    while choice != 0:
        print("Выберите действие: \n 1 Новая заметка \n 2 Прочитать все заметки \n 3 Выбрать заметку \n 0 Выход  ")
        choice = int(input())
        operation = {1: model.newNote, 2: model.readAllNote, 3: findNote, 0:model.exit}
        data = operation[choice](data)

def findNote(data):
    """Меню выбора дайствий над заметкой"""
    c = 0
    for i in data:
        print(str(c),i )
        c += 1
    n = int(input("Введите номер заметки: ")) 
    choice = int(input("Выберите действие: \n 1 Изменить заметку \n 2 Удалить заметку \n 3 Распечатать заметку \n 0 Отмена "))
    if choice  == 0: return 0
    operation = {1: editNote, 2: model.deleteNote, 3: model.printNote, 0: 0} 
    operation[choice](n, data)
    return data

def editNote(n, data):
    """Меню редактирования заметки"""
    choice = int(input("Выберите действие: \n 1 Изменить заголовок \n 2 Изменить текст \n 0 Отмена  "))
    if choice  == 0: return 0
    operation = {1: model.editNoteTitle, 2: model.editNoteBody, 0: 0} 
    operation[choice](n, data)
    return data
    