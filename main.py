# -*- coding: utf-8 -*-
"""
Created on Sat May 27 13:00:05 2023

@author: riki4
"""
import PySimpleGUI as sg
from Controller import Controller
from Pesquisa import Pesquisa
from Cadastro import Cadastro

class Main:
#O(1)
    def __init__(self, controller):
        self.controller = controller
        self.layout = [
            [sg.TabGroup([
                [sg.Tab('Pesquisa', Pesquisa(self.controller).get_layout(), key='-PESQUISA_TAB-')],
                [sg.Tab('Cadastro', Cadastro(self.controller).get_layout(), key='-CADASTRO_TAB-')]
            ])]
        ]
        self.janela = sg.Window('Minha Aplicação', self.layout)
        
 #O(1)
    def executar(self):
        while True:
            event, values = self.janela.read()
            if event == sg.WINDOW_CLOSED:
                break
            elif event == 'Buscar':
                titulo = values['-PESQUISA_TITULO-']
                comandos = self.controller.ConsultarPorTitulo(titulo)

            elif event == 'Incluir':
                self.janela['-PESQUISA_TAB-'].select()

            elif event == 'Editar':
                self.janela['-CADASTRO_TAB-'].select()

            elif event == 'Excluir':
                id = values['-ID-']
                self.controller.ExcluirComando(id)

            elif event == 'Visualizar':
                pass
            
control = Controller()
control.IniciarConexao()
app = Main(control)
app.executar()
        
