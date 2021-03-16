from Banco import Banco

class Versoes(object):


    def __init__(self, swversao = "", produto = "", hw = "",
    nb = "", fornecedor = ""):
      self.info = {}
      self.swversao = swversao
      self.produto= produto
      self.hw = hw
      self.nb = nb
      self.fornecedor = fornecedor


    def inserirVersoes(self):

      banco = Banco()
      try:

          c = banco.conexao.cursor()

          c.execute("insert into versoes (swversao, produto, hw, nb, fornecedor) values ('" + self.swversao + "','" + self.produto + "','" + self.hw + "', '" + self.nb + "', '" + self.fornecedor + "')")

          banco.conexao.commit()
          c.close()

          return "Versão cadastrada com sucesso!"
      except:
          return "Ocorreu um erro na inserção da Versão"

    def updateVersaoes(self):

      banco = Banco()
      try:

          c = banco.conexao.cursor()

          c.execute("update versoes set produto = '" + self.produto + "', hw = '" + self.hw +
          "', nb = '" + self.nb + "', fornecedor = '" + self.fornecedor +
          "' where swversao = " + self.swversao + " ")

          banco.conexao.commit()
          c.close()

          return "Versão atualizada com sucesso!"
      except:
          return "Ocorreu um erro na alteração da versão"

    def deleteVersoes(self):

      banco = Banco()
      try:

          c = banco.conexao.cursor()

          c.execute("delete from versoes where swversao = " + self.swversao + " ")

          banco.conexao.commit()
          c.close()

          return "Versão excluída com sucesso!"
      except:
          return "Ocorreu um erro na exclusão da versão"

    def buscarVersoes(self, swversao):
      banco = Banco()
      try:

          c = banco.conexao.cursor()

          c.execute("select * from versoes where swversao = " + swversao + "  ")

          for linha in c:
              self.swversao = linha[0]
              self.produto = linha[1]
              self.hw = linha[2]
              self.nb = linha[3]
              self.fornecedor = linha[4]

          c.close()

          return "Busca feita com sucesso!"
      except:
          return "Ocorreu um erro na busca da versão"
