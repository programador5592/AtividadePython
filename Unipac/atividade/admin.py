from django.contrib import admin
from .models import Empresas
from .models import Aprendiz
from .models import Disciplinas
from .models import Professor

# Register your models here.

admin.site.register(Empresas)
admin.site.register(Aprendiz)
admin.site.register(Disciplinas)
admin.site.register(Professor)

