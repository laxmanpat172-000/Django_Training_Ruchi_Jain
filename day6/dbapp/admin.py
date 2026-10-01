from django.contrib import admin
from dbapp.models import client
from dbapp.models import member,company


admin.site.register(client)
admin.site.register(member)
admin.site.register(company)

# Register your models here.
