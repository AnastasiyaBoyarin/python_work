import Note

def writeNoteToFile(array, mode):
    file = open("notes.csv", mode='w', encoding='utf-8')
    file.seek(0)
    file.close()
    file = open("notes.csv", mode=mode, encoding='utf-8')
    for notes in array:
        file.write(Note.Note.toString(notes))
        file.write('\n')
    file.close


def readNoteFromFile():
    try:
        array = []
        file = open("notes.csv", "r", encoding='utf-8')
        notes = file.read().strip().split("\n")
        for n in notes:
            split_n = n.split(';')
            note = Note.Note(
                id = split_n[0], title = split_n[1], body = split_n[2], date = split_n[3])
            array.append(note)
    except IOError:
        print('There are no any notes in the file...')
    finally:
        return array

def createNote():
    title = input('Enter title of note: ')
    body = input('Enter descrption of note: ')
    return Note.Note(title=title, body=body)

def run():
    userChoice = ''
    while userChoice != '7':
        print("\nThis is program 'Notes'. Menu:"
              "\n\n1 - Show all notes from file"
              "\n2 - Add note"
              "\n3 - Remove note"
              "\n4 - Edit note"
              "\n5 - Select note by date"
              "\n6 - Select note by id"
              "\n7 - Exit"
              "\n\nEnter action: ")
        userChoice = input().strip()
        if userChoice == '1':
            Note.Note.showNote('all')
        if userChoice == '2':
            Note.Note.addNote()
        if userChoice == '3':
            Note.Note.showNote('all')
            Note.Note.editNote('del')
        if userChoice == '4':
            Note.Note.showNote('all')
            Note.Note.editNote('edit')
        if userChoice == '5':
            Note.Note.showNote('date')
        if userChoice == '6':
            Note.Note.showNote('id')
            Note.Note.editNote('showNote')
        if userChoice == '7':
            print("The end!")
            break