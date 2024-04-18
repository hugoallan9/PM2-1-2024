from django.urls import path
from polls import views

urlpatterns = [path("<int:question_id>/", views.detail, name="detail"),
    # ex: /polls/5/results/
    path("<int:question_id>/results/", views.results, name="results"),
    # ex: /polls/5/vote/
    path("<int:question_id>/vote/", views.vote, name="vote"),
    path("crear-pregunta", views.crear_pregunta_vista, name="crear-pregunta-vista"),
    path("crear-respuesta/<int:pk_pregunta>/<int:numero_respuestas>", views.crear_respuestas_vista, name="crear-respuesta"),
               ]
