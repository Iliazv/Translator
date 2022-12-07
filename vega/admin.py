from django.contrib import admin
from .models import Document, Report, HistoryObject, SelectObject
#ilu

admin.site.register(Document)
admin.site.register(Report)
admin.site.register(HistoryObject)
admin.site.register(SelectObject)