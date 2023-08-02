# GUI - Graphical User Interface
# Tkinter - TK Interface
# importamos el módulo de tkinter
import tkinter as tk
# Importamos el módulo del tema de tkinter (componentes)
from tkinter import ttk

# Creamos un objeto usando la clase Tk
ventana = tk.Tk()
# Modificamos el tamaño de la ventana en (pixeles)
ventana.geometry('600x400')
# Cambiamos el nombre de la ventana
ventana.title('Nueva Ventana')
# Configuramos el icono de la aplicación
ventana.iconbitmap('icono.ico')
# Creamos un método evento_click (al dar click al botón 1 ejecuta esto)
def evento_click():
    # Cambiamos texto del botón
    boton1.config(text='Botón presionado')
    print('Ejecución del evento_click')
    # Creamos un nuevo botón
    boton2 = ttk.Button(ventana, text='Nuevo botón')
    boton2.pack()
# Creamos un botón (componente/widget), el objeto padre es la ventana
boton1 = ttk.Button(ventana, text = 'Dar click', command= evento_click)
# Pack layout manager para mostrar el botón de la ventana
boton1.pack()
# Iniciamos la ventana (esta línea la ejecutamos al final)
# Si la ejecutamos antes, no se van a mostrar los cambios
ventana.mainloop()


