import pytest


#Skip o Marcas cambia el comportam de la funcion o metodo (como un decorador

@pytest.mark.skip(reason="lo que sea") #... asi no se ejecuta
def test_preba():
    assert 1==1

@pytest.mark.marca1    # etste test lo crea,os en el archivo  pytest.ini
def test_preba1():
    assert 1==1

# el terminal --- : pytest -m "marca1" (enter)


# fixture es una accion previa a ejecutar el test
@pytest.fixture()   #(scope="sessions") #indica que solo se ejecutaria en session x ej ... si no se pone nada en () se ejecutara directamente
def fixture_1():
    return 3   # si en vez de return se usa yield se ejecutara cualquien accion posterior 

def test_preba2(fixture_1):
    variable = fixture_1  #lo pasamos como parametro
    assert variable==3

# terminal : pytest -rP (da un detalle de los errores)

#python -m pytest tests OTRA FORMA DE TESTEAR
