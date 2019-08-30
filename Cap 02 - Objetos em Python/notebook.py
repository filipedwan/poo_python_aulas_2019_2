import datetime

# A variável seguinte é utilizada para guardar o prox. id disponível para uma nova anotação;
last_id = 0

class Note:
    '''Representa uma nota em um notebook. Pode-se combiná-la com
    uma string e armazenar tags para cada nota.'''
    
    def __init__(self, memo, tags=''):
        '''inicializa uma nota com uma anotação (string) e uma
        tag opcional. A data de criação e o id são automatica-
        mente definidos para cada nota.'''
        self.memo = memo
        self.tags = tags
        self.creation_data = datetime.date.today()
        global last_id
        last_id += 1
        self.id = last_id
        
    def match(self, term):
        '''Determina se essa nota corresponde com o string term
        passada como parâmetro. É retornado True se houver cor-
        respondência e falso, caso contrário.
        
        A busca é case sensitive e faz correspondência tanto no
        texto quando nas tags
        '''
        return term in self.memo or term in self.tags


class Notebook:
    '''Representa uma coleção de notas que podem possuir,
    tags associadas, modificadas e buscadas.'''
    
    def __init__(self):
        '''Inicializa um notebook com uma lista vazia de anotações.'''
        self.notes = []
    
    def new_note(self, memo, tags=''):
        '''Cria uma nova nota e a adiciona a lista.'''
        self.notes.append(Note(memo, tags))
        
    def __find_note(self, note_id):
        '''Encontra um Note dado um id. Caso não encontre,
        retorna um objeto nulo (None)'''
        for note in self.notes:
            if note.id == note_id:
                return note
        return None
        
    def modify_memo(self, note_id, memo):
        '''Encontra a anotação pelo id e modifica o texto com o
        novo memo passado como parâmetro.'''
        note = self.__find_note(note_id)
        if note != None:
            note.memo = memo
                
    def modify_tags(self, note_id, tags):
        '''Encontra a anotação pelo id e modifica as tags com as
        novas tags passadas como parâmetro.'''
        note = self.__find_note(note_id)
        if note != None:
            note.tags = tags
                
    def search(self, term):
        '''Procura por todas as notas que possuem correspondência
        com a string term passada como parâmetro.'''
        return [note for note in self.notes if note.match(term)]
