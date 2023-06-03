# -*- coding: utf-8 -*-
"""
Created on Fri Jun  2 20:09:35 2023

@author: riki4
"""
import PySimpleGUI as sg
from Controller import Controller
class Cadastro:
    def __init__(self, controller):
        self.controller = controller
        self.layout = [
            [sg.Text('Título:'), sg.Input(key='-TITULO-')],
            [sg.Text('Comando:'), sg.Multiline(key='-COMANDO-', size=(30, 5))],
            [sg.Checkbox('Executa Print', key='-EXECUTAPRINT-')],
            [sg.Button('Executar'), sg.Button('Cancelar'), sg.Button('Salvar'), sg.Button('Organizar em Lista')]
        ]

    def get_layout(self):
        return self.layout
