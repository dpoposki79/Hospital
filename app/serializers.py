from rest_framework import serializers
from .models import Doktori, Pacienti, Oddeli, Pregledi, Hospitalizacija, Termin



class PacientiSerilizer(serializers.ModelSerializer):
    class Meta:
        model=Pacienti
        fields = "__all__"

    def create(self, validated_data):  
        return Pacienti.objects.create(**validated_data)

class DoktoriSerilizer(serializers.ModelSerializer):
    class Meta:
        model=Doktori
        fields = "__all__"

    def create(self, validated_data):   
        return Doktori.objects.create(**validated_data)

class OddeliSerilizer(serializers.ModelSerializer):

    class Meta:
        model=Oddeli
        fields = "__all__"

    def create(self, validated_data):  
        return Oddeli.objects.create(**validated_data)



class HospitalizacijaSerilizer(serializers.ModelSerializer):

    class Meta:
        model=Hospitalizacija
        fields = "__all__"

    def create(self, validated_data):
        return Hospitalizacija.objects.create(**validated_data)

class PreglediSerilizer(serializers.ModelSerializer):
    Doktor = DoktoriSerilizer(read_only=True)       #Ova se stava dokolku sakame da povrzeme podatoci. Pri API za pregledi ke dade detali i za doktori i za pacientot
    Pacient = PacientiSerilizer(read_only=True)
    class Meta:
        model=Pregledi
        fields = "__all__"
        
    def create(self, validated_data):
        return Pregledi.objects.create(**validated_data)

class TerminiSerilizer(serializers.ModelSerializer):
    class Meta:
        model=Termin
        fields = "__all__"
    def create(self, validated_data):
        return Termin.objects.create(**validated_data)