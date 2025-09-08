import flet as ft

def main(page: ft.Page):
    mensagem = ft.Text(value='ola mundo')
    page.add(mensagem)

    page.add(ft.Text(value='Meu nome e Denis'))
    page.add(ft.Text(value='texto 1'), ft.Text(value='Texto 2'))

    elementos = [
        ft.Text(value='Produto 1'),
        ft.Text(value='Produto 2'),
        ft.Text(value='Produto 3'),
        ft.Text(value='Produto 4'),
        ft.Text(value='Produto 5'),
        ft.Text(value='Produto 6')

    ]

    page.add(*elementos)




    


ft.app(target= main)
