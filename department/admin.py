from django.contrib import admin
from .models import Department

# Register your models here.
class DepartmentAdmin(admin.ModelAdmin):
    model = Department
    list_display = [i.name for i in Department._meta.fields]

admin.site.register(Department,DepartmentAdmin)