# MATG1052 - Análisis Numérico ver 2019/05/29
# Resumen de problemas resueltos
# en clases /ESPOL/FCNM/MATG1013
# Blog: http://blog.espol.edu.ec/analisisnumerico
# propuesta: Edison Del Rosario
#            edelros@espol.edu.ec
# funciones en python en proceso de desarrollo
# contiene TAREAS para completar casos en cada algoritmo

# con el archivo en el directorio de trabajo, use:
# import mat1052 as fcnm

import numpy as np
import sympy as sym

# Unidad 01 Polinomio de Taylor

def politaylor(funcionx,x0,n):
    '''
    Calcula n términos del polinomio de Taylor
    funcionx es simbólica
    resultado en forma simbólica
    '''
    i = 0
    polinomio = 0
    while (i <= n):
        derivada   = funcionx.diff(x,i)
        derivadax0 = derivada.subs(x,x0)
        divisor = np.math.factorial(i)
        terminoi = (derivadax0/divisor)*(x-x0)**i
        polinomio = polinomio + terminoi
        i = i + 1
    return(polinomio)

# Unidad 02 - Raíces de funciones
# funcionx es tipo lambda
def biseccion(funcionx,a,b,tolera):
    '''
    Algoritmo de Bisección
    Los valores de [a,b] son seleccionados
    desde la gráfica de la función
    error = tolera
    '''
    fa = funcionx(a)
    fb = funcionx(b)
   
    tramo = np.abs(b-a)
    while (tramo>=tolera):
        c = (a+b)/2
        fc = funcionx(c)
        cambia = np.sign(fa)*np.sign(fc)
        if (cambia<0):
            b = c
            fb = fc
        else:
            a = c
            fa = fc
        tramo = np.abs(b-a)
    return(c)

def newton_raphson(funcionx, fxderiva, xi, tolera):
    '''
    funciónx y fxderiva son de forma numérica
    xi es el punto inicial de búsqueda
    '''
    tramo = abs(2*tolera)
    while (tramo>=tolera):
        xnuevo = xi - funcionx(xi)/fxderiva(xi)
        tramo = abs(xnuevo-xi)
        xi = xnuevo
    return(xi)

def puntofijo(gx,a,tolera, n = 15):
    """
    g(x) se obtiene al despejar una x de f(x)
    máximo de iteraciones predeterminado: n
    si no converge hasta n iteraciones
    la respuesta es NaN
    """
    i = 1
    b = gx(a)
    tramo = abs(b-a)
    while(tramo>=tolera and i<=n):
        a = b
        b = gx(a)
        tramo = abs(b-a)
        i = i+1
    respuesta = b
    # Valida respuesta
    if (i>=n):
        respuesta = np.nan
    return(respuesta)

def posicionfalsa(fx,a,b,tolera):
    '''
    Algoritmo de Posición Falsa
    Los valores de [a,b] son seleccionados
    desde la gráfica de la función
    error = tolera
    '''
    fa = fx(a)
    fb = fx(b)
    c = b - fb*(a-b)/(fa-fb)
    
    tramo = abs(b-a)
    while (tramo > tolera):
        fc = fx(c)
        cambia = np.sign(fa)*np.sign(fc)
        if (cambia > 0):
            tramo = abs(c-a)
            a = c
            fa = fc
        else:
            tramo = abs(c-b)
            b = c
            fb = fc
        c = b - fb*(a-b)/(fa-fb)

    respuesta = c
    
    # Valida respuesta
    fa = fx(a)
    fb = fx(b)
    cambio = np.sign(fa)*np.sign(fb)
    if (cambio>0):
        respuesta = np.nan
        
    return(respuesta)

# Unidad 03 - Sistemas de ecuaciones. Métodos directos
def gauss(A,B, casicero = 1e-15):
    '''
    algoritmo de Gauss para sistemas de ecuaciones
    casicero es usado para comparar celdas cero
    Supone que A y B tienen igual numero de filas
    B llega en forma de columna
    Tarea: diagonal con ceros
    '''
    AB = np.concatenate((A,B),axis=1)
    tamano = np.shape(AB)
    n = tamano[0]
    m = tamano[1]
    # Gauss elimina hacia adelante
    # tarea: verificar términos cero
    for i in range(0,n,1):
        pivote = AB[i,i]
        adelante = i+1 
        for k in range(adelante,n,1):
            if (np.abs(pivote)>=casicero):
                factor = AB[k,i]/pivote
                AB[k,:] = AB[k,:] - factor*AB[i,:]
            else:
                factor= 'division para cero'

    # Sustitución hacia atras
    X = np.zeros(n,dtype=float) 
    ultfila = n-1
    ultcolumna = m-1
    for i in range(ultfila,0-1,-1):
        suma = 0
        for j in range(i+1,ultcolumna,1):
            suma = suma + AB[i,j]*X[j]
        X[i] = (AB[i,ultcolumna]-suma)/AB[i,i]
    X = np.transpose([X])
    return(X)

def gauss_jordan(A,B, casicero = 1e-15):
    '''
    Algoritmo de Gauss-Jordan para sistemas de ecuaciones
    casicero es usado para comparar celdas cero
    Supone que A y B tienen igual numero de filas
    B llega en forma de columna
    Tarea: diagonal con ceros
    '''
    # Matriz aumentada
    AB = np.concatenate((A,B), axis=1)
    # Gauss elimina hacia adelante
    tamano = np.shape(AB)
    n = tamano[0]
    m = tamano[1]
    for i in range(0,n,1):
        pivote = AB[i,i]
        adelante = i+1 
        for k in range(adelante,n,1):
            if (np.abs(pivote)>=casicero):
                factor = AB[k,i]/pivote
                AB[k,:] = AB[k,:] - factor*AB[i,:]
            else:
                factor= 'division para cero'
    # Gauss-Jordan elimina hacia atras
    ultfila = n-1
    ultcolumna = m-1
    for i in range(ultfila,0-1,-1):
        # Normaliza fila, a 1 elemento diagonal
        AB[i,:] = AB[i,:]/AB[i,i]
        pivote = AB[i,i] # uno
        # arriba de la fila i
        atras = i-1 
        for k in range(atras,0-1,-1):
            if (np.abs(AB[k,i])>=casicero):
                factor = pivote/AB[k,i]
                AB[k,:] = AB[k,:]*factor - AB[i,:]
            else:
                factor = 'division para cero'
    X = AB[:,ultcolumna]
    X = np.transpose([X])
    return(X)

def gauss_eliminaAdelante(AB, casicero = 1e-15):
    '''
    Gauss elimina hacia adelante
    tarea: verificar términos cero
    '''
    tamano = np.shape(AB)
    n = tamano[0]
    m = tamano[1]
    for i in range(0,n,1):
        pivote = AB[i,i]
        adelante = i+1 
        for k in range(adelante,n,1):
            if (np.abs(pivote)>=casicero):
                factor = AB[k,i]/pivote
                AB[k,:] = AB[k,:] - factor*AB[i,:]
            else:
                factor= 'division para cero'
    return(AB)

def gauss_eliminaAtras(AB, casicero = 1e-15):
    '''
    Requiere la matriz triangular inferior
    Tarea: Verificar que sea triangular inferior
    Gauss-Jordan elimina hacia atras
    '''
    tamano = np.shape(AB)
    n = tamano[0]
    m = tamano[1]

    ultfila = n-1
    ultcolumna = m-1
    for i in range(ultfila,0-1,-1):
        # Normaliza a 1 elemento diagonal
        AB[i,:] = AB[i,:]/AB[i,i]
        pivote = AB[i,i] # uno
        # arriba de la fila i
        atras = i-1 
        for k in range(atras,0-1,-1):
            if (np.abs(AB[k,i])>=casicero):
                factor = pivote/AB[k,i]
                AB[k,:] = AB[k,:]*factor - AB[i,:]
            else:
                factor= 'division para cero'
    return(AB)

def pivoteafila(A):
    '''
    Pivotea parcial por filas
    Recibe la matriz A, copia en C para no modificar A
    Si hay ceros en diagonal, la matriz es singular,
    Tarea: Revisar si diagonal tiene ceros
    '''
    tamano = np.shape(A)
    n = tamano[0]
    m = tamano[1]
    C = np.copy(A)
    for i in range(0,n-1,1):
        # columna desde diagonal i en adelante
        columna = np.abs(C[i:,i])
        dondemax = np.argmax(columna)
        # revisa dondemax no está en la diagonal
        if (dondemax != 0):
            # intercambia fila
            temporal = np.copy(C[i,:])
            C[i,:] = C[dondemax+i,:]
            C[dondemax+i,:] = temporal
    return(C)

def inversa_gauss_jordan(A, casicero = 1e-15):
    '''
    inversa de A usando la matriz aumentada con la identidad
    liego aplica Gauss-Jordan
    '''
    tamano = np.shape(A)
    n = tamano[0]
    m = tamano[1]

    # Añade la matriz identidad
    identidad = np.identity(n)
    AI = np.concatenate((A,identidad), axis=1)
    m = 2*m

    # Gauss elimina hacia adelante
    AI = gauss_eliminaAdelante(AI)
    
    # Gauss-Jordan elimina hacia atras
    AI = gauss_eliminaAtras(AI)

    inversa = AI[:,n:]
    return(inversa)

def triang_LU(A, casicero = 1e-15):
    '''
    Triangulares de una matriz A=L.U
    Triangular inferior L = LU[0]
    Triangular superior U = LU[1]
    usa versión modificada de 
      elimina hacia adelante de Gauss-Jordan
    '''
    tamano = np.shape(A)
    n = tamano[0]
    m = tamano[1]

    U = np.copy(A)
    L = np.identity(n,dtype=float)

    # Gauss elimina hacia adelante
    # tarea: verificar términos cero
    for i in range(0,n,1):
        pivote = U[i,i]
        adelante = i+1 
        for k in range(adelante,n,1):
            if (np.abs(pivote)>=casicero):
                factor = U[k,i]/pivote
                U[k,:] = U[k,:] - factor*U[i,:]
                L[k,i] = factor

    LU = np.array([L,U])
    return(LU)

def norma_p(X,p):
    Xp = (np.abs(X))**p
    suma = np.sum(Xp)
    norma = suma**(1/p)
    return(norma)

def norma_euclidiana(X):
    norma = norma_p(X,2)
    return(norma)

def norma_filasum(X):
    sfila = np.sum(np.abs(X),axis=1)
    norma = np.max(sfila)
    return(norma)

def norma_frobenius(X):
    tamano = np.shape(X)
    n = tamano[0]
    m = tamano[1]
    norma = 0
    for i in range(0,n,1):
        for j in range(0,m,1):
            norma =  norma + np.abs(X[i,j])**2
    norma = np.sqrt(norma)
    return(norma)

def num_condicion(X):
    M = np.copy(X)
    Mi = np.linalg.inv(M)
    nM = norma_filasum(M)
    nMi= norma_filasum(Mi)
    ncondicion = nM*nMi
    return(ncondicion)

# UNIDAD 04 - Sistemas de ecuaciones. Métodos iterativos

def gauss_seidel(A,B,X,tolera, itermax=100):
    '''
    Algoritmo Gauss-Seidel,
    matrices, métodos iterativos
    ingresar iteramax si requiere más iteraciones
    Referencia: Chapra 11.2, p.310, pdf.334; Rodriguez 5.2 p.162
    Tarea:  verificar:
            diagonal dominante, no singular, converge
    '''
    tamano = np.shape(A)
    n = tamano[0]
    m = tamano[1]
    diferencia = np.ones(n, dtype=float)
    errado = np.max(diferencia)
    
    itera = 0
    while not(errado<=tolera or itera>iteramax):
        for i in range(0,n,1):
            nuevo = B[i]
            for j in range(0,m,1):
                if (i!=j): # excepto diagonal de A
                    nuevo = nuevo-A[i,j]*X[j]
            nuevo = nuevo/A[i,i]
            diferencia[i] = np.abs(nuevo-X[i])
            X[i] = nuevo
        errado = np.max(diferencia)
        itera = itera + 1
    # Vector en columna
    X =  np.transpose([X])
    # No converge
    if (itera>itermax):
        X=0
    return(X)

# UNIDAD 05 Interpolación
def dif_finitas(xi,fi):
    '''
    Genera la tabla de diferencias finitas
    resultado en: [título,tabla]
    Tarea: verificar tamaño de vectores
    '''
    # Tabla de diferencias finitas
    titulo = ['i','xi','fi']
    n = len(xi)
    # cambia a forma de columnas
    i = np.arange(1,n+1,1)
    i = np.transpose([i])
    xi = np.transpose([xi])
    fi = np.transpose([fi])
    # Añade matriz de diferencias
    dfinita = np.zeros(shape=(n,n),dtype=float)
    tabla = np.concatenate((i,xi,fi,dfinita), axis=1)
    # trabaja en tabla, por columnas
    [n,m] = np.shape(tabla)
    c = 3
    diagonal = n-1
    while (c<m):
        # Aumenta el título para cada columna
        titulo.append('df'+str(c-2))
        # calcula cada diferencia por fila
        f = 0
        while (f < diagonal):
            tabla[f,c] = tabla[f+1,c-1]-tabla[f,c-1]
            f = f+1
        diagonal = diagonal - 1
        c = c+1
    return([titulo,tabla])

def interpola_dfinitas(xi,fi):
    '''
    Interpolación de diferencias finitas avanzadas
    resultado: polinomio en forma simbólica
    '''
    # Tabla de diferencias finitas
    titulo = ['i','xi','fi']
    n = len(xi)
    # cambia a forma de columnas
    i = np.arange(1,n+1,1)
    i = np.transpose([i])
    xi = np.transpose([xi])
    fi = np.transpose([fi])
    # Añade matriz de diferencias
    dfinita = np.zeros(shape=(n,n),dtype=float)
    tabla = np.concatenate((i,xi,fi,dfinita), axis=1)
    # Sobre matriz de diferencias, por columnas
    [n,m] = np.shape(tabla)
    c = 3
    diagonal = n-1
    while (c<m):
        # Aumenta el título para cada columna
        titulo.append('df'+str(c-2))
        # calcula cada diferencia por fila
        f = 0
        while (f < diagonal):
            tabla[f,c] = tabla[f+1,c-1]-tabla[f,c-1]
            f = f+1
        
        diagonal = diagonal - 1
        c = c+1

    # POLINOMIO con diferencias finitas
    # caso: puntos en eje x equidistantes
    dfinita = tabla[:,3:]
    n = len(dfinita)
    x = sym.Symbol('x')
    h = xi[1,0]-xi[0,0]
    polinomio = fi[0,0]
    for c in range(1,n,1):
        denominador = np.math.factorial(c)*(h**c)
        factor = dfinita[0,c-1]/denominador
        termino=1
        for f  in range(0,c,1):
            termino = termino*(x-xi[f])
        polinomio = polinomio + termino*factor
    # simplifica polinomio, multiplica los (x-xi)
    polinomio = polinomio.expand()
    
    return(polinomio)

def interpola_lagrange(xi,yi):
    '''
    Interpolación con método de Lagrange
    resultado: polinomio en forma simbólica
    '''
    # PROCEDIMIENTO
    n = len(xi)
    x = sym.Symbol('x')
    # Polinomio
    polinomio = 0
    for i in range(0,n,1):
        # Termino de Lagrange
        termino = 1
        for j  in range(0,n,1):
            if (j!=i):
                termino = termino*(x-xi[j])/(xi[i]-xi[j])
        polinomio = polinomio + termino*yi[i]
    # Expande el polinomio
    polinomio = polinomio.expand()
    return(polinomio)

def traza3natural(xi,yi):
    '''
    Trazador cúbico natural, splines
    resultado: polinomio en forma simbólica
    '''
    n = len(xi)
    # Valores h
    h = np.zeros(n-1, dtype = float)
    for j in range(0,n-1,1):
        h[j] = xi[j+1] - xi[j]
    
    # Sistema de ecuaciones
    A = np.zeros(shape=(n-2,n-2), dtype = float)
    B = np.zeros(n-2, dtype = float)
    S = np.zeros(n, dtype = float)
    A[0,0] = 2*(h[0]+h[1])
    A[0,1] = h[1]
    B[0] = 6*((yi[2]-yi[1])/h[1] - (yi[1]-yi[0])/h[0])
    for i in range(1,n-3,1):
        A[i,i-1] = h[i]
        A[i,i] = 2*(h[i]+h[i+1])
        A[i,i+1] = h[i+1]
        B[i] = 6*((yi[i+2]-yi[i+1])/h[i+1] - (yi[i+1]-yi[i])/h[i])
    A[n-3,n-4] = h[n-3]
    A[n-3,n-3] = 2*(h[n-3]+h[n-2])
    B[n-3] = 6*((yi[n-1]-yi[n-2])/h[n-2] - (yi[n-2]-yi[n-3])/h[n-3])
    # Resolver sistema de ecuaciones
    r = np.linalg.solve(A,B)
    # S
    for j in range(1,n-1,1):
        S[j] = r[j-1]
    S[0] = 0
    S[n-1] = 0
    
    # Coeficientes
    a = np.zeros(n-1, dtype = float)
    b = np.zeros(n-1, dtype = float)
    c = np.zeros(n-1, dtype = float)
    d = np.zeros(n-1, dtype = float)
    for j in range(0,n-1,1):
        a[j] = (S[j+1]-S[j])/(6*h[j])
        b[j] = S[j]/2
        c[j] = (yi[j+1]-yi[j])/h[j] - (2*h[j]*S[j]+h[j]*S[j+1])/6
        d[j] = yi[j]
    
    # Polinomio trazador
    x = sym.Symbol('x')
    polinomio = []
    for j in range(0,n-1,1):
        ptramo = a[j]*(x-xi[j])**3 + b[j]*(x-xi[j])**2 + c[j]*(x-xi[j])+ d[j]
        ptramo = ptramo.expand()
        polinomio.append(ptramo)
    
    return(polinomio)

def mincuadrados(xi,yi):
    n=len(xi)
    sx = 0
    sy = 0
    sxy = 0
    sx2 = 0
    for i in range(0,n,1):
        sx = sx + xi[i]
        sy = sy + yi[i]
        sxy = sxy + xi[i]*yi[i]
        sx2 = sx2 + xi[i]**2
    a1 = (n*sxy - sx*sy)/(n*sx2-sx**2)
    a0 = sy/n - a1*sx/n
    a = [a0,a1]
    return(a)

# UNIDAD 07 Integración

def integratrapecio(funcionx,a,b,tramos):
    h = (b-a)/tramos
    x = a
    suma = funcionx(x)
    for i in range(0,tramos-1,1):
        x = x+h
        suma = suma + 2*funcionx(x)
    suma = suma + funcionx(b)
    area = h*(suma/2)
    return(area)

def integrasimpson13(funcionx,a,b,tramos):
    h = (b-a)/tramos
    x = a
    # segmento: por cada dos tramos
    suma = funcionx(x)
    for i in range(0,tramos-2,2):
        x = x + h
        suma = suma + 4*funcionx(x)
        x = x + h
        suma = suma + 2*funcionx(x)
    # último segmento 
    x= x + h
    suma = suma + 4*funcionx(x)
    suma = suma + funcionx(b)
    area = h*(suma/3)
    return(area)

def integraCuadGauss2p(funcionx,a,b):
    x0 = -1/np.sqrt(3)
    x1 = -x0
    xa = (b+a)/2 + (b-a)/2*(x0)
    xb = (b+a)/2 + (b-a)/2*(x1)
    area = ((b-a)/2)*(funcionx(xa) + funcionx(xb))
    return(area)

def edo_euler(d1y,x0,y0,h,muestras):
    # Aplicando Taylor 2 términos
    tamano = muestras + 1
    estimado = np.zeros(shape=(tamano,2),dtype=float)
    # incluye el punto [x0,y0]
    estimado[0] = [x0,y0]
    x = x0
    y = y0
    for i in range(1,tamano,1):
        y = y + h*d1y(x,y)
        x = x+h
        estimado[i] = [x,y]
    return(estimado)

def edo_taylor3t(d1y,d2y,x0,y0,h,muestras):
    # Aplicando Taylor 3 términos
    tamano = muestras + 1
    estimado = np.zeros(shape=(tamano,2),dtype=float)
    # incluye el punto [x0,y0]
    estimado[0] = [x0,y0]
    x = x0
    y = y0
    for i in range(1,tamano,1):
        y = y + h*d1y(x,y) + ((h**2)/2)*d2y(x,y)
        x = x+h
        estimado[i] = [x,y]
    return(estimado)

def rungekutta2(d1y,x0,y0,h,muestras):
    # Runge Kutta de 2do orden
    tamano = muestras + 1
    estimado = np.zeros(shape=(tamano,2),dtype=float)
    
    # incluye el punto [x0,y0]
    estimado[0] = [x0,y0]
    xi = x0
    yi = y0
    for i in range(1,tamano,1):
        K1 = h * d1y(xi,yi)
        K2 = h * d1y(xi+h, yi + K1)

        yi = yi + (1/2)*(K1+K2)
        xi = xi + h
        
        estimado[i] = [xi,yi]
    return(estimado)

def rungekutta4(d1y,x0,y0,h,muestras):
    # Runge Kutta de 4do orden
    tamano = muestras + 1
    estimado = np.zeros(shape=(tamano,2),dtype=float)
    
    # incluye el punto [x0,y0]
    estimado[0] = [x0,y0]
    xi = x0
    yi = y0
    for i in range(1,tamano,1):
        K1 = h * d1y(xi,yi)
        K2 = h * d1y(xi+h/2, yi + K1/2)
        K3 = h * d1y(xi+h/2, yi + K2/2)
        K4 = h * d1y(xi+h, yi + K3)

        yi = yi + (1/6)*(K1+2*K2+2*K3 +K4)
        xi = xi + h
        
        estimado[i] = [xi,yi]
    return(estimado)

