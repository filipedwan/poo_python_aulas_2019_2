from GUI import Gui
from dao import ClientDAO
from tkinter import END
from model import Client

'''
Adaptado de:
https://github.com/brenordv/python-tutorial-tkinter-sqlite-01
http://raccoon.ninja/pt/dev-pt/tutorial-aplicacao-em-python-sqlite-parte-01/
https://raccoon.ninja/pt/dev-pt/tutorial-aplicacao-em-python-sqlite-parte-02/
http://raccoon.ninja/pt/dev-pt/tutorial-aplicacao-em-python-sqlite-parte-03/
http://raccoon.ninja/pt/dev-pt/tutorial-aplicacao-em-python-sqlite-parte-04/
'''

class Controller:
    def __init__(self):
        self.gui = Gui()
        self.dao = ClientDAO()
        self.selected = None #cliente selecionado
        self.currentClient = Client()
    
    def view_command(self):
        "método para visualização dos resultados"
        try:
            rows = self.dao.view()
            self.gui.listClientes.delete(0, END)
            for r in rows:
                self.gui.listClientes.insert(END, r)
        except Exception as e:
            print(e)

    def __fill_current_client(self):
        self.currentClient.nome = self.gui.txtNome.get()
        self.currentClient.sobrenome = self.gui.txtSobrenome.get()
        self.currentClient.email = self.gui.txtEmail.get()
        self.currentClient.cpf = self.gui.txtCPF.get()

    def search_command(self):
        "método para buscar registros"
        self.gui.listClientes.delete(0, END)
        self.__fill_current_client()
        try:
            rows = self.dao.search(self.currentClient)
            for r in rows:
                self.gui.listClientes.insert(END, r)
        except Exception as e:
            print(e)
    
    def insert_command(self):
        "método para inserir registros"
        self.__fill_current_client()
        self.dao.insert(self.currentClient)
        self.view_command()

    def get_selected_row(self, event):
        "método que seleciona na listbox e popula os campos de input"
        if self.gui.listClientes.curselection():
            index = self.gui.listClientes.curselection()[0]        
            self.selected = self.gui.listClientes.get(index)
            self.gui.entNome.delete(0, END)
            self.gui.entNome.insert(END, self.selected[1])
            self.gui.entSobrenome.delete(0, END)
            self.gui.entSobrenome.insert(END, self.selected[2])
            self.gui.entEmail.delete(0, END)
            self.gui.entEmail.insert(END, self.selected[3])
            self.gui.entCPF.delete(0, END)
            self.gui.entCPF.insert(END, self.selected[4])

    def update_command(self):
        "método para atualizar registro"
        id = self.selected[0]
        self.__fill_current_client()
        self.dao.update(id,self.currentClient)
        self.view_command()

    def del_command(self):
        "método para remover registro"
        id = self.selected[0]
        self.dao.delete(id)
        self.view_command()

    def close_command(self):
        self.dao.close()
        self.gui.window.destroy()


    def start(self):
        self.gui.listClientes.bind('<<ListboxSelect>>', self.get_selected_row)
        #associando o comportamento à interface
        self.gui.btnViewAll.configure(command=self.view_command)
        self.gui.btnBuscar.configure(command=self.search_command)
        self.gui.btnInserir.configure(command=self.insert_command)
        self.gui.btnUpdate.configure(command=self.update_command)
        self.gui.btnDel.configure(command=self.del_command)
        self.gui.btnClose.configure(command=self.close_command)
        self.gui.run()

Controller().start()