import pytest
import csv
import config
from DataStructures import listiterator as it
from DataStructures import liststructure as lt

def newList (datastructure='SINGLE_LINKED', cmpfunction=None):
    """Crea una lista vacia.

    Args:
        cmpfunction: Función de comparación para los elementos de la lista
    Returns:
        Una nueva lista
    Raises:
        Exception
    """
    try:
        lst = lt.newList(datastructure, cmpfunction)
        return lst
    except Exception as exp:
        error.reraise (exp, 'TADList->newList: ')
        
def test_carga():
    lista = []
    lst = lt.newList()

    file = "Data\theMoviesdb\MoviesCastingRaw-small.csv"
    sep= ";"
    dialect = csv.excel()
    dialect.delimiter = sep

    assert(lt.size(lst)==0), "la lista no empieza en cero" 

    try:
        with open(file,enconding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile,dialect=dialect)

            for row in reader:
                lista.append(row)
                lt.addLast(lst,row)
    except:
        assert False, "Se presento un error al cargar el archivo"

    assert len(lista) == lt.size(lst), "son diferentes tamaños"

    for i in range (len(lista)):
        assert lt.getElement(lst,i+1)==lista[i], "las listas no estan en el mismo orden"