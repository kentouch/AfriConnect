from django.contrib import admin

# Register your models here.
# contact/admin.py

from django.contrib import admin
from .models import ContactMessage

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'sent_date')
    list_filter = ('sent_date',)
    search_fields = ('name', 'email', 'subject', 'message')
    readonly_fields = ('sent_date',)