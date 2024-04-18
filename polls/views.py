from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Question, Choice
from django.template import loader
from .forms import crear_pregunta, crear_respuestas
from datetime import datetime


# Create your views here.
def home(request):
    return HttpResponse("Mi primer sitio web hola!!!!!!")


def detail(request, question_id):
    # question = Question.objects.get(pk=question_id)
    plantilla = loader.get_template('index.html')
    contexto = {'titulo': "Detalle de las preguntas", 'contenido': "Este es el ejemplo de uso de una plantilla"}
    return HttpResponse(plantilla.render(contexto, request))


def results(request, question_id):
    return HttpResponse("Estás viendo los resultados de la pregunta %s." % question_id)


def vote(request, question_id):
    return HttpResponse("Estás votando por la pregunta %s." % question_id)


def crear_pregunta_vista(request):
    if request.method == "POST":
        form = crear_pregunta(request.POST)
        if form.is_valid():
            texto_pregunta = form.cleaned_data['texto_pregunta']
            pregunta = Question(question_text=texto_pregunta, pub_date=datetime.now().strftime('%Y-%m-%d %H:%m'))
            pregunta.save()
            preguntas = Question.objects.all()
            pk = preguntas[len(preguntas)-1].pk
            return HttpResponseRedirect("crear-respuesta/" + str(pk) + "/" + str(form.cleaned_data['numero_opciones_respuesta']))
        else:
            print("La forma no es válida")
    else:
        form = crear_pregunta()
    return render( request, template_name='preguntas_test.html', context={'form':form})

def crear_respuestas_vista(request, pk_pregunta, numero_respuestas):
    if request.method == "POST":
        form = crear_respuestas(request.POST)
        if form.is_valid():
            respuesta1 = form.cleaned_data['respuesta1']
            respuesta2 = form.cleaned_data['respuesta2']
            respuesta3 = form.cleaned_data['respuesta3']
            respuesta4 = form.cleaned_data['respuesta4']
            pregunta = Question.objects.get(pk=pk_pregunta)
            op1 = Choice(question= pregunta, choice_text=respuesta1)
            op2 = Choice(question= pregunta, choice_text=respuesta2)
            op3 = Choice(question= pregunta, choice_text=respuesta3)
            op4 = Choice(question= pregunta, choice_text=respuesta4)
            op1.save()
            op2.save()
            op3.save()
            op4.save()
            HttpResponseRedirect('index.html')
    else:
        form = crear_respuestas()
    return render(request, template_name='opciones_respueta.html', context={'form':form})