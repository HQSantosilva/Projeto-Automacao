# -*- coding: utf-8 -*-
"""
Created on Fri Jun  2 20:09:33 2023

@author: riki4
"""
import PySimpleGUI as sg
import controller.py as controller
class Pesquisa:
    def __init__(self):
        self.layout = [
            [sg.Text('Digite um termo de pesquisa:')],
            [sg.Input(key='-PESQUISA-')],
            [sg.Button('Pesquisar')],
            [sg.Button('Incluir')]
        ]

    def get_layout(self):
        return self.layout