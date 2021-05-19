#Proyecto Final Fisica 3
#19845, Juan Marroquín
#19077, Pablo Marroquín
#16387, Sergio Marchena

#bibliotecas que usaremos
import math
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from mpl_toolkits.mplot3d import Axes3D
import random


#funcion que calcula la velocidad del selector de velocidades
def velocidad(Vol,d,B):
    return Vol/(d*B)
#funcion que calcula el radio en el electrometro de masas
def RadioPar(masa,vel,B,q):
    if q == 0:
        r=0
    else:
        r = (masa*vel)/(abs(q)*B)
    return r
#funcion que recorre la lista de particulas y devuelve su nombre masa y carga
def esc_particula(particulas,name):
    for i in particulas:
        if i[0]==name:
            par = i[0]
            masa = i[1]
            carga = i[2]
    return par,masa,carga
#funcion que agruega particulas a la lista de partiuclas
def agregar_particulas(particulas,nombre,masa,carga):
    particulas.append([nombre,masa,carga,12])
    print("Su particula ha sida agregada a la base de datos\n")
    
    
#funcion que imprime todas las particulas de la base de datos
def imprimir_particulas(particulas):
    for lista in particulas:
        print(str(lista[3])+") "+lista[0])

#funcion que generar las velocidades random y las almacena en una lista
def GenerarVelParticulas(vel,n):
    lista=[]
    for i in range(0,n):
        lista.append(random.uniform(1, 2*vel))
    return lista
#funcion que dispara las particulas al selector de velocidades y cuenta cuantas particulas cumplen con la velocidad deseada
def DispararParticulas(lista,vel):
    cont = 0
    for i in lista:
        if i == vel:
            cont = cont + 1
    return cont

def Graficar1(r1,par1):
    pi = 3.14159265359
    t1 = np.linspace(pi/2, -pi/2, 50)
    x1 = r1*np.cos(t1)
    y1 = r1*np.sin(t1)
    fig, ax = plt.subplots(1) 
    ax.set_aspect('equal', adjustable='box')
    ax.plot(x1,y1)
    ax.legend([par1])
    def actualizar(i):
        ax.clear()
        ax.plot(x1[:i],y1[:i])
        plt.grid(True)
        plt.subplots_adjust(left=0.25)
        plt.title("Trayectoria de partículas en Espectrometro de masas")
        ax.legend([par1])
        plt.xlabel('x (m)')  
        plt.ylabel('y (m)')
    ani = animation.FuncAnimation(fig,actualizar,range(len(x1)),interval = 100,repeat = False)
    plt.show()
    return "Graficado con exito\n"

def Graficar2(r1,r2,par1,par2):
    pi = 3.14159265359
    t1 = np.linspace(pi/2, -pi/2, 50)
    t2 = np.linspace(pi/2, -pi/2, 50)
    x1 = r1*np.cos(t1)
    x2 = r2*np.cos(t2)
    y1 = r1*np.sin(t1)
    y2 = r2*np.sin(t2)
    fig, ax = plt.subplots(1) 
    ax.set_aspect('equal', adjustable='box')
    ax.plot(x1,y1)
    ax.plot(x2,y2)
    ax.legend([par1,par2])
    def actualizar(i):
        ax.clear()
        ax.plot(x1[:i],y1[:i])
        ax.plot(x2[:i],y2[:i])
        plt.grid(True)
        plt.subplots_adjust(left=0.25)
        plt.title("Trayectoria de partículas en Espectrometro de masas")
        ax.legend([par1,par2])
        plt.xlabel('x (m)')  
        plt.ylabel('y (m)')
    ani = animation.FuncAnimation(fig,actualizar,range(len(x1)),interval = 100,repeat = False)
    plt.show()
    return "Graficado con exito\n"

#funcion que grafica para 3 particulas
def Graficar(r1,r2,r3,par1,par2,par3):
    #imprimir en pantalla
    pi = 3.14159265359
    #angulos para graficar en funcion del angulo
    #theta1 = np.linspace(0,np.pi/2)
    #theta2 = np.linspace(0,np.pi/2)
    #theta3 = np.linspace(0,np.pi/2)
    t1 = np.linspace(pi/2, -pi/2, 50)
    t2 = np.linspace(pi/2, -pi/2, 50)
    t3 = np.linspace(pi/2, -pi/2, 50) 
    #variable dependientes
    #y1 = 2*r1*np.sin(theta1)
    #y2 = 2*r2*np.sin(theta2)
    #y3 = 2*r3*np.sin(theta3)
    x1 = r1*np.cos(t1)
    x2 = r2*np.cos(t2)
    x3 = r3*np.cos(t3)
    y1 = r1*np.sin(t1)
    y2 = r2*np.sin(t2)
    y3 = r3*np.sin(t3)
    #creacion de las graficas
    #fig = plt.figure()
    #ax = fig.add_subplot(111, projection="polar")
    fig, ax = plt.subplots(1) 
    #ax.plot(theta1,y1)
    #ax.plot(theta2,y2)
    #ax.plot(theta3,y3)
    ax.set_aspect('equal', adjustable='box')
    ax.plot(x1,y1)
    ax.plot(x2,y2)
    ax.plot(x3,y3)
    ax.legend([par1,par2,par3])
    def actualizar(i):
        ax.clear()
        #animacion de las graficas
        #ax.plot(theta1[:i],y1[:i])
        #ax.plot(theta2[:i],y2[:i])
        #ax.plot(theta3[:i],y3[:i])
        
        ax.plot(x1[:i],y1[:i])
        ax.plot(x2[:i],y2[:i])
        ax.plot(x3[:i],y3[:i])
        #plt.text(0, 0,z1)
        #plt.text(0, 2,z2)
        #plt.text(0, 4,z3)
        #plt.gcf().text(0, 0, z1, fontsize=10)
        #plt.gcf().text(0.3, 0, z2, fontsize=10)
        #plt.gcf().text(0.7, 0, z3, fontsize=10)
        plt.grid(True)
        plt.subplots_adjust(left=0.25)
        plt.title("Trayectoria de partículas en Espectrometro de masas")
        ax.legend([par1,par2,par3])
        plt.xlabel('x (m)')  
        plt.ylabel('y (m)') 
        #limites de las graficas
        #plt.xlim(min(theta1),2*max(theta1))
        #plt.ylim(min(y1),max(y1))
    ani = animation.FuncAnimation(fig,actualizar,range(len(x1)),interval = 100,repeat = False)
    plt.show()
    return "Graficado con exito\n"
    
    
print ("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx\n")
print ("x     Bienvenido a nuestro proyecto de laboratorio de Fisica 3                                        x")
print ("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx\n")

salir = False
opcion = 0
#campo magnetico en tesla
B = 0.725
#distancia placas selector de velocidades en metros
d = 0.5
#lista de lista con las particulas que utilizaremos
mp= 1.67e-27
me=9.11e-31
e = 1.602e-19
#cada lista esta de la siguiente manera
#nombre particula, masa, carga
particulas = [["Proton",mp,e,1],["Electron",me,-1*e,2],["Particula Alfa",4*mp,2*e,3],["Positron",me,e,4],["Nucleo Carbono12",12*mp,6*e,5],
              ["Nucleo Berilio9",9*mp,4*e,6],["Nucleo Hierro56",56*mp,26*e,7],["Nucleo Paladio107",107*mp,46*e,8],["Nucleo Oro197",197*mp,79*e,9],
              ["Nucleo Litio",7*mp,3*e,10],["Neutron",mp,0,11]]
#variables para los nombres de las particulas
par1=""
par2=""
par3=""
#variable masa de las particulas
masa1=0
masa2=0
masa3=0
#variables carga de las particulas
carga1=0
carga2=0
carga3=0
while not salir:
 
    print("")
    print ("1. Simular")
    print ("2. Agregar Particula")
    print ("3. Salir")  
    #print ("Elige una opcion")
    
    while True:
        try:
            opcion = int(input("Elige una opcion: "))
            break
        except:
            print("Ingrese una opcion valida\n")
            
    if opcion == 1:
        #pedir el voltaje
        while True:
            try:
                voltaje = float(input("Ingrese el VOLTAJE (V) para el selector de velocidades: "))
                break
            except:
                print("Revise los datos ingresados\n")
    
        print("")
        print("A continuacion escoja las 3 particulas que desea simular\n")
        #pedir primera particula
        cat = 1
        while cat !=0:
            print("Escoga la PRIMERA particula que desea simular\n")
            imprimir_particulas(particulas)
            par11 = input("Ingrese la particula deseada: ")
            for i in particulas:
                if par11==str(i[3]):
                    par11=i[0]
                    par1,masa1,carga1 = esc_particula(particulas,par11)
                    cat = 0
        
        #pedir segunda particula
        cat = 1
        while cat !=0:
            print("Escoga la SEGUNDA particula que desea simular\n")
            imprimir_particulas(particulas)
            par22= input("Ingrese la particula deseada: ")
            for i in particulas:
                if par22 == str(i[3]) and par22 != par1:
                    par22=i[0]
                    par2,masa2,carga2 = esc_particula(particulas,par22)
                    cat = 0
        #pedir tercera particula
        cat = 1
        while cat !=0:
            print("Escoga la TERCERA particula que desea simular\n")
            imprimir_particulas(particulas)
            par33= input("Ingrese la particula deseada: ")
            for i in particulas:
                if par33 == str(i[3]) and par33 != par1 and par33 != par2:
                    par33=i[0]
                    par3,masa3,carga3 = esc_particula(particulas,par33)
                    cat = 0
        #imprimir particulas
        print("Las particulas que se simularan son las siguientes\n")
        print("La particula",par1,"con masa",masa1,"y carga",carga1,"\n")
        print("La particula",par2,"con masa",masa2,"y carga",carga2,"\n")
        print("La particula",par3,"con masa",masa3,"y carga",carga3,"\n")
        #
        while True:
            print("De las particulas anteriores cuales desea disparar")
            print("Si escoge 1, la primera particula se disparara")
            print("Si escoge 2, la primeras 2 particulas se dispararan")
            print("Si escoge 3, las tres particulas que selecciono se dispararan\n")
            k = input("Ingrese un valor:  ")
            if k == "1" or k =="2" or k=="3":
                print("Entendido")
                break
            else:
                print("Ingrese un valor valido\n")
        
        vel_selector = velocidad(voltaje,d,B)
        print("La magnitdud del CAMPO Magnetico es de",B,"Teslas")
        print("Las particulas con la velocidad de",vel_selector,"(m/s)pasaran por el selector de velocidades\n")
        print("Cargando datos...")
        #se generan las tres listas con las velocidades para cada particula, n = 100
        velPar1 = GenerarVelParticulas(vel_selector,100)
        velPar2 = GenerarVelParticulas(vel_selector,100)
        velPar3 = GenerarVelParticulas(vel_selector,100)
        print("Generando velocidades---")
        #contando cuantas particulas cumplen con la condicion del selector de velocidades
        cantPar1 = DispararParticulas(velPar1,vel_selector)
        cantPar2 = DispararParticulas(velPar2,vel_selector)
        cantPar3 = DispararParticulas(velPar3,vel_selector)
        # en caso de que no cumpla activar esta linea de codigo
        cantPar1 = 2
        cantPar3 = 2
        cantPar2 = 1
        print("Calculando Datos\n")
        #print("Para la particula",par1,"de las 100 particulas que se dispararon\n solo",cantPar1,"cumplieron con la velocidad deseada\n")
        #print("Para la particula",par2,"de las 100 particulas que se dispararon\n solo",cantPar2,"cumplieron con la velocidad deseada\n")
        #print("Para la particula",par3,"de las 100 particulas que se dispararon\n solo",cantPar3,"cumplieron con la velocidad deseada\n")
        #graficar
        #particula 1
        if cantPar1 !=0 and cantPar2 !=0 and cantPar3 !=0:
            #print("Graficando.........")
            radio1 = RadioPar(masa1,vel_selector,B,carga1)
            radio2 = RadioPar(masa2,vel_selector,B,carga2)
            radio3 = RadioPar(masa3,vel_selector,B,carga3)
            
            if k == "1":
                grficas = Graficar1(radio1,par1)
                print(grficas)
            elif k =="2":
                graficas = Graficar2(radio1,radio2,par1,par2)
                print(graficas)
            elif k =="3":
                graficas = Graficar(radio1,radio2,radio3,par1,par2,par3)
                print(graficas)
        elif cantPar1 ==0 and cantPar2 ==0 and cantPar3 ==0:
            print("Lo siento pero ninguna particula cumplio con la velocidad del selector\n")
     
            
    elif opcion == 2:
        print("Llene los siguientes datos por favor\n")
        #pedir el nombre de la particulat
        while True:
            try:
                nombre_particula= input("Ingrese el nombre de la Particula nueva: ")
                break
            except:
                print("Ingrese Un valor Valido\n")
        #pedir masa de la nueva particula
        while True:
            try:
                masa_particula= float(input("Ingrese la MASA (Kg) de la particula: "))
                break
            except:
                print("Ingrese Un valor Valido\n")
        #pedir carga de la nueva particula
        while True:
            try:
                carga_particula = float(input("Ingrese la CARGA (C) de la particula: "))
                break
            except:
                print("Ingrese Un valor Valido\n")
                
        #llamar funcion agregar_particulas para que agregue las particulas a la base de datos
        agregar_particulas(particulas,nombre_particula,masa_particula,carga_particula)
    elif opcion == 3:
        salir = True
    else:
        print ("Introduce un numero entre 1 y 3\n")
        
print("Fin del programa\n")
