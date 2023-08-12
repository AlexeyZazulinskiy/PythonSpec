import model
import view


def menu():
    """Основное меню программы"""
    view.clearConsole()
    choice = -1
    data = model.readFile()
    while choice != "exit":
        operation = {"add": model.newNote, "read": view.readAllNote,
                     "ch": choiceNote, "exit": model.exit}
        choice = view.userInputOperation(
            "Выберите действие: \n add Новая заметка \n read Прочитать все заметки \n ch Выбрать заметку \n exit Выход  ", operation)
        view.clearConsole()
        data = operation[choice](data)


def choiceNote(data):
    """Меню выбора дайствий над заметкой"""
    view.clearConsole()
    view.printShortNoteList(data)
    n = int(input("Введите номер заметки: "))
    view.clearConsole()
    if n < 0 or n > len(data):
        print("Заметка не найдена")
        return data
    view.printNote(n, data)
    operation = {"edit": editNote, "del": model.deleteNote}
    choice = view.userInputOperation(
        "Выберите действие: \n edit Изменить заметку \n del Удалить заметку \n r Отмена \n", operation)
    if choice == "r":
        return data

    operation[choice](n, data)
    return data


def editNote(n, data):
    """Меню редактирования заметки"""
    operation = {"title": model.editNoteTitle, "body": model.editNoteBody}
    choice = view.userInputOperation(
        "Выберите действие: \n title Изменить заголовок \n body Изменить текст \n r Отмена \n", operation)
    if choice == "r":
        return data

    operation[choice](n, data)
    return data
