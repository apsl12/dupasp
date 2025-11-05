from django.contrib import admin
from .models import Table1
@admin.register(Table1)
class Table1Admin(admin.ModelAdmin):
    list_display = ('s_no','name','email')
# Register your models here.
