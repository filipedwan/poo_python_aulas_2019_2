import sys

from notebook import Notebook, Note

class Menu:
    '''Mostra um menu e aciona as ações apropriadas com base
    nas opções escolhidas.'''
    def __init__(self):
        self.notebook = Notebook()
        self.choices = {
            "1": self.show_notes,
            "2": self.search_notes,
            "3": self.add_note,
            "4": self.modify_note,
            "5": self.quit
        }
    def display_menu(self):
        print("""
        Notebook Menu
    
        1. Mostrar todas as Notas
        2. Buscar Notas
        3. Adicionar Nota
        4. Modificar Nota
        5. Sair
        """)
    def run(self):
        '''Mostra o menu e aciona a opção escolhida.'''
        while True:
            self.display_menu()
            choice = input("Escolha uma opção: ")
            action = self.choices.get(choice)
            if action:
                action()
            else:
                print("{0} não é uma opção válida".format(choice))

    def show_notes(self, notes=None):
        if not notes:
            notes = self.notebook.notes
        for note in notes:
            print("{0}: {1}\n{2}".format(note.id, note.tags, note.memo))
    
    def search_notes(self):
        term = input("Buscar por: ")
        notes = self.notebook.search(term)
        self.show_notes(notes)
        
    def add_note(self):
        memo = input("Entre com a anotação: ")
        self.notebook.new_note(memo)
        print("Sua anotação foi adicionada.")
        
    def modify_note(self):
        id = input("Entre com o id da anotação: ")
        memo = input("Entre com a anotação: ")
        tags = input("Entre com as tags: ")
        if memo:
            self.notebook.modify_memo(int(id), memo)
        if tags:
            self.notebook.modify_tags(int(id), tags)
            
    def quit(self):
        print("Obrigado por usar nosso sitema!")
        sys.exit(0)
        
if __name__ == "__main__":
    Menu().run()
