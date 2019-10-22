import sqlite3 as sql
database = "clientes.db"
 
'''
* Para esta aplicação, precisamos apenas de uma tabela 
(que se chamará clientes), com os seguintes campos:
    * Id
    * Nome
    * Sobrenome
    * Email
    * CPF
'''

#conn = sql.connect(database)
#cur = conn.cursor()
#cur.execute("CREATE TABLE IF NOT EXISTS cliente (id INTEGER PRIMARY KEY , nome TEXT, sobrenome TEXT, email TEXT, cpf TEXT)")
#conn.commit()
#conn.close()


class TransactionObject():
    database    = "clientes.db"
    conn        = None
    cur         = None
    connected   = False
 
    def connect(self):
        "realiza conexão com o banco de dados"
        TransactionObject.conn = sql.connect(TransactionObject.database)
        TransactionObject.cur = TransactionObject.conn.cursor()
        TransactionObject.connected = True
 
    def disconnect(self):
        " fecha a conexão com o banco de dados"
        TransactionObject.conn.close()
        TransactionObject.connected = False
 
    def execute(self, sql, parms = None):
        '''
        executa um comando no banco de dados. recebe três parâmetros:
        * self: referencia para o próprio objeto. não precisa ser informado;
        * sql: comando SQL a ser executado;
        * parms: vetor com os parâmetros do comando SQL. Pode ser omitido.
        '''
        if TransactionObject.connected:
            if parms == None:
                TransactionObject.cur.execute(sql)
            else:
                TransactionObject.cur.execute(sql, parms)
            return True
        else:
            return False
 
    def fetchall(self):
        "recupera os valores recebidos de um comando select."
        return TransactionObject.cur.fetchall()
 
    def persist(self):
        "realiza o commit das operações realizadas."
        if TransactionObject.connected:
            TransactionObject.conn.commit()
            return True
        else:
            return False

class ClienteDao:
    def __init__(self):
        "Quando a aplicação for executada pela primeira vez, cria-se o banco de dados"
        self.trans = TransactionObject()
        self.trans.connect()
        self.trans.execute("CREATE TABLE IF NOT EXISTS clientes (id INTEGER PRIMARY KEY , nome TEXT, sobrenome TEXT, email TEXT, cpf TEXT)")
        self.trans.persist()

    def view(self):
        "recupera todos os dados do banco."
        self.trans.execute("SELECT * FROM clientes")    
        rows = self.trans.fetchall()
        return rows

    def insert(self, nome, sobrenome, email, cpf):
        "insere novos registros no banco"
        self.trans.execute("INSERT INTO clientes VALUES(NULL, ?,?,?,?)", (nome, sobrenome, email, cpf))
        self.trans.persist()

    def search(self, nome="", sobrenome="", email="", cpf=""):
        '''
        A função de busca utiliza o operador OR e todos os campos 
        que não forem preenchidos pelo usuário na hora da busca serão 
        considerados como strings vazias
        '''
        trans.execute("SELECT * FROM clientes WHERE nome=? or sobrenome=? or email=? or cpf=?", (nome,sobrenome,email, cpf))
        rows = trans.fetchall()
        return rows

    def update(self, id, nome, sobrenome, email, cpf):
        "atualiza registros no banco"
        self.trans.execute("UPDATE clientes SET nome =?, sobrenome=?, email=?, cpf=? WHERE id = ?",(nome, sobrenome,email, cpf, id))
        self.trans.persist()
    
    def delete(self, id):
        "remove registros no banco"
        self.trans.execute("DELETE FROM clientes WHERE id = ?", (id,))
        self.trans.persist()

    def close(self):
        "fechar o banco"
        print('Fechando o Banco...')
        self.trans.disconnect()