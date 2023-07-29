import pyodbc

try:
    connection=pyodbc.connect('DRIVER={SQL Server};SERVER=MSI;DATABASE=proyecto_samsung;Trusted_Connection=yes')
    print("Conexion exitosa")
except Exception as ex:
    print(ex)