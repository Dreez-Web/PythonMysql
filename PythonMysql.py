import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from Clientes import *
from Conexion import *

class FormularioClientes:
    
     global base 
     base = None
     
     global groupbox
     groupbox = None
     
     global textBoxId
     textBoxId = None
     
     global textBoxNombres
     textBoxNombres = None
     
     global textBoxApellidos
     textBoxApellidos= None
     
     global combo 
     combo = None
     
     global tree 
     tree = None
    
def Formulario():
        
     global base 
     global groupbox
     global textBoxId
     global textBoxNombres
     global textBoxApellidos
     global combo
     global tree 
        
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
            
            Button(groupbox,text="Guardar",width=10,command=guardarRegistros).grid(row=4,column=0)
            Button(groupbox,text="Modificar",width=10,command=modificarRegistros).grid(row=4,column=1)
            Button(groupbox,text="Eliminar",width=10).grid(row=4,column=2)
            
            
            groupbox = LabelFrame(base,text="Lista del personal",padx=5,pady=5)
            groupbox.grid(row=0,column=1,padx=5,pady=5)
            
            tree = ttk.Treeview(groupbox,columns=("Id","Nombres","Apellidos","Sexo"),show='headings',height=5,)
            tree.column("# 1",anchor=CENTER)
            tree.heading("# 1", text="Id")
            tree.column("# 2",anchor=CENTER)
            tree.heading("# 2", text="Nombres")
            tree.column("# 3",anchor=CENTER)
            tree.heading("# 3", text="Apellidos")
            tree.column("# 4",anchor=CENTER)
            tree.heading("# 4", text="Sexo")
            
            #agregar los datos a la tabla
            #mostrar tabla

            for row in CClientes.mostrarClientes():
                  tree.insert("","end",values=row)

            tree.bind("<<TreeviewSelect>>",seleccionarRegistro)
            
            tree.pack()
             
            base.mainloop()
                    
     except ValueError as error:
                print("Error al mostrar la interfaz, error: {}".format(error))        



def guardarRegistros():
    
    global textBoxNombres, textBoxApellidos, combo, groupbox
    
    try:
        #verificar si los widgets estan inicializados
        if textBoxNombres is None or textBoxApellidos is None or combo is None:
            print("Los widgets no estan inicializados")
            
        nombres = textBoxNombres.get()
        apellidos = textBoxApellidos.get()
        sexo = combo.get()
        
        CClientes.ingresarclientes(nombres, apellidos, sexo)
        messagebox.showinfo("Informacion","Los datos fueron guardados")
        
        actualizarTreeView()

        #limpiamos los campos
        
        textBoxNombres.delete(0,END)
        textBoxApellidos.delete(0,END)
    except ValueError as error:
        print("Error al ingresar los datos{}".format(error))



def actualizarTreeView():
      global tree

      try:
            #Borrar todos los elementos actuales del TreeView
            tree.delete(*tree.get_children())  

            #Obtener nuevos datos que queremos mostrar
            datos = CClientes.mostrarClientes()

            #insertar datos en el tree
            for row in CClientes.mostrarClientes():
                  tree.insert("","end",values=row)
      except ValueError as error:
            print("Error al actualizar tabla{}".format(error))  



def seleccionarRegistro(event):
    try:
          #obner id de elemento seleccionado
        itemSeleccionado = tree.focus()

        if itemSeleccionado:
             values = tree.item(itemSeleccionado)['values']

             textBoxId.delete(0,END)
             textBoxId.insert(0,values[0])
             textBoxNombres.delete(0,END)
             textBoxNombres.insert(0,values[1])
             textBoxApellidos.delete(0,END)
             textBoxApellidos.insert(0,values[2])
             combo.set(values[3])
    except ValueError as error:
         print("Error al seleccionar registro{}".format(error))

def modificarRegistros():
    
    global textBoxId,textBoxNombres, textBoxApellidos, combo, groupbox
    
    try:
        #verificar si los widgets estan inicializados
        if textBoxId is NONE or textBoxNombres is None or textBoxApellidos is None or combo is None:
            print("Los widgets no estan inicializados")
            return
        idUsuario = textBoxId.get()
        nombres = textBoxNombres.get()
        apellidos = textBoxApellidos.get()
        sexo = combo.get()
        
        CClientes.modificarClientes(idUsuario,nombres, apellidos, sexo)
        messagebox.showinfo("Informacion","Los datos fueron guardados")
        
        actualizarTreeView()

        #limpiamos los campos
        textBoxId.delete(0,END)
        textBoxNombres.delete(0,END)
        textBoxApellidos.delete(0,END)
    except ValueError as error:
        print("Error al ingresar los datos{}".format(error))         
Formulario() 

