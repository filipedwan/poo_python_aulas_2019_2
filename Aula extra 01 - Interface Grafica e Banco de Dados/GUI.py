from tkinter import *

class Gui():
    '''Essa classe modela a interface gráfica
    da aplicação
    '''
    window = Tk()
    window.wm_title("Cadastro de Clientes")

    txtNome = StringVar()
    txtSobrenome = StringVar()
    txtEmail = StringVar()
    txtCPF = StringVar()

    lblnome = Label(window, text="Nome")
    lblsobrenome = Label(window, text="Sobrenome")
    lblemail = Label(window, text="Email")
    lblcpf = Label(window, text="CPF")

    entNome = Entry(window, textvariable=txtNome)
    entSobrenome = Entry(window, textvariable=txtSobrenome)
    entEmail = Entry(window, textvariable=txtEmail)
    entCPF = Entry(window, textvariable=txtCPF)

    listClientes = Listbox(window)
    scrollClientes = Scrollbar(window)

    btnViewAll = Button(window, text="Ver todos")
    btnBuscar = Button(window, text="Buscar")
    btnInserir = Button(window, text="Inserir")
    btnUpdate = Button(window, text="Atualizar Selecionados")
    btnDel = Button(window, text="Deletar Selecionados")
    btnClose = Button(window, text="Fechar")

    #Associando os objetos a grid da janela...
    lblnome.grid(row=0,column=0)
    lblsobrenome.grid(row=1,column=0)
    lblemail.grid(row=2,column=0)
    lblcpf.grid(row=3, column=0)
    entNome.grid(row=0, column=1, padx=50, pady=50)
    entSobrenome.grid(row=1, column=1)
    entEmail.grid(row=2, column=1)
    entCPF.grid(row=3, column=1)
    listClientes.grid(row=0, column=2, rowspan=10)#rowspan para fazer com que o objeto ocupe mais de uma linha.
    scrollClientes.grid(row=0, column=6, rowspan=10)
    btnViewAll.grid(row=4, column=0, columnspan=2)#columnspan para fazer com que o objeto ocupe mais de uma linha.
    btnBuscar.grid(row=5, column=0, columnspan=2)
    btnInserir.grid(row=6, column=0, columnspan=2)
    btnUpdate.grid(row=7, column=0, columnspan=2)
    btnDel.grid(row=8, column=0, columnspan=2)
    btnClose.grid(row=9, column=0, columnspan=2)

    #Associando a Scrollbar com a Listbox...
    listClientes.configure(yscrollcommand=scrollClientes.set)
    scrollClientes.configure(command=listClientes.yview)

    #definindo o tamanho dos elementos
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
    for child in window.winfo_children():
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
        Gui.window.mainloop()
