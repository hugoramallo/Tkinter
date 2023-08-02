import tkinter as tk
from tkinter import ttk
# Creamos ventana
ventana = tk.Tk()
# Tamaño ventana
ventana.geometry('600x400')
# Título ventana
ventana.title('Manejo de Grid')
# Icono
ventana.iconbitmap('icono.ico')

# Configurar el grid (usamos proporciones para lo que ocupa el espacio 1, 5)
ventana.rowconfigure(0, weight=1) #primera fila
ventana.rowconfigure(1, weight=10)
ventana.columnconfigure(0, weight=2)
ventana.columnconfigure(1, weight=10)


#Métodos de los eventos
def evento1():
    boton1.config(text='Botón 1 presionado')
def evento2():
    boton2.config(text='Botón 2 presionado')

def evento4():
    # fg cambia el color de la fuente, relief cambia el relieve
    boton4.config(text='Botón 4 presionado', fg='blue', relief=tk.GROOVE)

# Definimos dos botones
boton1 = tk.Button(ventana, text='Botón 1', command=evento1)
#boton1.pack()
# Método grid (sticky = posición, padx/pady = padding)
boton1.grid(row=0, column=0, sticky='NSWE', padx=40, pady=30, columnspan=2, rowspan=2)
# N(arriba), E(derecha), S(abajo), W(izquierda), por defecto es el centro
boton2 = tk.Button(ventana, text='Botón 2', command=evento2)
# botón se posiciona en la izquierda
boton2.grid(row=1, column=0, sticky='NSWE') # NSWE se expande todo el espacio que tenga disponible
# Método mainloop recibe todos los eventos y permite mostrar ventana


boton3 = tk.Button(ventana, text='Botón 3', command=evento2)
boton3.grid(row=0, column=1, sticky='NSWE') # NSWE se expande todo el espacio que tenga disponible

boton4 = tk.Button(ventana, text='Botón 4', command=evento4)
boton4.grid(row=1, column=1, sticky='NSWE') # NSWE se expande todo el espacio que tenga disponible

ventana.mainloop()


