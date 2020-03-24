def hola(eje_x):
    eje_x = ["hola","cola"]

def separadorString(eje_x,eje_y,cursor):
    for row in cursor:
        formateados = row[0].strftime("%m/%d/%Y,%H:%M:%S")
    resultado = formateados.split(',')
    eje_x.append(resultado[0])
    eje_y.append(resultado[1]) 

def aSegundos(eje_y_previo):
    eje_y= []
    for y in eje_y_previo:
        h, m ,s = y.split(':')    
    total_seconds = int(h) * 3600 + int(m) * 60 + int(s)
    eje_y.append(total_seconds)
    return eje_y

def fechasEnXSinRepetir(eje_x,resultado):
    for x in eje_x:
        flag = False
        for x_r in resultado:
            if (x_r == x):
                flag = True    
                break 
    if(flag == True):
        resultado.append(x)
    return resultado         