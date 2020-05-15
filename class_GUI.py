from tkinter import *


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
		#self.frame_left.config(bg="red")

		self.frame_left.config(width="350" ,height="750")



		#________________ area de botones y entris del frame left__________


		self.label1_frame_left=Label(self.frame_left, text="Ingrese la Informacion de la Venta" , font=(15) , fg="blue" )
		self.label1_frame_left.place(x=20 , y=20)


		self.label2_frame_left=Label(self.frame_left , text="Producto:" , font=(5))
		self.label2_frame_left.place(x=20 , y=100)
		self.Entry1_frame_lef=Text(self.frame_left , width=18 , height=3)
		self.Entry1_frame_lef.place(x=100 ,y=135)
		self.Button1_frame_lef=Button(self.frame_left , text="Buscar" , width="18" )
		self.Button1_frame_lef.place(x=100 , y=100)



		self.label3_frame_left=Label(self.frame_left , text="Cantidad:" , font=(5))
		self.label3_frame_left.place(x=20 , y=200)
		self.Entry2_frame_lef=Entry()
		self.Entry2_frame_lef.place(x=100 , y=200)

		self.label3_frame_left=Label(self.frame_left , text="Precio:" , font=(5))
		self.label3_frame_left.place(x=20 , y=250)
		self.Entry2_frame_lef=Entry()
		self.Entry2_frame_lef.place(x=100 , y=250)




		self.Button2_frame_lef=Button(self.frame_left , text="guardar" , width="15" )
		self.Button2_frame_lef.place(x=20 , y=330)

		self.Button3_frame_lef=Button(self.frame_left , text="Limpiar Campos" , width="15" )
		self.Button3_frame_lef.place(x=150 , y=330)






		#________________  FINNNN area de botones y entris del frame left__________



		#________________ area de botones y entris del frame arriba a la izquierda__________

		self.frame_top=Frame()
		self.frame_top.pack( side="left" ,anchor="n")
		#self.frame_top.config(bg="blue")
		self.frame_top.config(relief="sunken")
		self.frame_top.config(width="900" , height="100")




		self.label4_frame_raight=Label(self.frame_top , text="Venta"  ,  font=(1000000000) , fg="blue")
		self.label4_frame_raight.place(x=20 , y=20)


		self.label5_frame_raight=Label(self.frame_top , text="Usuario:"  ,  font=(1000000000) , fg="blue")
		self.label5_frame_raight.place(x=250 , y=20)
		self.INTERMEDIO=Label(self.frame_top , text="Angelo Urbano"  ,  font=(1000000000))
		self.INTERMEDIO.place(x=320 , y=20)


		self.label6_frame_raight=Label(self.frame_top , text="Cedula:"  ,  font=(1000000000) , fg="blue")
		self.label6_frame_raight.place(x=500 , y=20)
		self.INTERMEDIO2=Label(self.frame_top , text="25850696"  ,  font=(1000000000) )
		self.INTERMEDIO2.place(x=560 , y=20)





		self.root.mainloop()




new=create_window_point_of_sale()		
