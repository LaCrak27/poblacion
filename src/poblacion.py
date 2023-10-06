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
def lee_poblaciones(ruta_fichero: str) -> list:
    res = []
    with open(ruta_fichero, "rt") as f:
        reader = csv.reader(f)
        for pais, codigo, año, censo in reader:
            res.append(RegistroPoblacion(pais, codigo, año, censo))
    return res



def calcula_paises(poblaciones: list) -> list:
    res = []
    for element in poblaciones:
        if(res.__contains__(element.pais) == False):
            res.append(element.pais)
    return res
    """
    Calcula la lista de países distintos presentes en una lista de de tuplas de tipo RegistroPoblacion.

    @param poblaciones: lista de tuplas con información de poblaciones
    @type poblaciones: list(RegistroPoblacion)

    @return: lista de paises, ordenada alfabéticamente, sin duplicados
    @rtype: list(str)
    """


def filtra_por_pais(poblaciones:list, pais_o_codigo:str) -> list:
    res = []
    for element in poblaciones:
        if(element.codigo == pais_o_codigo) or (element.pais == pais_o_codigo):
            res.append((element.año, element.censo))
    return res

    """
    Devuelve el año y el censo de las tuplas correspondientes a un determinado pais

    @param poblaciones: lista de tuplas con información de poblaciones
    @type poblaciones: list(RegistroPoblacion)
    @param pais_o_codigo: nombre o código del país del que se seleccionarán los registros
    @type pais_o_codigo: str

    @return: lista de tuplas (año, censo) seleccionadas
    @rtype: list(tuple(int, int))
    """
##############################################################################################

##############################################################################################
def filtra_por_paises_y_anyo(poblaciones: list, año: int, paises: set) -> list:
    res = []
    for element in poblaciones:
        if(element.año == str(año)) and (paises.__contains__(element.pais)):
            res.append((element.pais, element.censo))
    return res
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
def muestra_evolucion_poblacion(poblaciones: list, pais_o_codigo: str):
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
    titulo = pais_o_codigo
    lista_años = []
    lista_habitantes = []
    pop_list = filtra_por_pais(poblaciones, pais_o_codigo)
    for element in pop_list:
        lista_años.append(int(element[0]))
        lista_habitantes.append(int(element[1]))
    # Estas instrucciones dibujan la gráfica
    plt.title(titulo)
    plt.plot(lista_años, lista_habitantes)
    plt.show()


###############################################################################################

###############################################################################################
def muestra_comparativa_paises_anyo(poblaciones: list, año: int, paises: list):
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
    titulo = año
    lista_paises = []
    lista_habitantes = []
    lista_año = filtra_por_paises_y_anyo(poblaciones, año, paises)
    for element in lista_año:
        lista_paises.append(element[0])
        lista_habitantes.append(int(element[1]))

    # Estas instrucciones dibujan la gráfica
    plt.title(titulo)
    plt.bar(lista_paises, lista_habitantes)
    plt.show()
