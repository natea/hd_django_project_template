# -*- coding: utf-8 -*-
"""
Admin configuration for for %%PROJECTNAME%%.

%%COPYRIGHT%%
"""

### SAMPLE CODE FOLLOWS

from django.contrib import admin
from %%MODULENAME%%.models import Auftrag, AuftragsPosition


class AuftragsPositionInline(admin.StackedInline):
    """Configuration of the Django Admin Interface."""
    model = AuftragsPosition
    extra = 0
    

class AuftragAdmin(admin.ModelAdmin):
    """Configuration of the Django Admin Interface."""
    inlines = [AuftragsPositionInline]
    date_hierarchy = 'created_at'
    list_display = ('pk', 'liefer_name1', 'bestelldatum')
    list_filter = ('status', 'kundennr')
    search_fields = ('guid', 'kundenauftragsnr', 'auftragsnr')
    save_on_top = True
    raw_id_fields = ('verladung', )
    

# register admin classes
admin.site.register(Auftrag, AuftragAdmin)
