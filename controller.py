# -*- coding: utf-8 -*-
"""
Created on Sat May 27 13:02:06 2023

@author: riki4
"""
import pywinauto
from pywinauto import Desktop, Application
from pywinauto.keyboard import SendKeys
from Connection import Connection

class Controller:
    def __init__(self):
        self.Banco = Connection('server',
                                             'database',
                                             'username',
                                             'password')
    def IniciarConexao(self):
        self.Banco.Conectar()
    def EncerrarConexao(self):
        self.Banco.Desconectar()
    
    def AbrirComandos(self):
        return self.Banco.Listar
    
    def ExcluirComando(self,id):
        return self.Banco.ExcluirComando(id)    
        
    def LimparComandosAntigos(self):
        return self.Banco.LimparComandosAntigos()
    
    def EditarComando(self, id, titulo, comando, executaprint):
        return self.Banco.EditarComando(id, titulo, comando, executaprint)
    
    def IncluirComando(self, titulo, comando, executaprint):
        return self.Banco.IncluirComando(titulo, comando, executaprint)
    
#app = Application(backend="uia").start("notepad.exe")
#window = app.window(class_name="Notepad")
#window.Edit.type_keys("Hello, World!")
# button_salvar = window.child_window(title="Salvar", control_type="Button")
# button_salvar.click()
# edit_texto = window.child_window(class_name="Edit")
# edit_texto.type_keys("Texto a ser digitado")
# app.kill()