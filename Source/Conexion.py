import pyodbc

try:
    connection=pyodbc.connect('DRIVER={SQL Server};SERVER=JHOSTIN\SQLEXPRESS;DATABASE=proyecto_samsung;UID=sa;PWD=1234')
    print("Conexion exitosa")
except Exception as ex:
    print(ex)