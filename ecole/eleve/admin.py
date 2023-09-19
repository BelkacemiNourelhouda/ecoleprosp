from django.contrib import admin
from eleve.models import Eleve, ElevePre, ElevePrim, EleveCEM
# Register your models here.


admin.site.register(Eleve)
admin.site.register(EleveCEM)
admin.site.register(ElevePrim)
admin.site.register(ElevePre)

