# -*- coding: utf-8 -*-
"""
Created on Fri Jun  2 20:09:35 2023

@author: riki4
"""
import PySimpleGUI as sg
import controller.py as controller
class Cadastro:
    def __init__(self):
        self.layout = [
            [sg.Text('Título'), sg.Input(key='-TITULO-')],
            [sg.Button('Cadastrar')]
        ]

    def get_layout(self):
        return self.layout
