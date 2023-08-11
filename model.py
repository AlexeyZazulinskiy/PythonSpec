import noteClass

def newNote (data):
    """Создание новой заметки"""
    t = input("Введите заголовок: ")
    b = input("Введите заметку: ")
    data.append(noteClass.noteC.newNote(t,b))
    appendToFile(data[len(data)-1])
    return data

def appendToFile (i):
    """Дописывание в фаил новой заметки (используется только для новый заметок)"""
    with open('notes.txt', 'a', encoding= 'utf-8') as f:
        f.writelines(noteClass.noteC.getNote(i))
    print("Заметка сохранена")
    
def readAllNote(data):
    """Выведение в консоль всех заметок прочитанных из файла"""
    for i in data:
        print(i)
    return data
    
def deleteNote(n, data):
    """Удаление заметки"""
    del data[n]

def editNoteTitle(n,data):
    """Изменение загодовка заметки"""
    s = input("Введите новый заголовок заметки: ")
    res = noteClass.noteC.setTitle(data[n],s)
    data[n] = res

def editNoteBody(n,data):
    """Изменение текста заметки"""
    s = input("Введите новый текст заметки: ")
    res = noteClass.noteC.setBody(data[n],s)
    data[n] = res

def printNote(n, data):
    """Вывод в консоль конкретной заметки"""
    print('clear')
    s = noteClass.noteC.TitleName
    for i in range(len(data[n])):
        print(s[i], data[n][i])
    
def readFile():
    """Чтение заметок из файла в список data"""
    data = [i.split(';') for i in open('notes.txt', 'r', encoding= 'utf-8')]
    print(data)
    return noteClass.noteC.readNoteStrip(data)

def exit(data):
    """Сохранение списка заметок data, с перезаписью файла и завершение программы"""
    with open('notes.txt', 'w', encoding= 'utf-8') as f:
        for i in data:
            f.writelines(noteClass.noteC.getNote(i))
    return 0