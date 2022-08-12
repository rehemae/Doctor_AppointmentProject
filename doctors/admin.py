from django.contrib import admin
from.models import Login,Registration,Clinic

# Register your models here.
class LoginAdmin(admin.ModelAdmin):
    list_display=("first_name","last_name",)
    search_fields=("fist_name","last_name")
admin.site.register(Login,LoginAdmin)
admin.site.register(Registration)
admin.site.register(Clinic)
