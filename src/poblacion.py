# -*- coding: utf-8 -*-

""" 
Poblacion mundial
@author: Toñi Reina
REVISOR: José Antonio Troyano, Daniel Mateos, Mariano González, Fermín Cruz
ÚLTIMA MODIFICACIÓN: 10/10/2022
"""

import csv
from matplotlib import pyplot as plt
from collections import namedtuple

RegistroPoblacion = namedtuple("RegistroPoblacion", "pais, codigo, año, censo")

############################################################################################
def lee_poblaciones(ruta_fichero):
    """
    Lee el fichero de entrada y devuelve una lista de tuplas poblaciones

    @param fichero: nombre del fichero de entrada
    @type fichero: str

    @return: lista de tuplas con la información del fichero
    @rtype: RegistroPoblacion
    """
    pass


def calcula_paises(poblaciones):
    """
    Calcula la lista de países distintos presentes en una lista de de tuplas de tipo RegistroPoblacion.

    @param poblaciones: lista de tuplas con información de poblaciones
    @type poblaciones: list(RegistroPoblacion)

    @return: lista de paises, ordenada alfabéticamente, sin duplicados
    @rtype: list(str)
    """
    pass


def filtra_por_pais(poblaciones, pais_o_codigo):
    """
    Devuelve el año y el censo de las tuplas correspondientes a un determinado pais

    @param poblaciones: lista de tuplas con información de poblaciones
    @type poblaciones: list(RegistroPoblacion)
    @param pais_o_codigo: nombre o código del país del que se seleccionarán los registros
    @type pais_o_codigo: str

    @return: lista de tuplas (año, censo) seleccionadas
    @rtype: list(tuple(int, int))
    """
    pass


##############################################################################################

##############################################################################################
def filtra_por_paises_y_anyo(poblaciones, año, paises):
    """
    Devuelve el país y el censo de las tuplas correspondientes a un conjunto de paises de un año concreto.

    @param poblaciones: lista de tuplas con información de poblaciones
    @type poblaciones: list(RegistroPoblacion)
    @param año: año del que se seleccionarán los registros
    @type año: int
    @param paises: conjunto de nombres de países de los que se seleccionarán los registros
    @type paises: set(str)

    @return: lista de tuplas (pais, censo) seleccionadas
    @rtype: list(tuple(str,int))
    """
    pass


##############################################################################################

###############################################################################################
def muestra_evolucion_poblacion(poblaciones, pais_o_codigo):
    """
    Genera una curva con la evolución de la población de un país. El país puede
    darse como su nombre completo o por su código.

    @param poblaciones: lista de tuplas con información de poblaciones
    @type poblaciones: list(RegistroPoblacion)
    @param pais_o_codigo: nombre o código del país del que se generará la gráfica
    @type pais_o_codigo: str
    """
    # TODO Complete la función para asignar los valores correctos
    #  a las variables titulo, lista_años y lista_habitantes
    titulo = ""
    lista_años = []
    lista_habitantes = []

    # Estas instrucciones dibujan la gráfica
    plt.title(titulo)
    plt.plot(lista_años, lista_habitantes)
    plt.show()


###############################################################################################

###############################################################################################
def muestra_comparativa_paises_anyo(poblaciones, año, paises):
    """
    Genera una gráfica de barras en la que se muestra la comparativa de
    la población de varios países en un año concreto

    @param poblaciones: lista de tuplas con información de poblaciones
    @type poblaciones: list(RegistroPoblacion)
    @param año: del que se generará la gráfica
    @type año: int
    @param paises: nombres de los países para los que se generará la gráfica
    @type paises: list(str)
    """
    # TODO Complete la función para asignar los valores correctos
    #  a las variables titulo, lista_paises y lista_habitantes
    titulo = ""
    lista_paises = []
    lista_habitantes = []

    # Estas instrucciones dibujan la gráfica
    plt.title(titulo)
    plt.bar(lista_paises, lista_habitantes)
    plt.show()
