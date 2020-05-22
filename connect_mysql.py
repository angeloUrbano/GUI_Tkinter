import mysql.connector as mysql


class connect_to_mysql:

	def __init__(self):

		self.my_conect=mysql.connect(host="localhost", user="root", passwd="Angelo2611#",  database="ventas")

		self.my_cursor=self.my_conect.cursor()

		





connect_to_mysql1=connect_to_mysql()
