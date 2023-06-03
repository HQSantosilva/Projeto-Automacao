# -*- coding: utf-8 -*-
"""
Created on Fri Jun  2 20:09:33 2023

@author: riki4
"""
import PySimpleGUI as sg
from Controller import Controller
class Pesquisa:
    def __init__(self, controller):
        self.controller = controller
        self.layout = [
            [sg.Text('Título:'), sg.Input(key='-PESQUISA_TITULO-')],
            [sg.Button('Buscar'), sg.Button('Incluir'), sg.Button('Editar'), sg.Button('Excluir'), sg.Button('Visualizar')]
        ]

    def get_layout(self):
        return self.layout