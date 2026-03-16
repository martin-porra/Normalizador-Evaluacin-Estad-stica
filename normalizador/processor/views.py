from django.shortcuts import render, redirect
from django.http import HttpResponse
import pandas as pd
from .servicios.cleaner import limpiar_dataframe

def home(request):
     return redirect("upload")

def upload(request):

    if request.method == "POST":

        archivo = request.FILES.get("archivo")

        if not archivo:
            return render(request, "upload.html", {"error": "Selecciona un archivo"})
        
        if archivo.name.endswith(".csv"):
            df = pd.read_csv(archivo)

        elif archivo.name.endswith(".xlsx"):
            df = pd.read_excel(archivo)

        else:
            return render(request, "upload.html", {"error": "Formato no soportado"})
        
        tabla = limpiar_dataframe(df)
        tablapreview = tabla.head().to_html()

        request.session["data"] = tabla.to_csv(index=False)
        return render(request, "upload.html", {"tabla": tablapreview})
    
    return render(request, "upload.html")



def descargar(request):

    data = request.session.get("data")

    if not data:
        return HttpResponse("No hay archivo para descargar")

    response = HttpResponse(data, content_type="text/csv")

    response["Content-Disposition"] = 'attachment; filename="archivo_limpio.csv"'

    return response
    return render(request, "upload.html")

