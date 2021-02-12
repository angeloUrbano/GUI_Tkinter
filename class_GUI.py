from tkinter import *

import tkinter as tk

import sqlite3

from tkinter import ttk

from tkinter import messagebox
from connect_mysql  import *
from BackendSpace import *

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


#test_mysql1=test_mysql()		





class create_window_point_of_sale():



	def __init__(self):

		self.root=Tk()

		self.menu=Menu(self.root)
		self.root.config(menu=self.menu)


		#____________________var client__________

		self.name=StringVar()
		self.surname=StringVar()
		self.cedula=IntVar()
		self.fom_number=StringVar()
		self.status=StringVar()

		#____________________FINNN__________

		#___________________var proveedor_________

		self.name_proveedor=StringVar()
		self.name_producto=StringVar()
		self.fom_number2=IntVar()
		self.email=StringVar()
		


		#____________________________________


		#_________________var_product________

		self.name_product=StringVar()
		self.existing_quantity=IntVar()

		#__________________FIN_______________


		self.option1=Menu(self.menu , tearoff=0)
		self.option1.add_command(label="Add Cliente" , command=self.new_window_client_add)
		self.option1.add_command(label="Add Producto" , command=self.new_window_product_add)

		self.option2=Menu(self.menu , tearoff=0)
		self.option2.add_command(label="Add Caracteristica")
		self.option2.add_command(label="Add Proveedor" , command=self.new_window_proveedor_add)

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

		"""print(self.name.get(),
		self.surname.get(),
		self.cedula.get(),
		self.fom_number.get(),
		self.status.get())"""


	def new_window_client_add(self):

		self.root_client=Toplevel(self.root)
		


		self.label_client1=Label(self.root_client, text="Nombre:")
		self.label_client1.grid()
		self.entry_client1=Entry(self.root_client , textvariable=self.name)
		self.entry_client1.grid()

		self.label_client2=Label(self.root_client, text="Apellido:" )
		self.label_client2.grid()
		self.entry_client2=Entry(self.root_client ,  textvariable=self.surname)
		self.entry_client2.grid()

		self.label_client3=Label(self.root_client, text="Cedula:" )
		self.label_client3.grid()
		self.entry_client3=Entry(self.root_client ,  textvariable=self.cedula)
		self.entry_client3.grid()


		self.label_client4=Label(self.root_client, text="Telefono:" )
		self.label_client4.grid()
		self.entry_client4=Entry(self.root_client , textvariable=self.fom_number)
		self.entry_client4.grid()

		self.label_client5=Label(self.root_client, text="Estado:" )
		self.label_client5.grid()
		self.entry_client5=Entry(self.root_client , textvariable=self.status)
		self.entry_client5.grid()


		self.button_cliente1=Button(self.root_client, text="add" , command=self.test)
		self.button_cliente1.grid()

		self.button_cliente2=Button(self.root_client, text="Limpiar Campos" , command=self.clint)
		self.button_cliente2.grid()

		self.button_cliente2=Button(self.root_client, text="Lista" , command=self.update_list)
		self.button_cliente2.grid()

		

		#_______________________lista de productos__________________

		self.lista2=ttk.Treeview(self.root_client)

		self.lista2["columns"]=("uno" , "dos" , "tres" , "cuatro" ,"cinco" )
		self.lista2.column("#0" , width=30 , minwidth=70 )
		self.lista2.column("uno" , width=170 , minwidth=70 )
		self.lista2.column("dos" , width=150 , minwidth=150 )
		self.lista2.column("tres" , width=185, minwidth=100 )
		self.lista2.column("cuatro" , width=80 , minwidth=100)
		self.lista2.column("cinco" , width=80 , minwidth=100 )
		
		self.lista2.heading("#0" , text="codigo"   )
		self.lista2.heading("uno" , text="Nombre"   )
		self.lista2.heading("dos" , text="Apellido")
		self.lista2.heading("tres" , text="Cedula")
		self.lista2.heading("cuatro" , text="Telefono")
		self.lista2.heading("cinco" , text="Status")
		
		
		self.lista2.place(x=150 ,y=50)


		#_______________________lista de productos__________________



		

		self.root_client.mainloop()


	def new_window_product_add(self):

		self.root_product=Toplevel(self.root)


		self.label_product1=Label(self.root_product, text="Nombre Producto:")
		self.label_product1.grid()
		self.entry_product1=Entry(self.root_product)
		self.entry_product1.grid()

		self.label_product2=Label(self.root_product, text="Cantidad Existente:")
		self.label_product2.grid()
		self.entry_product2=Entry(self.root_product)
		self.entry_product2.grid()

		self.label_product3=Label(self.root_product, text="Caracteristicas:")
		self.label_product3.grid()
		self.entry_product3=Entry(self.root_product)
		self.entry_product3.grid()


		self.label_product4=Label(self.root_product, text="Precio Unitario:")
		self.label_product4.grid()
		self.entry_product4=Entry(self.root_product)
		self.entry_product4.grid()

		self.label_product5=Label(self.root_product, text="Proveedor:")
		self.label_product5.grid()
		self.entry_product5=Entry(self.root_product)
		self.entry_product5.grid()


		self.button_product1=Button(self.root_product, text="test")
		self.button_product1.grid()

		self.button_product2=Button(self.root_product, text="test")
		self.button_product2.grid()

		self.button_product3=Button(self.root_product, text="test")
		self.button_product3.grid()



		self.lista=ttk.Treeview(self.root_product)

		self.lista["columns"]=("uno" , "dos" , "tres"  )
		self.lista.column("#0" , width=30 , minwidth=70 )
		self.lista.column("uno" , width=270 , minwidth=270 )
		self.lista.column("dos" , width=150 , minwidth=150 )
		self.lista.column("tres" , width=185, minwidth=100 )
		
		self.lista.heading("#0" , text="codigo"   )
		self.lista.heading("uno" , text="Pedido"   )
		self.lista.heading("dos" , text="Cantidad")
		self.lista.heading("tres" , text="Precio")
		
		self.lista.place(x=150 ,y=50)


		

		self.root_product.mainloop()


	def new_window_proveedor_add(self):
		
		


		self.root_caracteristica= Toplevel(self.root)

		self.label_name_proveedor1=Label(self.root_caracteristica , text="Nombre:")
		self.label_name_proveedor1.grid()
		self.entry_name_proveedor=Entry(self.root_caracteristica , textvariable=self.name_proveedor)
		self.entry_name_proveedor.grid()

		self.label_produc_proveedor2=Label(self.root_caracteristica , text="Nombre Producto:")
		self.label_produc_proveedor2.grid()
		self.label_produc_proveedor2=Entry(self.root_caracteristica , textvariable=self.name_producto)
		self.label_produc_proveedor2.grid()	

		self.label_number_proveedor3=Label(self.root_caracteristica , text="Numero de Telefono:")
		self.label_number_proveedor3.grid()
		self.label_number_proveedor3=Entry(self.root_caracteristica , textvariable=self.fom_number2)
		self.label_number_proveedor3.grid()	

		self.label_email_proveedor4=Label(self.root_caracteristica , text="Email:")
		self.label_email_proveedor4.grid()
		self.label_email_proveedor4=Entry(self.root_caracteristica , textvariable=self.email)
		self.label_email_proveedor4.grid()

		self.button_proveedor_test=Button(self.root_caracteristica, text="Guardar", command=self.add_proveedor)
		self.button_proveedor_test.grid()
		self.button_proveedor_test2=Button(self.root_caracteristica, text="Limpiar campos" , command=self.proveedor_clint)
		self.button_proveedor_test2.grid()




		self.lista=ttk.Treeview(self.root_caracteristica)

		self.lista["columns"]=("uno" , "dos" , "tres"  )
		self.lista.column("#0" , width=30 , minwidth=70 )
		self.lista.column("uno" , width=270 , minwidth=270 )
		self.lista.column("dos" , width=150 , minwidth=150 )
		self.lista.column("tres" , width=185, minwidth=100 )
		
		self.lista.heading("#0" , text="codigo"   )
		self.lista.heading("uno" , text="Pedido"   )
		self.lista.heading("dos" , text="Cantidad")
		self.lista.heading("tres" , text="Precio")
		
		self.lista.place(x=150 ,y=50)	





		self.root_caracteristica.mainloop()	

		

	




		
