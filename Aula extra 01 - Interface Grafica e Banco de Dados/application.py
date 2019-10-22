from GUI import Gui
from dao import ClienteDao
from tkinter import END

'''
Adaptado de:
http://raccoon.ninja/pt/dev-pt/tutorial-aplicacao-em-python-sqlite-parte-01/
https://raccoon.ninja/pt/dev-pt/tutorial-aplicacao-em-python-sqlite-parte-02/
http://raccoon.ninja/pt/dev-pt/tutorial-aplicacao-em-python-sqlite-parte-03/
http://raccoon.ninja/pt/dev-pt/tutorial-aplicacao-em-python-sqlite-parte-04/
'''

class Controller:
    def __init__(self):
        self.app = Gui()
        self.dao = ClienteDao()
    
    def view_command(self):
        "método para visualização dos resultados"
        rows = self.dao.view()
        self.app.listClientes.delete(0, END)
        for r in rows:
            self.app.listClientes.insert(END, r)

    def search_command(self):
        "método para buscar registros"
        self.app.listClientes.delete(0, END)
        rows = self.dao.search(self.app.txtNome.get(), self.app.txtSobrenome.get(), self.app.txtEmail.get(), self.app.txtCPF.get())
        for r in rows:
            self.app.listClientes.insert(END, r)
    
    def insert_command(self):
        "método para inserir registros"
        self.dao.insert(self.app.txtNome.get(), self.app.txtSobrenome.get(), self.app.txtEmail.get(), self.app.txtCPF.get())
        self.view_command()

    def getSelectedRow(self, event):
        "método que seleciona na listbox e popukla os campos de input"
        global selected
        index = self.app.listClientes.curselection()[0]
        selected = self.app.listClientes.get(index)
        self.app.entNome.delete(0, END)
        self.app.entNome.insert(END, selected[1])
        self.app.entSobrenome.delete(0, END)
        self.app.entSobrenome.insert(END, selected[2])
        self.app.entEmail.delete(0, END)
        self.app.entEmail.insert(END, selected[3])
        self.app.entCPF.delete(0, END)
        self.app.entCPF.insert(END, selected[4])

    def update_command(self):
        "método para atualizar registro"
        self.dao.update(selected[0],self.app.txtNome.get(),self.app.txtSobrenome.get(),self.app.txtEmail.get(), self.app.txtCPF.get())
        self.view_command()

    def del_command(self):
        "método para remover registro"
        id = selected[0]
        self.dao.delete(id)
        self.view_command()

    def close_command(self):
        self.dao.close()
        self.app.window.destroy()


    def start(self):
        self.app.listClientes.bind('<<ListboxSelect>>', self.getSelectedRow)
        #associando o comportamento à interface
        self.app.btnViewAll.configure(command=self.view_command)
        self.app.btnBuscar.configure(command=self.search_command)
        self.app.btnInserir.configure(command=self.insert_command)
        self.app.btnUpdate.configure(command=self.update_command)
        self.app.btnDel.configure(command=self.del_command)
        #self.app.btnClose.configure(command=self.app.window.destroy)
        self.app.btnClose.configure(command=self.close_command)
        self.app.run()

Controller().start()