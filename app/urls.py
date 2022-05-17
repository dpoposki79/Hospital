from django.urls import path
from .views import DoktorView, PacientView, OddeliView, PreglediView, HospitalizacijaView, Home
#from allauth.socialaccount.providers.github import views as github_views




urlpatterns=[

    path("doktor/", DoktorView.as_view()),
    path("pacient/", PacientView.as_view()),
    path("oddel/", OddeliView.as_view()),
    path("pregled/", PreglediView.as_view()),
    path("hospitalizacija/", HospitalizacijaView.as_view()),
#    path ("github/", GithubConnect.as_view),
#    path ("github/auth/", github_views.oauth2_login),
#    path ("homepage/", home, name="home"),
    path('', Home.as_view(), name='home')



 

]