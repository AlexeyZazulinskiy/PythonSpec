import model


def menu():
    """Основное меню программы"""
    model.clearConsole()
    choice = -1
    data = model.readFile()
    while choice != 0:
        print("Выберите действие: \n add Новая заметка \n read Прочитать все заметки \n choice Выбрать заметку \n exit Выход  ")
        choice = input()
        model.clearConsole()
        operation = {"add": model.newNote, "read": model.readAllNote,
                     "choice": choiceNote, "exit": model.exit}
        data = operation[choice](data)


def choiceNote(data):
    """Меню выбора дайствий над заметкой"""
    model.clearConsole()
    c = 0
    for i in data:
        print(str(c), i)
        c += 1
    n = int(input("Введите номер заметки: "))
    model.clearConsole()
    if n < 0 | n > len(data):
        print("Заметка не найдена")
        return 0
    model.printNote(n, data)
    choice = input(
        "Выберите действие: \n edit Изменить заметку \n del Удалить заметку \n r Отмена ")
    if choice == 0:
        return 0
    operation = {"edit": editNote, "del": model.deleteNote, "r": 0}
    operation[choice](n, data)
    return data


def editNote(n, data):
    """Меню редактирования заметки"""
    choice = input(
        "Выберите действие: \n title Изменить заголовок \n body Изменить текст \n r Отмена  ")
    if choice == 0:
        return 0
    operation = {"title": model.editNoteTitle,
                 "body": model.editNoteBody, "r": 0}
    operation[choice](n, data)
    return data
