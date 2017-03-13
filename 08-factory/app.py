from mysql_factory import Connection_Factory

connection = Connection_Factory().get_connection()

cursor.connection.cursor()

cursor.execute("SELECT * FROM usuarios")

for linha in cursor:
	print linha

connection.close()