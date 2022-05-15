from django.urls import path
from .views import DoktorView, PacientView, OddeliView, PreglediView, HospitalizacijaView




urlpatterns=[

    path("doktor/", DoktorView.as_view()),
    path("pacient/", PacientView.as_view()),
    path("oddel/", OddeliView.as_view()),
    path("pregled/", PreglediView.as_view()),
    path("hospitalizacija/", HospitalizacijaView.as_view())


 

]