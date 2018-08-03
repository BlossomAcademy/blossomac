from django.contrib import admin
from .models import Feedback

##admin.site.unregister(User)

@admin.register(Feedback)
class BlossomAdmin(admin.ModelAdmin):
    list_display=['sender']
    
# Register your models here.
 