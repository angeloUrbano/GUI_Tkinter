from tkinter import *

import tkinter as tk

import sqlite3

from tkinter import ttk

from tkinter import messagebox
from connect_mysql  import *

class test_mysql(connect_to_mysql):	
	"""de esta manera a travez de la herencia puedo acceder 
	a la clase que me esta gestionando la coneccion a la BBDD"""				

	def __init__(self):

		super().__init__()

		
		self.my_cursor.execute('''
				CREATE TABLE LIBROS(
				NOMBRE VARCHAR(100));
			''')
		self.my_conect.commit()


test_mysql1=test_mysql()		





class create_window_point_of_sale():



	def __init__(self):

		self.root=Tk()

		self.menu=Menu(self.root)
		self.root.config(menu=self.menu)


		self.option1=Menu(self.menu , tearoff=0)
		self.option1.add_command(label="nuevo")
		self.option1.add_command(label="nuevo")

		self.option2=Menu(self.menu , tearoff=0)
		self.option2.add_command(label="nuevo")
		self.option2.add_command(label="nuevo")

		self.option3=Menu(self.menu , tearoff=0)
		self.option3.add_command(label="nuevo")
		self.option3.add_command(label="nuevo")

		self.option4=Menu(self.menu , tearoff=0)
		self.option4.add_command(label="nuevo")
		self.option4.add_command(label="nuevo")


		self.menu.add_cascade(label="prueba" , menu=self.option1)
		self.menu.add_cascade(label="prueba2" , menu=self.option2)
		self.menu.add_cascade(label="prueba3" , menu=self.option3)
		self.menu.add_cascade(label="prueba4" , menu=self.option4)


		


		self.frame_left=Frame()

		self.frame_left.pack(side="left" , anchor="n")
		self.frame_left.config(bg="azure2")

		self.frame_left.config(width="350" ,height="750")



		#________________ area de botones y entris del frame left__________


		self.label1_frame_left=Label(self.frame_left, text="Ingrese la Informacion de la Venta" , font=(15) , fg="lime green")
		self.label1_frame_left.place(x=20 , y=20)


		self.label2_frame_left=Label(self.frame_left , text="Producto:" , font=(5) , fg="lime green")
		self.label2_frame_left.place(x=20 , y=100)
		self.Entry1_frame_lef=Text(self.frame_left , width=18 , height=3)
		self.Entry1_frame_lef.place(x=100 ,y=135)
		self.Button1_frame_lef=Button(self.frame_left , text="Buscar" , width="18"  , fg="lime green")
		self.Button1_frame_lef.place(x=100 , y=100)



		self.label3_frame_left=Label(self.frame_left , text="Cantidad:" , font=(5) , fg="lime green")
		self.label3_frame_left.place(x=20 , y=200)
		self.Entry2_frame_lef=Entry()
		self.Entry2_frame_lef.place(x=100 , y=200)

		self.label3_frame_left=Label(self.frame_left , text="Precio:" , font=(5) , fg="lime green")
		self.label3_frame_left.place(x=20 , y=250)
		self.Entry2_frame_lef=Entry()
		self.Entry2_frame_lef.place(x=100 , y=250)




		self.Button2_frame_lef=Button(self.frame_left , text="guardar" , width="15" , fg="lime green" )
		self.Button2_frame_lef.place(x=20 , y=330)

		self.Button3_frame_lef=Button(self.frame_left , text="Limpiar Campos" , width="15"  , fg="lime green")
		self.Button3_frame_lef.place(x=150 , y=330)




		self.miimagen=PhotoImage(file="gastos.png")

		
		self.label1=Label(self.frame_left,image=self.miimagen)
		self.label1.place(x=0 , y=500)






		#________________  FINNNN area de botones y entris del frame left__________



		

		self.frame_top=Frame()
		self.frame_top.pack( side="left" ,anchor="n")
		self.frame_top.config(bg="azure2")
		self.frame_top.config(bd=30)
		self.frame_top.config(relief="groove")
		self.frame_top.config(width="900" , height="800")


		#________________ area de botones y entris del frame arriba a la derecha__________

		self.label4_frame_raight=Label(self.frame_top , text="Venta"  ,  font=(1000000000) , fg="lime green")
		self.label4_frame_raight.place(x=20 , y=20)


		self.label5_frame_raight=Label(self.frame_top , text="Usuario:"  ,  font=(1000000000) , fg="lime green")
		self.label5_frame_raight.place(x=250 , y=20)
		self.INTERMEDIO=Label(self.frame_top , text="Angelo Urbano"  ,  font=(1000000000))
		self.INTERMEDIO.place(x=320 , y=20)


		self.label6_frame_raight=Label(self.frame_top , text="Cedula:"  ,  font=(1000000000) ,fg="lime green")
		self.label6_frame_raight.place(x=500 , y=20)
		self.INTERMEDIO2=Label(self.frame_top , text="25850696"  ,  font=(1000000000) )


		self.entry7_frame_raight=Entry(self.frame_top)
		self.entry7_frame_raight.place(x=20 , y=500)

		self.Button4_frame_top=Button(self.frame_top , text="Buscar Cliente" , width="15"  , fg="lime green")
		self.Button4_frame_top.place(x=160 , y=500)

		self.Entry8_frame_top=Text(self.frame_top , width=22 , height=3)
		self.Entry8_frame_top.place(x=20 ,y=530)


		self.Button4_frame_top=Button(self.frame_top , text="Realizar" , width="15"  , fg="lime green")
		self.Button4_frame_top.place(x=20 , y=610)


		self.Button6_frame_top=Button(self.frame_top , text="Eliminar" , width="15"  , fg="lime green")
		self.Button6_frame_top.place(x=160 , y=610)

		self.Button7_frame_top=Button(self.frame_top , text="Limpiar" , width="15"  , fg="lime green")
		self.Button7_frame_top.place(x=100 , y=650)



		self.label7_frame_raight=Label(self.frame_top , text="Total a Pagar"  ,  font=(1000000000) ,fg="red")
		self.label7_frame_raight.place(x=520 , y=500)

		self.label8_frame_raight=Label(self.frame_top , text="Paga Con:"  ,  font=(1000000000) ,fg="red")
		self.label8_frame_raight.place(x=520 , y=550)


		self.entry9_frame_raight=Entry(self.frame_top)
		self.entry9_frame_raight.place(x=520 , y=580)


		self.label9_frame_raight=Label(self.frame_top , text=" Se debe entregar Cambio de.."  ,  font=(1000000000) ,fg="red")
		self.label9_frame_raight.place(x=520 , y=620)
		









		self.INTERMEDIO2.place(x=560 , y=20)

		#________________ area de botones y entris del frame arriba a la derecha__________




		#_______________________lista de productos__________________

		self.lista=ttk.Treeview(self.frame_top)

		self.lista["columns"]=("uno" , "dos" , "tres"  )
		self.lista.column("#0" , width=30 , minwidth=70 )
		self.lista.column("uno" , width=270 , minwidth=270 )
		self.lista.column("dos" , width=150 , minwidth=150 )
		self.lista.column("tres" , width=185, minwidth=100 )
		
		self.lista.heading("#0" , text="codigo"   )
		self.lista.heading("uno" , text="Pedido"   )
		self.lista.heading("dos" , text="Cantidad")
		self.lista.heading("tres" , text="Precio")
		
		self.lista.place(x=80 ,y=50)


		#_______________________lista de productos__________________


		



		

		self.root.mainloop()




new=create_window_point_of_sale()		
