import numpy as np 
import matplotlib.pyplot as plt 
import pyodbc

conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=DESKTOP-1MGIDFT;'
                      'Database=netMatrix;'
                      'Trusted_Connection=yes;')

cursor = conn.cursor()
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
 


def estimate_coef(x, y): 
    # number of observations/points 
    n = np.size(x) 
  
    # mean of x and y vector 
    m_x, m_y = np.mean(x), np.mean(y) 
  
    # calculating cross-deviation and deviation about x 
    SS_xy = np.sum(y*x) - n*m_y*m_x 
    SS_xx = np.sum(x*x) - n*m_x*m_x 
  
    # calculating regression coefficients 
    b_1 = SS_xy / SS_xx 
    b_0 = m_y - b_1*m_x 
  
    return(b_0, b_1) 
  
def plot_regression_line(x, y, b): 
    # plotting the actual points as scatter plot 
    plt.scatter(x, y, color = "m", 
               marker = "o", s = 30) 
  
    # predicted response vector 
    y_pred = b[0] + b[1]*x 
  
    # plotting the regression line 
    plt.plot(x, y_pred, color = "g") 
  
    # putting labels 
    plt.xlabel('x') 
    plt.ylabel('y') 
  
    # function to show plot 
    plt.show() 
  
def main(): 
    # observations 
    x = eje_x 
    y = eje_y 
  
    # estimating coefficients 
    b = estimate_coef(x, y) 
    #print("Estimated coefficients:\nb_0 = {}  \nb_1 = {}".format(b[0], b[1])) 
  
    # plotting regression line 
    plot_regression_line(x, y, b) 
  
if __name__ == "__main__": 
    main() 