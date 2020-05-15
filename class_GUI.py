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
		self.Entry1_frame_lef=Entry()
		self.Entry1_frame_lef.place(x=100 ,y=130)
		self.Button1_frame_lef=Button(self.frame_left , text="Buscar" , width="15" )
		self.Button1_frame_lef.place(x=100 , y=100)



		self.label3_frame_left=Label(self.frame_left , text="Cantidad:" , font=(5))
		self.label3_frame_left.place(x=20 , y=180)
		self.Entry2_frame_lef=Entry()
		self.Entry2_frame_lef.place(x=100 , y=180)

		self.label3_frame_left=Label(self.frame_left , text="Precio:" , font=(5))
		self.label3_frame_left.place(x=20 , y=230)
		self.Entry2_frame_lef=Entry()
		self.Entry2_frame_lef.place(x=100 , y=230)





		self.Button2_frame_lef=Button(self.frame_left , text="guardar" , width="15" )
		self.Button2_frame_lef.place(x=20 , y=280)

		self.Button3_frame_lef=Button(self.frame_left , text="Limpiar Campos" , width="15" )
		self.Button3_frame_lef.place(x=150 , y=280)












		#________________  FINNNN area de botones y entris del frame left__________




		self.frame_top=Frame()
		self.frame_top.pack( side="left" ,anchor="n")
		self.frame_top.config(bg="blue")
		self.frame_top.config(relief="sunken")
		self.frame_top.config(width="900" , height="100")



		self.root.mainloop()




new=create_window_point_of_sale()		
