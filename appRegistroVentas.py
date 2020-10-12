from tkinter import *
from tkinter import messagebox
from io import open



ventana = Tk()
ventana.title("Registros Ventas")
ventana.geometry("500x500")
ventana.config(bg="white")

miFrame=Frame(ventana)
miFrame.pack()
miFrame.config(width="500",height="500")

nombre_producto = StringVar()
precio_ingresado = StringVar()
cantidad = StringVar()
total = StringVar()

def archivo_ventas(nombre_producto,precio,cantidad,ganancia):
    archivo_texto=open("ventas.doc","a")
    nombre_precio=("\n"+nombre_producto+" $ "+str(precio)+" cantidad vendida: "+str(cantidad)+" importe: $"+str(ganancia))
    archivo_texto.write(nombre_precio)
  
    archivo_texto.close()
    
def ver_venta():
    messagebox.showinfo("Correcto","La venta se registró correctamente")
    entry_nombre.delete(0,END)
    entry_precio.delete(0,END)
    entry_cantidad.delete(0,END)
    entry_total.delete(0,END)
    
def validar_ingresos():
    nombre = nombre_producto.get()
    precio_producto = int(precio_ingresado.get())
    cantidad_ingresada = int(cantidad.get())
    total.set(cantidad_ingresada*precio_producto)
    ganancia = cantidad_ingresada*precio_producto
    if precio_producto <=0:
        messagebox.showwarning("Error!","El precio debe ser mayor a cero")
        
    if len(nombre) <=0:
        messagebox.showwarning("Error!","Debe completar el campo nombre")

    if cantidad_ingresada <=0:
        messagebox.showwarning("Error!","Ingrese una cantidad mayor a 0")

    elif precio_producto >0 and len(nombre)>0 and cantidad_ingresada >0:
        archivo_ventas(nombre,precio_producto,cantidad_ingresada,ganancia)
        ver_venta()
        
    
miFrame.config(bd=40)
miFrame.config(cursor="hand2")

entry_nombre=Entry(miFrame,textvariable=nombre_producto)
entry_nombre.grid(row=0,column=1,)
nombre_label=Label(miFrame,text="Nombre del producto : ")
nombre_label.grid(row=0,column=0,sticky="e")

    
entry_precio=Entry(miFrame,textvariable=precio_ingresado)
entry_precio.grid(row=1,column=1,pady=10)
precio_label=Label(miFrame,text="Precio $ : ")
precio_label.grid(row=1,column=0,sticky="e")

entry_cantidad=Entry(miFrame,textvariable=cantidad)
entry_cantidad.grid(row=2,column=1,)
cantidad_label=Label(miFrame,text="Cantidad : ")
cantidad_label.grid(row=2,column=0,sticky="e")

entry_total=Entry(miFrame,textvariable=total)
entry_total.grid(row=3,column=1,pady=10)
total_label=Label(miFrame,text="Total $ : ")
total_label.grid(row=3,column=0,sticky="e")

boton=Button(ventana,text="Aceptar",command=validar_ingresos)
boton.pack()


ventana.mainloop()
