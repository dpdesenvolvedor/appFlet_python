import flet as ft

def main(page: ft.Page):
  #  page.bgcolor = 'green'
   # page.bgcolor = '#B12B12'
    page.bgcolor = ft.Colors.AMBER_200


    page.update()

ft.app(target= main)