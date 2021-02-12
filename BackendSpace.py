from tkinter import *

import tkinter as tk

import sqlite3

from tkinter import ttk

from tkinter import messagebox
from connect_mysql  import *

from class_GUI import *



class add_client(create_window_point_of_sale):

	def test(self):

		self.add=True

		self.my_conect=mysql.connect(host="localhost", user="root", passwd="Angelo2611#",  database="ventas")

		self.my_cursor=self.my_conect.cursor()


		try:

			if self.name.get()== "" or self.surname.get()== "" or self.cedula.get()== ""  or self.fom_number.get()=="" or self.status.get()== "":

				self.add=False

				messagebox.showwarning("BAD" , "No se pueden guardar campos vacios")

				self.clint()

			if (self.add):

				LIST=[(self.name.get(), self.surname.get(), self.cedula.get(), self.fom_number.get() , self.status.get())]

				self.my_cursor.executemany("INSERT INTO cliente VALUES (NULL , %s, %s, %s, %s, %s ) ",LISTA)

				self.my_conect.commit()
		
				messagebox.showinfo("GOOD" , "Registro guardado con exito")

				self.clint()

		except:

			messagebox.showwarning("BAD" , "En los Campos de Cedula Y/O Telefono no se Permite TEXTO o Campos Vacios")

			self.clint()

			


	def clint(self):

		self.name.set("")
		self.name.set("")
		self.surname.set("") 
		self.cedula.set("")
		self.fom_number.set("")
		self.status.set("")


	def proveedor_clint(self):

		self.name_proveedor=set("")
		self.name_producto=set("")
		self.fom_number2=set("")
		self.email=set("")




	def update_list(self):
		
		record =self.lista2.get_children()

		for elemento in record:

			self.lista2.delete(elemento)

		self.my_conect=mysql.connect(host="localhost", user="root", passwd="Angelo2611#",  database="ventas")

		self.my_cursor=self.my_conect.cursor()

		self.my_cursor.execute("SELECT * FROM cliente")

		lista=self.my_cursor.fetchall()
		
		for x in range(len(lista)):

			self.lista2.insert("" , 0 ,text=lista[x][0] , values=(lista[x][1] ,lista[x][2] ,lista[x][3] , lista[x][4], lista[x][5] ))
	



	def add_proveedor(self):
		self.my_conect=mysql.connect(host="localhost", user="root", passwd="Angelo2611#",  database="ventas")

		self.my_cursor=self.my_conect.cursor()
		self.add=True

		

		try:

			if self.name_proveedor.get()== "" or self.name_producto.get()== "" or self.fom_number2.get()== ""  or self.email.get()=="":

				self.add=False

				messagebox.showwarning("BAD" , "No se pueden guardar campos vacios")

				self.proveedor_clint()

			if (self.add):

				LIST=[(self.name_proveedor.get(), self.name_producto.get(), self.fom_number2.get(), self.email.get())]

				self.my_cursor.executemany("INSERT INTO proveedor VALUES (NULL , %s, %s, %s, %s ) ",LIST)

				self.my_conect.commit()
		
				messagebox.showinfo("GOOD" , "Registro guardado con exito")

				self.proveedor_clint()

		except:

			messagebox.showwarning("BAD" , "En  Campo de Telefono no se Permite TEXTO o Campos Vacios")

			self.proveedor_clint()	







		



		





add_client1=add_client()


		