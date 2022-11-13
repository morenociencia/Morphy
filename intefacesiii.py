import tkinter as tk
from tkinter.font import BOLD
from typing import Collection

#Importando modulo
import apuestas as app



def main():


    #Raiz
    root = tk.Tk()

    root.title("Morphy")

    #Poder redimensionar y tamaño
    root.resizable(1, 1)
    root.geometry("900x400")

    #Creando frame
    frame0 = tk.Frame(root)

    #Tamaño del frame

    frame0.pack(expand=True)

    #Creando Label y Entry
    #Ingresando cantidad de dinero
    
    #Creando variables a usar
    #Cantidades de dinero optimas
    k = tk.DoubleVar()
    f = tk.DoubleVar()
    l = tk.DoubleVar()

    #Rentabilidades de cada uno
    rentak = tk.DoubleVar()
    rentaf = tk.DoubleVar()
    rental = tk.DoubleVar()

    #Inversión total
    inverT = tk.DoubleVar()

    #Nombre de los jugadores
    nombrek = tk.StringVar()
    nombrek.set("El valor para su k: ")

    nombref = tk.StringVar()
    nombref.set("El valor para su f: ")

    nombrel = tk.StringVar()
    nombrel.set("El valor para su l: ")

    #Determinando si es un juego racional
    racional = tk.StringVar()
    racional.set("Esperando")

    #Valor por defecto de empate
    empate = tk.StringVar()
    empate.set("Empate")

    #Comparador
    #Minimización media
    minM = tk.DoubleVar()

    #Información Estadística
    media = tk.StringVar()
    media.set("Media: ")

    varianza = tk.StringVar()
    varianza.set("Varianza: ")

    desviacionE = tk.StringVar()
    desviacionE.set("D.E.: ")

    #Agregando supuesto estadístico 1 y 2
    sE1 = tk.StringVar()
    sE1.set("S.S.0: ")

    sE2 = tk.StringVar()
    sE2.set("S.S.1: ")

    #Agregando Curtosis
    kurt = tk.StringVar()
    kurt.set("Curtosis")

    #Agregando Skewness
    skewness = tk.StringVar()
    skewness.set("Skewness")

    #Agregando minRiesgo j
    jmin = tk.StringVar()
    jmin.set("j minimo")


    #------------------------------------------------------------

    #Mostrando minimizaciñon media
    minM_E = tk.Label(frame0,textvariable=minM)
    minM_E.config(bg="#52BE80")
    minM_E.grid(column=0, row=1)

    #Texto

    racionalE = tk.Label(frame0, textvariable=racional)
    racionalE.config(bg="#DC7633")
    racionalE.grid(column=0, row=0)

    #Columnspan para que ocupe más de una columna
    dineroT = tk.Label(frame0, text="Ingrese la cantidad de dinero: ")
    dineroT.grid(column=1,row=0, padx=10, pady=10)


    #Entrada
    dineroE = tk.Entry(frame0)
    dineroE.grid(column=2, row=0, padx=10, pady=10)


    #Tasa de rentabilidad
    tasaT = tk.Label(frame0, text="Ingrese la tasa de rentabilidad: ")
    tasaT.grid(column=1, row=1)

    tasaE = tk.Entry(frame0)
    tasaE.grid(column=2, row=1)


    #Mostrando el total invertido
    totalI_T = tk.Label(frame0, text="Inversión Total: ")
    totalI_T.grid(column=3, row=0)
    totalI_T.config(font=BOLD)

    totalI_E = tk.Label(frame0, textvariable= inverT)
    totalI_E.config(bg="#DC7633")
    totalI_E.grid(column=3, row=1)
    

    #---------------------------Ingresando datos------------------
    iD = tk.Label(frame0, text="Ingrese el dato de los jugadores")
    iD.grid(column=0, row=2, padx=15, pady=15, columnspan=4)
    iD.config(font=BOLD)


    #---------------------------Ingresando tasas------------------
    #Label
    tasa0 = tk.Label(frame0, text="Ingrese la tasa: ")
    tasa0.grid(column=0, row=3, pady=5)

    tasa1 = tk.Label(frame0, text="Ingrese la tasa: ")
    tasa1.grid(column=0, row=4, pady=5)

    tasa2 = tk.Label(frame0, text="Ingrese la tasa: ")
    tasa2.grid(column=0, row=5, pady=5)


    #Datos
    #Jugador--------------------------1
    tasaE0 = tk.Entry(frame0)
    tasaE0.grid(column=1, row=3, pady=5)

    nombreE0 = tk.Entry(frame0)
    nombreE0.grid(column=3, row=3, pady=5)


    #Jugador---------------------------2
    tasaE1 = tk.Entry(frame0)
    tasaE1.grid(column=1, row=4, pady=5)

    nombreE1 = tk.Label(frame0, textvariable=empate)
    nombreE1.grid(column=3, row=4, pady=5)


    #Jugador----------------------------3
    tasaE2 = tk.Entry(frame0)
    tasaE2.grid(column=1, row=5, pady=5)

    nombreE2 = tk.Entry(frame0)
    nombreE2.grid(column=3, row=5, pady=5)


    #Nombre de los jugadores
    nombreT0 = tk.Label(frame0, text="Ingrese el nombre del jugador: ")
    nombreT0.grid(column=2, row=3, pady=5)

    nombreT1 = tk.Label(frame0, text="Ingrese el nombre del jugador: ")
    nombreT1.grid(column=2, row=4, pady=5)

    nombreT2 = tk.Label(frame0, text="Ingrese el nombre del jugador: ")
    nombreT2.grid(column=2, row=5, pady=5)


    #---------------------Funciones Importantes---------------------------
    def nombres():
        
        cash = float(dineroE.get())
        cantidadBeneficios = float(tasaE.get())

        nombre0 = nombreE0.get()
        #Predeterminado para saber racionalidad
        #Llamar al valor de empate
        nombre1 = empate.get()
        nombre2 = nombreE2.get()

        tasa_0 = tasaE0.get()
        tasa_1 = tasaE1.get()
        tasa_2 = tasaE2.get()

        listaNombres = [nombre0, nombre1, nombre2]
        listaValores = [float(tasa_0), float(tasa_1), float(tasa_2)]
        
        salida = app.calculadora(cash, cantidadBeneficios, listaValores, 
        listaNombres)

        #Colocando valores en los entry
        #Cantidades de dinero
        k.set(round(salida[2], 2))
        f.set(round(salida[1], 2))
        l.set(round(salida[0], 2))

        #Rentabilidades
        rentak.set(round(salida[5], 2))
        rentaf.set(round(salida[4], 2))
        rental.set(round(salida[3], 2))

        inverT.set(round(salida[6], 2))

        #Colocando nombre de jugadores
        #Según Corresponda
        nombrek.set(salida[9])
        nombref.set(salida[8])
        nombrel.set(salida[7])

        #Determinando si es un juego racional
        racional.set(salida[10])

        #Determinando la minimización media

        #Muestra lo que debería pagar con doble opción
        minM.set(
            round(
            (round(salida[2], 2)*(salida[11]))
            /
            (round(salida[2], 2)+round(salida[1], 2))
            , 2))

        #Sacando información estadística

        media.set("Media: " + str(round(salida[12],2)))

        varianza.set("Varianza: " + str(round(salida[13],2)))

        desviacionE.set("D.E.: " + str(round(salida[14],2)))

        #Supestos estadísticos
        sE1.set("S.S.0: " + str(salida[15]))

        sE2.set("S.S.1: " + str(salida[16]))

        #Curtosis
        kurt.set("Curtosis: " + str(round(salida[17],4)))

        #skewness
        skewness.set("Skew: " + str(round(salida[18],4)))

        #jmin
        jmin.set("j: " + str(round(salida[19],4)))

        #print(salida)


    #----------------------Botón de calculo------------------------------


    #Boton en row6, column0
    boton0 = tk.Button(frame0, text="Calcular", width=25, height=1, command= nombres)
    boton0.grid(column=0, row=6,padx=15, pady=15, columnspan=4)
    boton0.config(font=BOLD)


    #-------------------------------Mostrando Resultados----------------------------
    #

    resultadoT0 = tk.Label(frame0, textvariable=nombrek)
    resultadoT0.grid(column=0, row=7, padx=20, pady=5)

    resultadoT0 = tk.Label(frame0, textvariable=nombref)
    resultadoT0.grid(column=0, row=8, padx=20, pady=5)

    resultadoT0 = tk.Label(frame0, textvariable=nombrel)
    resultadoT0.grid(column=0, row=9, padx=20, pady=5)


    resultadoE0 = tk.Entry(frame0, textvariable=k).grid(column=1, row=7)

    resultadoE0 = tk.Entry(frame0, textvariable=f).grid(column=1, row=8)

    resultadoE0 = tk.Entry(frame0, textvariable=l).grid(column=1, row=9)


    #------------------Tasas de perdidad y ganancia------------------

    #REEEEEEMPLAZAR LOS VALORES DE K F L POR NOMBRES INGRESADOS

    tasaR_T0 = tk.Label(frame0, text=" Rentabilidad de k % : ")
    tasaR_T0.grid(column=2, row=7)

    tasaR_T1 = tk.Label(frame0, text=" Rentabilidad de f % : ")
    tasaR_T1.grid(column=2, row=8)
    
    tasaR_T2 = tk.Label(frame0, text=" Rentabilidad de l % : ")
    tasaR_T2.grid(column=2, row=9)
    

    #Mostrando las tasa

    tasaR_E0 = tk.Entry(frame0, textvariable=rentak)
    tasaR_E0.grid(column=3, row=7)

    tasaR_E1 = tk.Entry(frame0, textvariable=rentaf)
    tasaR_E1.grid(column=3, row=8)

    tasaR_E2 = tk.Entry(frame0, textvariable=rental)
    tasaR_E2.grid(column=3, row=9)


    #----------------Mostrando información estadístico--------------

    #row3, column 4 and 5

    media_T = tk.Label(frame0,textvariable=media)
    media_T.grid(column=4, row=0)
    
    varianza_T = tk.Label(frame0, textvariable=varianza)
   # varianza_T.config(bg="#52BE80")
    varianza_T.grid(column=4, row=1)
    
    #Debido a que los cambios son pequeños
    #Es mejor tener como referencia la 
    #Desviación Estándar
    
    de_T = tk.Label(frame0, textvariable=desviacionE)
    de_T.config(bg="#52BE80")
    de_T.grid(column=5, row=2)

    #---------------Mostrando Supestos Estadísticos----------------------

    sE1_T = tk.Label(frame0, textvariable=sE1)
    sE1_T.config(bg="#F4D03F")
    sE1_T.grid(column=5,row=3)

    sE2_T = tk.Label(frame0, textvariable=sE2)
    sE2_T.config(bg="#F4D03F")
    sE2_T.grid(column=5, row=4)

    #-------------------- Mostrando Curtosis------------------------------
    kurt_T = tk.Label(frame0, textvariable=kurt)
    kurt_T.config(bg="#F4D03F")
    kurt_T.grid(column=5, row=5)

    #-------------------- Mostrando Skewness------------------------------
    skew_T = tk.Label(frame0, textvariable=skewness)
    skew_T.config(bg="#F4D03F")
    skew_T.grid(column=5, row=6)

    #-------------------- Mostrando j minimo------------------------------
    jmin_T = tk.Label(frame0, textvariable=jmin)
    jmin_T.config(bg="#5DADE2")
    jmin_T.grid(column=5, row=7)



    root.mainloop()


if __name__ == "__main__" :
    main()
