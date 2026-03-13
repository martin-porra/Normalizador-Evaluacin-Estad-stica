from django.shortcuts import render
from django.http import HttpResponse
import pandas as pd

def upload(request):

    if request.method == "POST":

        archivo = request.FILES["archivo"]

        if archivo.name.endswith(".csv"):
            df = pd.read_csv(archivo)

        elif archivo.name.endswith(".xlsx"):
            df = pd.read_excel(archivo)

        else:
            return render(request, "upload.html", {"error": "Formato no soportado"})

        tabla = df.head().to_html()

        return render(request, "upload.html", {"tabla": tabla})

    return render(request, "upload.html")