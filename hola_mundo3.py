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

# Entrada de texto de 30 caracteres, width(cantidad caracteres que ocupa la caja)
# show = caracter que se va a mostrar(ejemplo * en passwrod), pero aunque se vea se captura el texto que escribimos
# state = tk.DISABLED desactiva la caja de texto
entrada1 = ttk.Entry(ventana, width=30, justify=tk.CENTER, state=tk.NORMAL)
entrada1.grid(row=0, column=0)

#insert agrega un texto ( 0 o 5 es el índice en la cadena)
entrada1.insert(0,'Introduce una cadena')
entrada1.insert(tk.END,'.')
# una vez agregada la info se puede poner como solo lectura, siempre al final si lo queremos
#entrada1.config(state='readonly')
#método enviar
def enviar():
    #imprimimos lo que hemos escrito en el cajetín del texto
    print(entrada1.get())
    # Modificamos texto del botón
    boton1.config(text=entrada1.get())
    # Eliminar el contenido
    #entrada1.delete(0, tk.END)
    # Seleccionar texto de la caja
    entrada1.select_range(0, tk.END)
    # Para hacer efectiva la selección del texto
    entrada1.focus()

# Creamos un botón (componente, texto, evento)
boton1= ttk.Button(ventana, text='Enviar', command=enviar)
boton1.grid(row=0, column=1)
ventana.mainloop()
