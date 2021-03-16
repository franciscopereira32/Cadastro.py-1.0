#importando módulo do pymysql
import sqlite3

class Banco():

    def __init__(self):
        self.conexao = sqlite3.connect('banco.db')
        self.createTable()

    def createTable(self):
        c = self.conexao.cursor()

        c.execute("""create table if not exists versoes (
                    swversao integer primary key,
                    produto text,
                    hw text,
                    nb text,
                    fornecedor text)""")
        self.conexao.commit()
        c.close()
