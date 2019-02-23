from django.contrib import admin
from .models import Employee
from import_export.admin import ImportExportModelAdmin


class EmployeeAdmin(ImportExportModelAdmin):
    pass

#admin.register(Employee,EmployeeAdmin)
admin.site.register(Employee,EmployeeAdmin)
