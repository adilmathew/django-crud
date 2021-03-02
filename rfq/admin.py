#rom WORK.rfq.models import Component
from django.contrib import admin
from .models import (Rfq,Component,Part,Consumable)
# Register your models here.
admin.site.register(Rfq)
admin.site.register(Component)
admin.site.register(Part)
admin.site.register(Consumable)
