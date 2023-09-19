from django.contrib import admin

# Register your models here.
from django.contrib import admin
from elevedeux.models import Eleve, ElevePre, ElevePrim, EleveCEM
# Register your models here.


admin.site.register(Eleve)
admin.site.register(EleveCEM)
admin.site.register(ElevePrim)
admin.site.register(ElevePre)

