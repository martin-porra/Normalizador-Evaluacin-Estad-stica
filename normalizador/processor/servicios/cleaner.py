import unicodedata
import re
import pandas as pd 

def limpiar_texto(texto):

    texto = str(texto)

    # eliminar acentos y todo lo que no sea ascii: ñ -> n
    texto = unicodedata.normalize("NFD", texto)
    texto = texto.encode("ascii", "ignore").decode("utf-8")

    #eliminar caracteres especiales (deja numeros, letras y espacios)
    #texto = re.sub(r"[^a-zA-Z0-9\s]", "", texto)

    return texto


def limpiar_dataframe(df):

    df = df.map(limpiar_texto)

    return df