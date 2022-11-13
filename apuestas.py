from typing import Dict, List
from tabulate import tabulate



#Variable que muestra total de juegos analizados
totalTotal = 0


def calculadora(cash, cantidadBeneficios,listaValores, listaNombres):


    #Creando diccionario base con datos
    diccBase1 = dict(zip(listaNombres, listaValores))


    #Organizando de mayor a menor
    #Encontrando máximo valor
    a = max(listaValores)
    #Indice del máximo valor
    indice = listaValores.index(a)

    if indice == 0:

        anombre = listaNombres[0]

        if listaValores[1] >= listaValores[2]:
            
            bnombre = listaNombres[1] 
            b = listaValores[1]
            
            cnombre = listaNombres[2] 
            c = listaValores[2]
        else:
            
            bnombre = listaNombres[2] 
            b = listaValores[2]
            
            
            cnombre = listaNombres[1] 
            c = listaValores[1]

    elif indice == 1:

        anombre = listaNombres[1]

        if listaValores[0] >= listaValores[2]:
            
            bnombre = listaNombres[0]
            b = listaValores[0]

            cnombre = listaNombres[2]
            c = listaValores[2]

        else:

            bnombre = listaNombres[2]
            b = listaValores[2]
            
            cnombre = listaNombres[0]
            c = listaValores[0]

    elif indice == 2:

        anombre = listaNombres[2]

        if listaValores[0] >= listaValores[1]:
            
            bnombre = listaNombres[0]
            b = listaValores[0]
            
            cnombre = listaNombres[1]
            c = listaValores[1]

        else:
            
            bnombre = listaNombres[1]
            b = listaValores[1]
            
            cnombre = listaNombres[0]
            c = listaValores[0]


    #Generando listas para mostrar en formato tabla
    poblacion = [diccBase1[anombre], diccBase1[bnombre], diccBase1[cnombre]]
    nomABC = [anombre, bnombre, cnombre]
    
    table =[[nomABC], [poblacion]]

    #Mostrando Datos ordenados al usuario
    #print("Porcentajes asignados según casa")
    #print(tabulate(table, tablefmt="rst"))

    #Sacando cálculos básicos
    media = (a+b+c)/3
    varianza = (((a-media)**2)+((b-media)**2)+((c-media)**2))/3
    de = varianza**0.5

    table1 = [["Media", "Varianza", "Desviación E."], [media, varianza, de]]


    #print("Información estadística")
    #print(tabulate(table1, tablefmt="rst"))


    #--------------------------Procedimiento para sacar porcentajes
    #Listade xi
    listaxi=[]


    #Sacando porcentaje
    for i in poblacion:

        d = (i*(1/3))/media
        listaxi.append(d)


    #Variable fi o xt, no siempre da 1
    fi = 0
    for i in listaxi:
        fi+=i


    #Sacando yi
    listayi=[]

    for i in listaxi:
        yi = fi-i
        listayi.append(yi)

    #print de control
    #print(listayi)

    #Sacando variable lambda
    #Lambda es igual a la suma de los yi
    lamb = 0

    for i in listayi:
        lamb+=i

    #Sacando los porcentajes
    listaPorcentaje=[]

    for i in listayi:
        z=(i)/lamb
        #Se quita el 100
        #Se quitó un round z
        listaPorcentaje.append((z))

    table2 = [[nomABC],[listaPorcentaje]]

    #print("Porcentajes")
    print(tabulate(table2, tablefmt="rst"))

    #print("Cantidades de Dinero")


    #Sacando en dinero
    listaCash= []

    for i in listaPorcentaje:

        listaCash.append(i*cash)

    
    #-----------------------------------------------------
    table3=[[nomABC], [listaCash]]
    textoAgregado1 = tabulate(table3, tablefmt="rst")
    #print(textoAgregado1)

    #Sacar f
    #k siempre va a ser el ultimo de lista cash
    k= listaCash[2]
    rr = diccBase1[bnombre]
    tetta = 1 + cantidadBeneficios  

    #
    #f = (k*(c/tetta)) / ((rr)/tetta)
    #print(f)
    #Simplificando
    f = (k*c)/rr
    #print(f)

    #c es la tasa de k
    #Cuanto le debe apostar a la pero opción
    l = k*((c/(tetta))-1)-f #Se quita round l
    #print("La cantidad de dinero para su peor opción: " + str(l))

    #Definiendo si es una buena apuesta
    #if l<0:
    #    print("Es una apuesta NO recomendada")
    #elif l>=0 and l<100:
    #    print("Es una apuesta RIESGOSA")
    #elif l>=100:
    #    print("Es una apuesta Recomendada")    

    #Mostrando total inversión
    if (l*a)>=0:

        totalInversion = l + f + k
        
        if bnombre == "Empate":

            racional = "Racional"

        else:

            racional = "NO Racional"

    else:

        totalInversion = f + k

        if bnombre == "Empate":

            racional = "Racional"

        else:

            racional = "NO Racional"
    #----------------------------------------------------------------------
    #Sacando Rentabilidades
    rentabilidadk = ((k*c*100)/totalInversion) - 100

    rentabilidadf = ((f*b*100)/totalInversion) - 100

    rentabilidadl = ((l*a*100)/totalInversion) - 100
    
    #----------------------------------------------------------------------
    #Sacando la media real, valor esperado.
    #a,b,c son las tarifas dadas, a es peor.
    mediaReal = (a*listaPorcentaje[0])+(b*listaPorcentaje[1])+(c*listaPorcentaje[2])

    varainzaReal = (((a-mediaReal)**2)*listaPorcentaje[0])+(((b-mediaReal)**2)*listaPorcentaje[1])+(((c-mediaReal)**2)*listaPorcentaje[2])

    deReal = varainzaReal**0.5

    #----------------------------------------------------------------------    
    #Sacando Supuestos Estadísticos de control
    #c y b deben estar por debajo de la media
    supuestoE1 = False

    z1 = mediaReal+deReal

    z_1 = mediaReal-deReal

    print(a)
    print(b)
    print(c)
    print(abs(z1-a))
    print(abs(z_1-c))

    if abs(z1-a)>abs(z_1-c):

        supuestoE1 = True
    
    #Simetrìa positiva, se desea.
    #a la desviación estándar
    supuestoE2 = False

    #Final - inicial
    if b <= mediaReal and c<= mediaReal:

        supuestoE2 = True

    #----------------------------------------------------------------------
    #Curtosis
    curtosisNum = (((a-mediaReal)**4)*listaPorcentaje[0])+(((b-mediaReal)**4)*listaPorcentaje[1])+(((c-mediaReal)**4)*listaPorcentaje[2])
    curtosisDen = deReal**4
    curtosis = (curtosisNum / curtosisDen)-3
    print("Su curtosis es de: " + str(curtosis))

    #----------------------------------------------------------------------
    #Skewness
    skewNum = (((a-mediaReal)**3)*listaPorcentaje[0])+(((b-mediaReal)**3)*listaPorcentaje[1])+(((c-mediaReal)**3)*listaPorcentaje[2])
    skewDen = varainzaReal**(3/2)
    skew = (skewNum/ skewDen)
    print("Su skewness es de: " + str(skew))

    #----------------------------------------------------------------------
    #Minimización de riesgo máximo
    #Dinero Total
    Dt = (k*c)/tetta
    j = Dt / (Dt - f- k)


    #----------------------------------------------------------------------
    #Devuelve una lista con los valores
    return [l,f,k,
    rentabilidadl,rentabilidadf,rentabilidadk,
    totalInversion,
    anombre, bnombre, cnombre, 
    racional, c,
    mediaReal, varainzaReal, deReal,
    supuestoE1, supuestoE2, curtosis, skew, j]
