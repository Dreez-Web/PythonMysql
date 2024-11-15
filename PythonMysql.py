import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

class FormularioClientes:
    
 def Formulario():
    try:
        base = Tk()
        base.geometry("1200x600")
        base.title("Formulario Python")
        
        groupbox = LabelFrame(base, text="Datos personales",padx=5,pady=5)
        groupbox.grid(row=0,column=0,padx=10,pady=10)
        
        labelId=Label(groupbox,text="Id:", width=13,font=("arial",12)).grid(row=0,column=0)
        textBoxId = Entry(groupbox)
        textBoxId.grid(row=0,column=1)
        
        labelNombres=Label(groupbox,text="Nombres:", width=13,font=("arial",12)).grid(row=1,column=0)
        textBoxNombres = Entry(groupbox)
        textBoxNombres.grid(row=1,column=1)
        
        labelApellidos=Label(groupbox,text="Apellidos:", width=13,font=("arial",12)).grid(row=2,column=0)
        textBoxApellidos = Entry(groupbox)
        textBoxApellidos.grid(row=2,column=1)
        
        labelSexo=Label(groupbox,text="Sexo:", width=13,font=("arial",12)).grid(row=3,column=0)
        seleccionSexo = tk.StringVar()
        combo = ttk.Combobox(groupbox, values=["Masculino","Femenino"],textvariable=seleccionSexo)
        combo.grid(row=3,column=1)
        seleccionSexo.set("Masculino")
        
        Button(groupbox,text="Guardar",width=10).grid(row=4,column=0)
        Button(groupbox,text="Modificar",width=10).grid(row=4,column=1)
        Button(groupbox,text="Eliminar",width=10).grid(row=4,column=2)
        
        base.mainloop()
                
    except ValueError as error:
            print("Error al mostrar la interfaz, error: {}".format(error))        


FormularioClientes.Formulario()