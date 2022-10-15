from django.contrib import admin
from .models import cars
from .models import tx
from .models import user

admin.site.register(cars)
admin.site.register(tx)
admin.site.register(user)

