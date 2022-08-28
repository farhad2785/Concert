from django.contrib import admin
from . import models
# Register your models here.

admin.site.register(models.ConcertModel)
admin.site.register(models.LocationModel)
admin.site.register(models.TicketModel)
admin.site.register(models.TimeModel)
