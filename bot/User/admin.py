from django.contrib import admin
from User.models import Contastant,Handle_Name
# Register your models here.
class ContastantAdmin(admin.ModelAdmin):
    list_display=('id','c_id','c_name','c_email')
admin.site.register(Contastant,ContastantAdmin)

admin.site.register(Handle_Name)