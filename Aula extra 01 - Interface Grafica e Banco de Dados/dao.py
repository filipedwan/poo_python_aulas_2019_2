import sqlite3 as sql
 
'''
* Para esta aplicação, precisamos apenas de uma tabela 
(que se chamará clientes), com os seguintes campos:
    * Id
    * Nome
    * Sobrenome
    * Email
    * CPF
'''

class BdAccess():
    database    = "clientes.db"
    conn        = None
    cur         = None
    connected   = False
 
    def connect(self):
        "realiza conexão com o banco de dados"
        try:
            BdAccess.conn = sql.connect(BdAccess.database)
            BdAccess.cur = BdAccess.conn.cursor()
            BdAccess.connected = True
            self.execute("CREATE TABLE IF NOT EXISTS clientes (id INTEGER PRIMARY KEY , nome TEXT, sobrenome TEXT, email TEXT, cpf TEXT)")
        except sqlite3.Error as error:
            print("Erro no banco de dados: ", error)
 
    def disconnect(self):
        " fecha a conexão com o banco de dados"
        BdAccess.conn.close()
        BdAccess.connected = False
 
    def execute(self, sql, parms = None):
        '''
        executa um comando no banco de dados. recebe três parâmetros:
        * self: referencia para o próprio objeto. não precisa ser informado;
        * sql: comando SQL a ser executado;
        * parms: vetor com os parâmetros do comando SQL. Pode ser omitido.
        '''
        if BdAccess.connected:
            if parms == None:
                BdAccess.cur.execute(sql)
            else:
                BdAccess.cur.execute(sql, parms)
            return True
        else:
            return False
 
    def fetchall(self):
        "recupera os valores recebidos de um comando select."
        return BdAccess.cur.fetchall()
 
    def persist(self):
        "realiza o commit das operações realizadas."
        if BdAccess.connected:
            BdAccess.conn.commit()
            return True
        else:
            return False

class ClientDAO:
    def __init__(self):
        "Quando a aplicação for executada pela primeira vez, cria-se o banco de dados"
        self.bd = BdAccess()
        self.bd.connect()
        self.bd.persist()

    def view(self):
        "recupera todos os dados do banco."
        rows = None
        try:
            self.bd.execute("SELECT * FROM clientes")    
            rows = self.bd.fetchall()
        except sql.Error as error:
            print("Falha ao tentar selecionar os registros")
            print("Classe da exceção: ", error.__class__)
            print("Exceção é ", error.args)
            raise sql.Error()
        return rows

    def insert(self, cliente):
        "insere novos registros no banco"
        try:
            self.bd.execute("INSERT INTO clientes VALUES(NULL, ?,?,?,?)", (cliente.nome, cliente.sobrenome, cliente.email, cliente.cpf))
            self.bd.persist()
        except sqlite3.Error as error:
            print("Falha ao tentar inserir os registros")
            print("Classe da exceção: ", error.__class__)
            print("Exceção é ", error.args)

    def search(self, cliente):
        '''
        A função de busca utiliza o operador OR e todos os campos 
        que não forem preenchidos pelo usuário na hora da busca serão 
        considerados como strings vazias
        '''
        rows = None
        try:
            self.bd.execute("SELECT * FROM clientes WHERE nome=? or sobrenome=? or email=? or cpf=?", (cliente.nome, cliente.sobrenome, cliente.email, cliente.cpf))
            rows = self.bd.fetchall()
        except sqlite3.Error as error:
            print("Falha ao tentar buscar os registros")
            print("Classe da exceção: ", error.__class__)
            print("Exceção é ", error.args)
            raise Exception
        return rows

    def update(self, id, cliente):
        "atualiza registros no banco"
        try:
            self.bd.execute("UPDATE clientes SET nome =?, sobrenome=?, email=?, cpf=? WHERE id = ?",(cliente.nome, cliente.sobrenome, cliente.email, cliente.cpf, id))
            self.bd.persist()
        except sqlite3.Error as error:
            print("Falha ao tentar atualizar os registros")
            print("Classe da exceção: ", error.__class__)
            print("Exceção é ", error.args)
    
    def delete(self, id):
        "remove registros no banco"
        try:
            self.bd.execute("DELETE FROM clientes WHERE id = ?", (id,))
            self.bd.persist()
        except sqlite3.Error as error:
            print("Falha ao tentar remover o registro")
            print("Classe da exceção: ", error.__class__)
            print("Exceção é ", error.args)

    def close(self):
        "fechar o banco"
        print('Fechando o Banco...')
        self.bd.disconnect()