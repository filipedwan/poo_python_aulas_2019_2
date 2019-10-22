from tkinter import Tk, StringVar, Label, Entry, Listbox, Scrollbar, Button

class Gui():
    def __init__(self):
        '''Essa classe modela a interface gráfica
        da aplicação
        '''
        self.window = Tk()
        self.window.wm_title("Cadastro de Clientes")

        self.txtNome = StringVar()
        self.txtSobrenome = StringVar()
        self.txtEmail = StringVar()
        self.txtCPF = StringVar()

        self.lblnome = Label(self.window, text="Nome")
        self.lblsobrenome = Label(self.window, text="Sobrenome")
        self.lblemail = Label(self.window, text="Email")
        self.lblcpf = Label(self.window, text="CPF")

        self.entNome = Entry(self.window, textvariable=self.txtNome)
        self.entSobrenome = Entry(self.window, textvariable=self.txtSobrenome)
        self.entEmail = Entry(self.window, textvariable=self.txtEmail)
        self.entCPF = Entry(self.window, textvariable=self.txtCPF)

        self.listClientes = Listbox(self.window, width=45)
        self.scrollClientes = Scrollbar(self.window)

        self.btnViewAll = Button(self.window, text="Ver todos")
        self.btnBuscar = Button(self.window, text="Buscar")
        self.btnInserir = Button(self.window, text="Inserir")
        self.btnUpdate = Button(self.window, text="Atualizar Selecionados")
        self.btnDel = Button(self.window, text="Deletar Selecionados")
        self.btnClose = Button(self.window, text="Fechar")

    def configure_layout(self):
        "Configurando os itens na janela em grid"
        
        #Associando os objetos a grid da janela...
        self.lblnome.grid(row=0,column=0)
        self.lblsobrenome.grid(row=1,column=0)
        self.lblemail.grid(row=2,column=0)
        self.lblcpf.grid(row=3, column=0)
        #self.entNome.grid(row=0, column=1, padx=50, pady=50)
        self.entNome.grid(row=0, column=1)
        self.entSobrenome.grid(row=1, column=1)
        self.entEmail.grid(row=2, column=1)
        self.entCPF.grid(row=3, column=1)
        self.listClientes.grid(row=0, column=2, rowspan=10)#rowspan para fazer com que o objeto ocupe mais de uma linha.
        self.scrollClientes.grid(row=0, column=6, rowspan=10)
        self.btnViewAll.grid(row=4, column=0, columnspan=2)#columnspan para fazer com que o objeto ocupe mais de uma linha.
        self.btnBuscar.grid(row=5, column=0, columnspan=2)
        self.btnInserir.grid(row=6, column=0, columnspan=2)
        self.btnUpdate.grid(row=7, column=0, columnspan=2)
        self.btnDel.grid(row=8, column=0, columnspan=2)
        self.btnClose.grid(row=9, column=0, columnspan=2)

        #Associando a Scrollbar com a Listbox...
        self.listClientes.configure(yscrollcommand=self.scrollClientes.set)
        self.scrollClientes.configure(command=self.listClientes.yview)

    def configure_sizes(self):
        "definindo o tamanho dos elementos"
        x_pad = 5
        y_pad = 3
        width_entry = 30

        '''
        * Precisamos aplicar o padding para quase todos os 
        elementos, definir a largura dos botões e mais alguns
        pontos estéticos. Isso poderia ser feito manualmente,
        repetindo o código para todos os elementos. Todavia, 
        não vamos fazer assim.
        * Faremos a mudança de estilo da seguinte forma: Uma
        iteração por todos os elementos da janela, realizando
        as alterações conforme passamos pelos elementos.
        '''
        for child in self.window.winfo_children():
            widget_class = child.__class__.__name__
            if widget_class == "Button":
                child.grid_configure(sticky='WE', padx=x_pad, pady=y_pad)
            elif widget_class == "Listbox":
                child.grid_configure(padx=0, pady=0, sticky='NS')
            elif widget_class == "Scrollbar":
                child.grid_configure(padx=0, pady=0, sticky='NS')
            else:
                child.grid_configure(padx=x_pad, pady=y_pad, sticky='N')
        '''
        * padx e pady: Padding para o eixo X e Y do elemento. 
        É referente ao espaço entre a borda deste elemento e 
        a borda dos outros elementos da janela;
        * sticky: Indica em qual ponto da janela (norte – N, 
        sul – S, leste – E ou oeste W) o objeto estará ancorado. 
        Se você combinar o ponto leste e oeste (EW), o elemento 
        ocupará todo o espaço horizontal da coluna em que está 
        localizado. O mesmo ocorre se colocarmos NS (norte-sul), 
        o elemento ocupará todo o espaço vertical.
        * Para o ListBox e o ScrollBar, vamos definir padding zero 
        para que eles fiquem colados, parecendo que são apenas um elemento.
        '''

    def run(self):
        self.configure_layout()
        self.configure_sizes()
        self.window.mainloop()
