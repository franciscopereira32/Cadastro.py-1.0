from Versoes import Versoes
from tkinter import *

class Application:
    def __init__(self, master=None):
        self.fonte = ("Verdana", "8")

        self.container1 = Frame(master)
        self.container1["pady"] = 10
        self.container1.pack()
        self.container2 = Frame(master)
        self.container2["padx"] = 20
        self.container2["pady"] = 5
        self.container2.pack()
        self.container3 = Frame(master)
        self.container3["padx"] = 20
        self.container3["pady"] = 5
        self.container3.pack()
        self.container4 = Frame(master)
        self.container4["padx"] = 20
        self.container4["pady"] = 5
        self.container4.pack()
        self.container5 = Frame(master)
        self.container5["padx"] = 20
        self.container5["pady"] = 5
        self.container5.pack()
        self.container6 = Frame(master)
        self.container6["padx"] = 20
        self.container6["pady"] = 5
        self.container6.pack()
        #self.container7 = Frame(master)
        #self.container7["padx"] = 20
        #self.container7["pady"] = 5
        #self.container7.pack()
        self.container8 = Frame(master)
        self.container8["padx"] = 20
        self.container8["pady"] = 10
        self.container8.pack()
        self.container9 = Frame(master)
        self.container9["pady"] = 15
        self.container9.pack()

        self.titulo = Label(self.container1, text="Informe os dados da versão:")
        self.titulo["font"] = ("Calibri", "9", "bold")
        self.titulo.pack ()

        self.lblswversao = Label(self.container2,
        text="swversao:", font=self.fonte, width=10)
        self.lblswversao.pack(side=LEFT)

        self.txtswversao = Entry(self.container2)
        self.txtswversao["width"] = 10
        self.txtswversao["font"] = self.fonte
        self.txtswversao.pack(side=LEFT)

        self.btnBuscar = Button(self.container2, text="Buscar",
        font=self.fonte, width=10)
        self.btnBuscar["command"] = self.buscarVersoes
        self.btnBuscar.pack(side=RIGHT)

        self.lblproduto = Label(self.container3, text="Produto:",
        font=self.fonte, width=10)
        self.lblproduto.pack(side=LEFT)

        self.txtproduto = Entry(self.container3)
        self.txtproduto["width"] = 25
        self.txtproduto["font"] = self.fonte
        self.txtproduto.pack(side=LEFT)

        self.lblhw = Label(self.container4, text="Hardware:",
        font=self.fonte, width=10)
        self.lblhw.pack(side=LEFT)

        self.txthw = Entry(self.container4)
        self.txthw["width"] = 25
        self.txthw["font"] = self.fonte
        self.txthw.pack(side=LEFT)

        self.lblnb= Label(self.container5, text="Código NB:",
        font=self.fonte, width=10)
        self.lblnb.pack(side=LEFT)

        self.txtnb = Entry(self.container5)
        self.txtnb["width"] = 25
        self.txtnb["font"] = self.fonte
        self.txtnb.pack(side=LEFT)

        self.lblfornecedor= Label(self.container6, text="Fonecedor:",
        font=self.fonte, width=10)
        self.lblfornecedor.pack(side=LEFT)

        self.txtfornecedor = Entry(self.container6)
        self.txtfornecedor["width"] = 25
        self.txtfornecedor["font"] = self.fonte
        self.txtfornecedor.pack(side=LEFT)

        self.bntInsert = Button(self.container8, text="Inserir",
        font=self.fonte, width=12)
        self.bntInsert["command"] = self.inserirVersoes
        self.bntInsert.pack (side=LEFT)

        self.bntAlterar = Button(self.container8, text="Alterar",
        font=self.fonte, width=12)
        self.bntAlterar["command"] = self.alterarVersoes
        self.bntAlterar.pack (side=LEFT)

        self.bntExcluir = Button(self.container8, text="Excluir",
        font=self.fonte, width=12)
        self.bntExcluir["command"] = self.excluirVersoes
        self.bntExcluir.pack(side=LEFT)

        self.lblmsg = Label(self.container9, text="")
        self.lblmsg["font"] = ("Verdana", "9", "italic")
        self.lblmsg.pack()


    def inserirVersoes(self):
        versao = Versoes()

        versao.swversao = self.txtswversao.get()
        versao.produto = self.txtproduto.get()
        versao.hw = self.txthw.get()
        versao.nb = self.txtnb.get()
        versao.fornecedor = self.txtfornecedor.get()

        self.lblmsg["text"] = versao.inserirVersoes()

        self.txtswversao.delete(0, END)
        self.txtproduto.delete(0, END)
        self.txthw.delete(0, END)
        self.txtnb.delete(0, END)
        self.txtfornecedor.delete(0, END)
        #self.txtsenha.delete(0, END)



    def alterarVersoes(self):
        versao = Versao()

        versao.idswversao = self.txtswversao.get()
        versao.produto = self.txtproduto.get()
        versao.hw = self.txthw.get()
        versao.nb = self.txtnb.get()
        versao.fornecedor = self.txtfornecedor.get()
        #versaoo.senha = self.txtsenha.get()

        self.lblmsg["text"] = versao.updateVersaoes()

        self.txtswversao.delete(0, END)
        self.txtproduto.delete(0, END)
        self.txthw.delete(0, END)
        self.txtnb.delete(0, END)
        self.txtfornecedor.delete(0, END)
        #self.txtsenha.delete(0, END)



    def excluirVersoes(self):
        versao = Versoes()

        versao.swversao = self.txtswversao.get()

        self.lblmsg["text"] = versao.deleteVersoes()

        self.txtswversao.delete(0, END)
        self.txtproduto.delete(0, END)
        self.txthw.delete(0, END)
        self.txtnb.delete(0, END)
        self.txtfornecedor.delete(0, END)
        #self.txtsenha.delete(0, END)


    def buscarVersoes(self):
        versao = Versoes()

        swversao = self.txtswversao.get()

        self.lblmsg["text"] = versao.buscarVersoes(swversao)

        self.txtswversao.delete(0, END)
        self.txtswversao.insert(INSERT, versao.swversao)

        self.txtproduto.delete(0, END)
        self.txtproduto.insert(INSERT, versao.produto)

        self.txthw.delete(0, END)
        self.txthw.insert(INSERT,versao.hw)

        self.txtnb.delete(0, END)
        self.txtnb.insert(INSERT, versao.nb)

        self.txtfornecedor.delete(0, END)
        self.txtfornecedor.insert(INSERT,versao.fornecedor)

        #self.txtsenha.delete(0, END)
        #self.txtsenha.insert(INSERT,user.senha)


root = Tk()
Application(root)
root.mainloop()
