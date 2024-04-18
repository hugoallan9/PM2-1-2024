from django import forms

class crear_pregunta(forms.Form):
    texto_pregunta = forms.CharField(label="Pregunta", max_length=100)
    numero_opciones_respuesta = forms.IntegerField(label = "Número de opciones de respuestas")

class crear_respuestas(forms.Form):
    respuesta1 = forms.CharField(label="Respuesta 1", max_length=100)
    respuesta2 = forms.CharField(label="Respuesta 2", max_length=100)
    respuesta3 = forms.CharField(label="Respuesta 3", max_length=100)
    respuesta4 = forms.CharField(label="Respuesta 4", max_length=100)
