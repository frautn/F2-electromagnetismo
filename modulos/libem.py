# This work © 2024 by Edgardo Palazzo (epalazzo@fra.utn.edu.ar)
# is licensed under CC BY-NC-SA 4.0

# Librería de funciones para cálculos sencillos de electromagnetismo.

import numpy as np
import matplotlib.pyplot as plt


# TODO: Return axs, add
# more control over plotting parameters.
# Add examples in the docstring.
def plotE(E, dx, **params):
    """
    Muestra las líneas de campo en 2D.

    Parameters
    ----------
    E : function
        Una función de un campo vectorial (3 variables que devuelve 3 componentes).
    dx : float
        Se produce una grilla con -dx <= x <= dx. Si dy = 0,
        se usan los mismos intervalos para esa variable: -dx <= y <= dx.
    dy : float (opcional)
        La grilla puede tener distintas dimensiones en cada eje.
    w : integer (opcional)
        Cantidad de particiones de cada dimensión en la grilla.

    *Además de los parámetros de matplotlib y streamplot, por ejemplo:*
    figsize : tuple
    title : string
    """

    dy = params.get('dy', 0)
    w = params.get('w', 100)

    figsize = params.get('figsize', (4,4))
    title = params.get('title', 'Líneas de campo')
    linewidth = params.get('linewidth', 0.4)
    density = params.get('density', 0.7)

    # Convirtiendo w a número complejo se incluye el extremo del intervalo en mgrid.
    w = w * 1j
    if (dy==0):
        dy = dx
    Y, X = np.mgrid[-dx:dx:w, -dy:dy:w]
    Z = 0*X
    Ei, Ej, Ek = E(X,Y,Z)

    fig, axs = plt.subplots(1, 1, figsize=figsize)

    strm = axs.streamplot(X, Y, Ei, Ej, color='b',
                        linewidth=linewidth, density=density)
    axs.set_title(title)
    axs.set_xlabel('$x$ [m]')
    axs.set_ylabel('$y$ [m]')


# TODO: Return axs, add
# more control over plotting parameters.
# Add examples in the docstring.
def plotEf(Ef, Q, dx, **params):
    """
    Muestra las líneas de campo en 2D.

    Parameters
    ----------
    Ef : function
        Una función de un campo vectorial (3 variables que devuelve 3 componentes).
    Q : list
        Q = [
            [q1,x1,y1,z1],
            [q2,x2,y2,z2],
            ...
            [qN,xN,yN,zN]
        ]
    dx : float
        Se produce una grilla con -dx <= x <= dx. Si dy = 0,
        se usan los mismos intervalos para esa variable: -dx <= y <= dx.
    dy : float (opcional)
        La grilla puede tener distintas dimensiones en cada eje.
    w : integer (opcional)
        Cantidad de particiones de cada dimensión en la grilla.

    *Además de los parámetros de matplotlib y streamplot, por ejemplo:*
    figsize : tuple
    title : string
    """

    dy = params.get('dy', 0)
    w = params.get('w', 100)

    figsize = params.get('figsize', (4,4))
    title = params.get('title', 'Líneas de campo')
    linewidth = params.get('linewidth', 0.4)
    density = params.get('density', 0.7)

    # Convirtiendo w a número complejo se incluye el extremo del intervalo en mgrid.
    w = w * 1j
    if (dy==0):
        dy = dx
    Y, X = np.mgrid[-dx:dx:w, -dy:dy:w]
    Z = 0*X

    Ei, Ej, Ek = Ef(X,Y,Z,Q)

    fig, axs = plt.subplots(1, 1, figsize=figsize)
    strm = axs.streamplot(X, Y, Ei, Ej, color='b',
                        linewidth=linewidth, density=density)
    for q in Q:
        qq, xq, yq, zq = q
        if qq > 0:
            colorq = 'red'
        else :
            colorq = 'green'
        circ = plt.Circle((xq,yq), dx*0.02, color=colorq)
        axs.add_patch(circ)
    axs.set_title(title)
    axs.set_xlabel('$x$ [m]')
    axs.set_ylabel('$y$ [m]')
    plt.grid()


#TODO: add 3d version.
def plotEfcontribuciones(Ef, Q, x, **params):
    """
    Muestra los vectores de cada porción de un cuerpo extenso, ¡en 2D!
    (no usar este código si las cargas están distribuidas en 3D).

    Parameters
    ----------
    Ef : function
        Una función de un campo vectorial (3 variables que devuelve 3 componentes).
    Q : list
        Q = [
            [q1,x1,y1,z1],
            [q2,x2,y2,z2],
            ...
            [qN,xN,yN,zN]
        ]
    X : tuple
        Posición donde se calcula el campo.
    limites : tuple
        Lmites de los ejes: [xmin, xmax, ymin, ymax]
    scale : float
        Regula la longitud de las flechas.
    r : float
        Radio de las partículas cargadas.
    linewidth : float
        Grosor de las líneas que muestran la dirección.
    in3D : bool
        If True, it produces a 3D graph.

    *Además de los parámetros de matplotlib y quiver, por ejemplo:*
    length : float
    figsize : tuple
    title : string
    """

    figsize = params.get('figsize', (5,5))
    title = params.get('title', "Contribuciones al campo eléctrico total")
    scale = params.get('scale', 1)
    linewidth = params.get('linewidth', 0.5)
    in3D = params.get('in3D', False)

    xmin, xmax, ymin, ymax, zmin, zmax = x[0],x[0],x[1],x[1], x[2], x[2]
    x_pos = []
    y_pos = []
    z_pos = []
    Ei = []
    Ej = []
    Ek = []
    modulos = []
    for q in Q:
        Eii, Ejj, Ekk = Ef(x[0],x[1],x[2],[q])
        # Elige límites para cuando el parámetro límites no es informado.
        if q[1] > xmax:
            xmax = q[1]
        if q[1] < xmin:
            xmin = q[1]
        if q[2] > ymax:
            ymax = q[2]
        if q[2] < ymin:
            ymin = q[2]
        if q[3] > zmax:
            zmax = q[3]
        if q[3] < zmin:
            zmin = q[3]
        x_pos = np.concatenate((x_pos,x[0]), axis=None)
        y_pos = np.concatenate((y_pos,x[1]), axis=None)
        z_pos = np.concatenate((z_pos,x[2]), axis=None)
        modulo = np.sqrt(Eii**2 + Ejj**2 + Ekk**2)
        modulos = np.concatenate((modulos, modulo), axis=None)
        Ei = np.concatenate((Ei, Eii), axis=None)
        Ej = np.concatenate((Ej, Ejj), axis=None)
        Ek = np.concatenate((Ek, Ekk), axis=None)

    # Se expanden los límites automáticos:
    xmax = xmax + (xmax - xmin)*0.2
    xmin = xmin - (xmax - xmin)*0.2
    ymax = ymax + (ymax - ymin)*0.2
    ymin = ymin - (ymax - ymin)*0.2
    zmax = zmax + (zmax - zmin)*0.2
    zmin = zmin - (zmax - zmin)*0.2

    rm = np.max(np.sqrt((xmax-xmin)**2 + (ymax-ymin)**2 + (zmax-zmin)**2))*0.01
    r = params.get('r', rm)

    Ei = np.round(Ei/np.max(modulos),3)
    Ej = np.round(Ej/np.max(modulos),3)
    Ek = np.round(Ek/np.max(modulos),3)

    if in3D:
        limites = params.get('limites', [xmin,xmax,ymin,ymax, zmin, zmax])
    else:
        limites = params.get('limites', [xmin,xmax,ymin,ymax])

    arrwidth = params.get('arrwidth', 0.005*(limites[1]-limites[0]))
    
    # Creating plot
    if in3D:
        pass
    else:
        fig, ax = plt.subplots(figsize = figsize)

        # ax.quiver(x_pos, y_pos, Ei, Ej, angles='xy', scale_units='xy', scale=scale)
        ax.quiver(x_pos, y_pos, Ei, Ej, scale=scale, width=arrwidth)

        # Necesito un for separado para determinar el tamaño de los círculos.
        for q in Q:
            qq, xq, yq, zq = q
            ax.plot([xq,x[0]], [yq,x[1]], color='b', linewidth=linewidth, linestyle='dashed')
            if qq > 0:
                colorq = 'red'
            else :
                colorq = 'green'
            circ = plt.Circle((xq,yq), r, color=colorq)
            ax.add_patch(circ)
        # ax.set_title(title)
        ax.set_xlabel('$x$ [m]')
        ax.set_ylabel('$y$ [m]')

    ax.axis(limites)
    ax.set_title(title)
    plt.show()
    # plt.close()

def plotEfvector(Ef, Q, X, **params):
    """
    Muestra las vectores del campo en 2D usando pyplot.quiver.

    Parameters
    ----------
    Ef : function
        Una función de un campo vectorial (3 variables que devuelve 3 componentes).
    Q : list
        Q = [
            [q1,x1,y1,z1],
            [q2,x2,y2,z2],
            ...
            [qN,xN,yN,zN]
        ]
    X : tuple
        Posiciones donde se calcula el campo.
    limites : tuple
        Lmites de los ejes: [xmin, xmax, ymin, ymax]
    scale : float
        Regula la longitud de las flechas.

    *Además de los parámetros de matplotlib y quiver, por ejemplo:*
    length : float
    figsize : tuple
    title : string
    """

    figsize = params.get('figsize', (5,5))
    title = params.get('title', "Algunos vectores de campo eléctrico")
    scale = params.get('scale', 1)

    xmin, xmax, ymin, ymax = 0,0,0,0
    x_pos = []
    y_pos = []
    Ei = []
    Ej = []
    for x in X:
        Eii, Ejj, Ekk = Ef(x[0],x[1],x[2],Q)

        # Elige límites para cuando el parámetro límites no es informado.
        if x[0] > xmax:
            xmax = x[0]
        if x[0] < xmin:
            xmin = x[0]
        if x[1] > ymax:
            ymax = x[1]
        if x[1] < ymin:
            ymin = x[1]
        x_pos = np.concatenate((x_pos,x[0]), axis=None)
        y_pos = np.concatenate((y_pos,x[1]), axis=None)
        N = np.sqrt(Eii**2 + Ejj**2)*1.5
        Ei = np.concatenate((Ei, Eii/N), axis=None)
        Ej = np.concatenate((Ej, Ejj/N), axis=None)

    # Creating plot
    fig, ax = plt.subplots(figsize = figsize)
    ax.quiver(x_pos, y_pos, Ei, Ej, angles='xy', scale_units='xy', scale=scale)

    for q in Q:
        qq, xq, yq, zq = q
        # Elige límites para cuando el parámetro límites no es informado.
        if xq > xmax:
            xmax = xq
        if xq < xmin:
            xmin = xq
        if yq > ymax:
            ymax = yq
        if yq < ymin:
            ymin = yq

        if qq > 0:
            colorq = 'red'
        else :
            colorq = 'green'
        circ = plt.Circle((xq,yq), np.max(np.abs(X))*0.02, color=colorq)
        ax.add_patch(circ)
    # ax.set_title(title)
    ax.set_xlabel('$x$ [m]')
    ax.set_ylabel('$y$ [m]')

    # Se expanden los límites automáticos:
    xmax = xmax + (xmax - xmin)*0.2
    xmin = xmin - (xmax - xmin)*0.2
    ymax = ymax + (ymax - ymin)*0.2
    ymin = ymin - (ymax - ymin)*0.2

    limites = params.get('limites', [xmin,xmax,ymin,ymax])
    ax.axis(limites)
    ax.set_title(title)
    plt.show()
    # plt.close()


def plotEfvector3d(Ef, Q, dx, **params):
    """
    Muestra las vectores del campo en 3D usando pyplot.quiver.

    Parameters
    ----------
    Ef : function
        Una función de un campo vectorial (3 variables que devuelve 3 componentes).
    Q : list
        Q = [
            [q1,x1,y1,z1],
            [q2,x2,y2,z2],
            ...
            [qN,xN,yN,zN]
        ]
    dx : float
        Se produce una grilla con -dx <= x <= dx. Si dy = 0,
        se usan los mismos intervalos para esa variable: -dx <= y <= dx.
    dy : float (opcional)
        La grilla puede tener distintas dimensiones en cada eje.
    w : integer (opcional)
        Cantidad de particiones de cada dimensión en la grilla.

    *Además de los parámetros de matplotlib y quiver, por ejemplo:*
    length : float
    figsize : tuple
    title : string
    """

    dy = params.get('dy', 0)
    w = params.get('w', 100)
    length = params.get('length', dx * 0.15)

    figsize = params.get('figsize', (4,4))
    title = params.get('title', 'Campo eléctrico')
    linewidth = params.get('linewidth', 0.4)

    # Convirtiendo w a número complejo se incluye el extremo del intervalo en mgrid.
    w = w * 1j
    if (dy==0):
        dy = dx
        dz = dx
    X, Y, Z = np.mgrid[-dx:dx:w, -dy:dy:w, -dz:dz:w]

    Ei, Ej, Ek = Ef(X,Y,Z,Q)

    fig, axs = plt.subplots(1, 1, figsize=figsize)
    axs = fig.add_subplot(projection='3d')
    axs.quiver(X, Y, Z, Ei, Ej, Ek, length=length, normalize=True)

    # Graficar las cargas.
    u = np.linspace(0, 2 * np.pi, 100)
    v = np.linspace(0, np.pi, 100)
    xc = dx * 0.04 * np.outer(np.cos(u), np.sin(v))
    yc = dx * 0.04 * np.outer(np.sin(u), np.sin(v))
    zc = dx * 0.04 * np.outer(np.ones(np.size(u)), np.cos(v))

    for q in Q:
        qq, xq, yq, zq = q
        if qq > 0:
            colorq = 'red'
        else :
            colorq = 'green'
        axs.plot_surface(xc + xq, yc + yq, zc + zq, color=colorq)
    axs.set_title(title)
    axs.set_xlabel('$x$ [m]')
    axs.set_ylabel('$y$ [m]')
    plt.grid()
