from sys import prefix
from django.shortcuts import render
from .models import Doktori, Pacienti, Oddeli, Pregledi, Hospitalizacija
from rest_framework.response import Response
from .serializers import DoktoriSerilizer, PacientiSerilizer, OddeliSerilizer, PreglediSerilizer, HospitalizacijaSerilizer
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.permissions import IsAuthenticated



class DoktorView(APIView):
    permission_classes = (IsAuthenticated,) #za najava t.e. logiranje
#zemanje podatoci samo za eden doktor
    def get (self, request):
        doktor=Doktori.objects.get(id=request.GET["doktorId"])
        doktor_serializer = DoktoriSerilizer(doktor)
        return Response(doktor_serializer.data)

    def post (self, request):
        doktor_serializer = DoktoriSerilizer(data=request.data)
        if doktor_serializer.is_valid():
            doktor_serializer.save()
            return Response(doktor_serializer.data, status=status.HTTP_201_CREATED)
        return Response ({"Info" : "Nastana greska"}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request):
        doktor = Doktori.objects.get(id=request.GET["doktorId"])
        doktor.delete()
        return Response ({"Info" : "Dokotorot e izbrisan"})

    def patch(self, request):
        doktor = Doktori.objects.get(id = request.data['id'])
        doktor_serializer = DoktoriSerilizer(doktor, data=request.data)
        if doktor_serializer.is_valid():
            doktor_serializer.save()
            return Response (doktor_serializer.data, status=status.HTTP_201_CREATED)
        return Response({"Errors": doktor_serializer.errors})
    
 

class PacientView(APIView):
    permission_classes = (IsAuthenticated,)
#zemanje podatoci sao za eden pacient
    def get (self, request):
        pacient=Pacienti.objects.get(id=request.GET["pacientId"])
        pacient_serializer = PacientiSerilizer(pacient)
        return Response(pacient_serializer.data)

    def post (self, request):
        pacient_serializer = PacientiSerilizer(data=request.data)
        if pacient_serializer.is_valid():
            pacient_serializer.save()
            return Response(pacient_serializer.data, status=status.HTTP_201_CREATED)
        return Response ({"Info" : "Nastana greska"}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request):
        pacient = Pacienti.objects.get(id=request.GET["pacientId"])
        pacient.delete()
        return Response ({"Info" : "Pacientot e izbrisan"})

    def patch(self, request):
        pacient = Pacienti.objects.get(id = request.data['id'])
        pacient_serializer = PacientiSerilizer(pacient, data=request.data)
        if pacient_serializer.is_valid():
            pacient_serializer.save()
            return Response (pacient_serializer.data, status=status.HTTP_201_CREATED)
        return Response({"Errors": pacient_serializer.errors})


class OddeliView(APIView):
    permission_classes = (IsAuthenticated,)

    def get (self, request):
        oddel=Oddeli.objects.get(id=request.GET["oddelId"])
        oddel_serializer = OddeliSerilizer(oddel)
        return Response(oddel_serializer.data)

    def post (self, request):
        oddel_serializer = OddeliSerilizer(data=request.data)
        if oddel_serializer.is_valid():
            oddel_serializer.save()
            return Response(oddel_serializer.data, status=status.HTTP_201_CREATED)
        return Response ({"Info" : "Nastana greska"}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request):
        oddel = Oddeli.objects.get(id=request.GET["oddelId"])
        oddel.delete()
        return Response ({"Info" : "Oddelot e izbrisan"})

    def patch(self, request):
        oddel = Oddeli.objects.get(id = request.data['id'])
        oddel_serializer = OddeliSerilizer(oddel, data=request.data)
        if oddel_serializer.is_valid():
            oddel_serializer.save()
            return Response (oddel_serializer.data, status=status.HTTP_201_CREATED)
        return Response({"Errors": oddel_serializer.errors})

class PreglediView(APIView):
    permission_classes = (IsAuthenticated,)

    def get (self, request):
        pregled=Pregledi.objects.get(id=request.GET["pregledId"])
        pregled_serializer = PreglediSerilizer(pregled)
        return Response(pregled_serializer.data)

    def post (self, request):
        pregled_serializer = PreglediSerilizer(data=request.data)
        if pregled_serializer.is_valid():
            pregled_serializer.save()
            return Response(pregled_serializer.data, status=status.HTTP_201_CREATED)
        return Response ({"Info" : "Nastana greska"}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request):
        pregled = Pregledi.objects.get(id=request.GET["pregledId"])
        pregled.delete()    
        return Response ({"Info" : "Pregledot e izbrisan"})

    def patch(self, request):
        pregled = Pregledi.objects.get(id = request.data['id'])
        pregled_serializer = PreglediSerilizer(pregled, data=request.data)
        if pregled_serializer.is_valid():
            pregled_serializer.save()
            return Response (pregled_serializer.data, status=status.HTTP_201_CREATED)
        return Response({"Errors": pregled_serializer.errors})

class HospitalizacijaView(APIView):
    permission_classes = (IsAuthenticated,)

    def get (self, request):
        hospitalizacija=Pregledi.objects.get(id=request.GET["hospitalizacijaId"])
        hospitalizacija_serializer = HospitalizacijaSerilizer(hospitalizacija)
        return Response(hospitalizacija_serializer.data)

    def post (self, request):
        hospitalizacija_serializer = HospitalizacijaSerilizer(data=request.data)
        if hospitalizacija_serializer.is_valid():
            hospitalizacija_serializer.save()
            return Response(hospitalizacija_serializer.data, status=status.HTTP_201_CREATED)
        return Response ({"Info" : "Nastana greska"}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request):
        pregled = Hospitalizacija.objects.get(id=request.GET["hospitalizacijaId"])
        pregled.delete()    
        return Response ({"Info" : "Hospitalizacijata e izbrisana"})

    def patch(self, request):
        hospitalizacija = Hospitalizacija.objects.get(id = request.data['id'])
        hospitalizacija_serializer = HospitalizacijaSerilizer(hospitalizacija, data=request.data)
        if hospitalizacija_serializer.is_valid():
            hospitalizacija_serializer.save()
            return Response (hospitalizacija_serializer.data, status=status.HTTP_201_CREATED)
        return Response({"Errors": hospitalizacija_serializer.errors})