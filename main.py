# -*- coding: utf-8 -*-
"""
Created on Sat May 27 13:00:05 2023

@author: riki4
"""
import PySimpleGUI as sg
import controller.py as controller
import connection.py
import Pesquisa.py
import Cadastro.py

class Main:
    def __init__(self):
        self.layout = [
            [sg.TabGroup([
                [sg.Tab('Pesquisa', Pesquisa().get_layout(), key='-PESQUISA_TAB-')],
                [sg.Tab('Cadastro', Cadastro().get_layout(), key='-CADASTRO_TAB-')]
            ])]
        ]
        self.janela = sg.Window('Minha Aplicação', self.layout)

    def run(self):
        while True:
            event, values = self.janela.read()
            if event == sg.WINDOW_CLOSED:
                break
            elif event == 'Pesquisar':
                termo_pesquisa = values['-PESQUISA-']
                sg.popup(f'Pesquisando por: {termo_pesquisa}')
            elif event == 'Incluir':
                self.janela['-PESQUISA_TAB-'].select()  
            elif event == 'Cadastrar':
                nome = values['-TITULO-']
                sg.popup(f'Cadastrando: {titulo} ')

        self.janela.close()

app = Main()
app.run()
        
