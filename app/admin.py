from django.contrib import admin
from .models import Doktori, Pacienti, Oddeli, Pregledi, Hospitalizacija, Termin







admin.site.register(Doktori)
admin.site.register(Pacienti)
admin.site.register(Oddeli)
admin.site.register(Pregledi)
admin.site.register(Hospitalizacija)
admin.site.register(Termin)
# Register your models here.
