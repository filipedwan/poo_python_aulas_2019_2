class Client:
    def __init__(self, nome="", sobrenome="", email="", cpf=""):
        self.nome = nome
        self.sobrenome = sobrenome
        self.email = email
        self.cpf = cpf
    def __str__(self):
        print(self.nome, self.sobrenome, self.email, self.cpf)