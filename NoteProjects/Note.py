from datetime import datetime
import uuid
import inputOutputHelper

class Note:
    def __init__(self, id = str(uuid.uuid1())[0:3], title = "text",
                 body = "text",
                 date = str(datetime.now().strftime("%d.%m.%Y %H:%M:%S"))):
        self.id = id
        self.title = title
        self.body = body
        self.date = date

    def getId(note):
        return note.id

    def getTitle(note):
        return note.title

    def getBody(note):
        return note.body

    def getDate(note):
        return note.date

    def setId(note):
        note.id = str(uuid.uuid1())[0:3]

    def setTitle(note, title):
        note.title = title

    def setBody(note, body):
        note.body = body

    def setDate(note):
        note.date = str(datetime.now().strftime("%d.%m.%Y %H:%M:%S"))

    def toString(note):
        return note.id + ';' + note.title + ';' + note.body + ';' + note.date

    def mapNote(note):
        return '\nID: ' + note.id + '\n' + 'Name: ' + note.title + '\n' +\
             'Description: ' + note.body + '\n' + 'Date of pbulishing: ' + \
            note.date

    def addNote():
        note = inputOutputHelper.createNote()
        array = inputOutputHelper.readNoteFromFile()
        for notes in array:
            if Note.getId(note) == Note.getId(notes):
                Note.setId(note)
        array.append(note)
        inputOutputHelper.writeNoteToFile(array, 'a')
        print('Note is added...')

    def showNote(text):
        logic = True
        array = inputOutputHelper.readNoteFromFile()
        if text == 'date':
            date = input('Enter date in format dd.mm.yyyy: ')
        for notes in array:

            if text == 'all':
                logic = False
                print(Note.mapNote(notes))
            if text == 'id':
                logic = False
                print('ID: ' + Note.getId(notes))
            if text == 'date':
                logic = False
                if date in Note.getDate(notes):
                    print(Note.mapNote(notes))
        if logic == True:
            print('There are no any notes...')

    def editNote(text):
        id = input('Enter id of note which you are going to do any operation: ')
        array = inputOutputHelper.readNoteFromFile()
        logic = True
        for notes in array:
            if id == Note.getId(notes):
                logic = False
                if text == 'edit':
                    note = inputOutputHelper.createNote()
                    Note.setTitle(notes, note.getTitle())
                    Note.setBody(notes, note.getBody())
                    Note.setDate(notes)
                    print('Note has been changed...')
                if text == 'del':
                    array.remove(notes)
                    print('Note has been removed...')
                if text == 'showNote':
                    print(Note.mapNote(notes))
        if logic == True:
            print('There are no any notes with this id')
        inputOutputHelper.writeNoteToFile(array, 'a')