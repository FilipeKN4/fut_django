from django.contrib import admin

# Register your models here.
from .models import Time
from .forms import TimeModelForm

class AdminTime(admin.ModelAdmin):
    list_display = ["nome", "cidade", "sigla_estado"]
    list_editable = ["cidade"]
    form = TimeModelForm
    #class Meta:
    #    model = Time

admin.site.register(Time, AdminTime)