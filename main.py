import numpy as np 
import tensorflow as tf 
import matplotlib.pyplot as plt 
import pyodbc





conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=DESKTOP-1MGIDFT;'
                      'Database=netMatrix;'
                      'Trusted_Connection=yes;')

cursor = conn.cursor()

#Esto es de eventos de seguridad 1.0
#cursor.execute('SELECT [IdEvento],[IdTipoActivoXIndicador],[IdActivo],[IdCategoriaActivo],[IdEstado],[IdReglaEvento],[FechaHoraEvento],[FechaHoraBitacora],[FechaHoraNormalizacion],[FechaHoraModificacion],[FechaHoraLocalEvento],[FechaHoraLocalNormalizacion],[IdEventoPadre] FROM [netmatrix_final].[dbo].[Evento] WHERE [IdReglaEvento] = 4 OR [IdReglaEvento] = 7 OR [IdReglaEvento] = 22 OR [IdReglaEvento] = 23 OR [IdReglaEvento] = 24 OR [IdReglaEvento] = 25 OR [IdReglaEvento] = 26 OR [IdReglaEvento] = 1013 OR [IdReglaEvento] = 1014 OR [IdReglaEvento] = 1017 OR [IdReglaEvento] = 1018 OR [IdReglaEvento] = 1021 OR [IdReglaEvento] = 1023 OR [IdReglaEvento] = 1024 OR [IdReglaEvento] = 1026 OR [IdReglaEvento] = 1028')

#Esto es de eventos solo con la fecha simplificado (solo fecha)
##cursor.execute('SELECT [FechaHoraEvento] FROM [netmatrix_final].[dbo].[Evento] WHERE [IdReglaEvento] = 4 OR [IdReglaEvento] = 7 OR [IdReglaEvento] = 22 OR [IdReglaEvento] = 23 OR [IdReglaEvento] = 24 OR [IdReglaEvento] = 25 OR [IdReglaEvento] = 26 OR [IdReglaEvento] = 1013 OR [IdReglaEvento] = 1014 OR [IdReglaEvento] = 1017 OR [IdReglaEvento] = 1018 OR [IdReglaEvento] = 1021 OR [IdReglaEvento] = 1023 OR [IdReglaEvento] = 1024 OR [IdReglaEvento] = 1026 OR [IdReglaEvento] = 1028')



#Esto es de eventos de fallas 1.0
##cursor.execute('SELECT [IdEvento],[IdTipoActivoXIndicador],[IdActivo],[IdCategoriaActivo],[IdEstado],[IdReglaEvento],[FechaHoraEvento],[FechaHoraBitacora],[FechaHoraNormalizacion],[FechaHoraModificacion],[FechaHoraLocalEvento],[FechaHoraLocalNormalizacion],[IdEventoPadre] FROM [netmatrix_final].[dbo].[Evento] WHERE [IdReglaEvento] = 9 OR [IdReglaEvento] = 13 OR [IdReglaEvento] = 14 OR [IdReglaEvento] = 16 OR [IdReglaEvento] = 18 OR [IdReglaEvento] = 19 OR [IdReglaEvento] = 20 OR [IdReglaEvento] = 21 OR [IdReglaEvento] = 27 OR [IdReglaEvento] = 28 OR [IdReglaEvento] = 39 OR [IdReglaEvento] = 80 OR [IdReglaEvento] = 81 OR [IdReglaEvento] = 82 OR [IdReglaEvento] = 83 OR [IdReglaEvento] = 86')

#Esto es de eventos de fallas simplificado (solo fecha)
##cursor.execute('SELECT [FechaHoraEvento] FROM [netmatrix_final].[dbo].[Evento] WHERE [IdReglaEvento] = 9 OR [IdReglaEvento] = 13 OR [IdReglaEvento] = 14 OR [IdReglaEvento] = 16 OR [IdReglaEvento] = 18 OR [IdReglaEvento] = 19 OR [IdReglaEvento] = 20 OR [IdReglaEvento] = 21 OR [IdReglaEvento] = 27 OR [IdReglaEvento] = 28 OR [IdReglaEvento] = 39 OR [IdReglaEvento] = 80 OR [IdReglaEvento] = 81 OR [IdReglaEvento] = 82 OR [IdReglaEvento] = 83 OR [IdReglaEvento] = 86')




cursor.execute('SELECT [FechaHoraEvento] FROM [netmatrix_final].[dbo].[Evento] WHERE [IdReglaEvento] = 9 OR [IdReglaEvento] = 13 OR [IdReglaEvento] = 14 OR [IdReglaEvento] = 16 OR [IdReglaEvento] = 18 OR [IdReglaEvento] = 19 OR [IdReglaEvento] = 20 OR [IdReglaEvento] = 21 OR [IdReglaEvento] = 27 OR [IdReglaEvento] = 28 OR [IdReglaEvento] = 39 OR [IdReglaEvento] = 80 OR [IdReglaEvento] = 81 OR [IdReglaEvento] = 82 OR [IdReglaEvento] = 83 OR [IdReglaEvento] = 86')

eje_x = []
eje_y_previo = [] 
eje_y = [] 


for row in cursor:
    formateados = row[0].strftime("%m/%d/%Y,%H:%M:%S")
    resultado = formateados.split(',')
    eje_x.append(resultado[0])
    eje_y_previo.append(resultado[1]) 

for y in eje_y_previo:
    h, m ,s = y.split(':')    
    total_seconds = int(h) * 3600 + int(m) * 60 + int(s)
    eje_y.append(total_seconds)
 
n = len(eje_x)

plt.scatter(eje_x,eje_y)

plt.xlabel('fechas')
plt.xticks(rotation=90) 
plt.ylabel('segundos')
plt.title("Entrenamiento")
plt.show()


 