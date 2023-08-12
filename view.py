import noteClass
import os


def userInputOperation(s, dic):
    while True:
        inp = input(s)
        if inp in dic:
            return inp
        else:
            print("Ошибка ввода")


def printShortNoteList(data):
    """Выводит на экран пронумерованный список заметок"""
    c = 0
    for i in data:
        print(str(c) + ") ", noteClass.noteC.shortNote(i))
        c += 1


def readAllNote(data):
    """Выведение в консоль всех заметок прочитанных из файла"""
    clearConsole()
    for i in data:
        print(i)
    return data


def printNote(n, data):
    """Вывод в консоль конкретной заметки"""
    clearConsole()
    s = noteClass.noteC.TitleName
    for i in range(len(data[n])):
        print(s[i], data[n][i])


def clearConsole(): return os.system('cls')

"""Очистка консоли"""
