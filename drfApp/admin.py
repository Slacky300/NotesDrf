from django.contrib import admin

# Register your models here.
from . models import *

admin.site.register(UserAccount)
admin.site.register(Subject)
admin.site.register(Module)
admin.site.register(Notes)
