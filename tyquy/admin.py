from django.contrib import admin
from .models import Level, Session, Text, SessionText, Comment

# Register your models here.

class LevelAdmin(admin.ModelAdmin):
 list_display = ('name','description')
 list_filter = ['name']

class SessionAdmin(admin.ModelAdmin):
 list_display = ('name','instructions','level')
 list_filter = ['name','level']

class TextAdmin(admin.ModelAdmin):
 list_display = ('name','author','type')
 list_filter = ['type','author']


class SessionTextAdmin(admin.ModelAdmin):
 list_display = ('session','text')
 list_filter = ['session']


admin.site.register(Level, LevelAdmin)
admin.site.register(Session, SessionAdmin)
admin.site.register(Text, TextAdmin)
admin.site.register(SessionText, SessionTextAdmin)
admin.site.register(Comment)
