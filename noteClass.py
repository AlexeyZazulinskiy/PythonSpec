import datetime

class noteC:
    TitleName = ["Хэш = ","Дата = ","Заголовок = ","Текст = "]
    nTitle = ""
    nBody = ""
    nDate = datetime.date.today()
    noteLen = 4
    def newNote (title, body):
        """Создание новой заметки с присвоением времени создания и хеш суммы"""
        noteC.nTitle = str(title)
        noteC.nBody = str(body)
        h = hash(noteC.nTitle + noteC.nBody + str(noteC.nDate))
        return [h, str(noteC.nDate),noteC.nTitle,noteC.nBody]
        
    def getNote(i):
        """Проверка и подготовка строки массива для записи в фаил"""
        if len(i) != noteC.noteLen:
            print("data error")
            return i
        res =  str(i[0]) + ";" + i[1] + ";" + i[2] + ";" + i[3] + "\n"
        return res
    
    def readNoteStrip(data):
        """Убирание символа переноса строки при чтении из файла"""
        for i in data:
            if len(i) != noteC.noteLen:
                print("data error")
            i[len(i)-1]= str(i[len(i)-1]).strip()
        return data
    
    def setTitle(i,s):
        """Изменение заголовка заметки"""
        i[2] = s
        return i
    
    def setBody(i,s):
        """Изменение текста заметки"""
        i[3] = s
        return i