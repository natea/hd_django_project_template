# -*- coding: utf-8 -*-
"""
Models for %%PROJECTNAME%%.

%%COPYRIGHT%%
"""

### SAMPLE CODE FOLLOWS
from django.db import models

class Angebot(models.Model):
    created_at = models.DateTimeField(verbose_name='Angelegt', auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(verbose_name='letzte Aenderung', auto_now=True, editable=False)
    
    class Meta:
        """Additional imformation for the ORM."""
        get_latest_by = 'created_at'
        ordering = ['-created_at']
        verbose_name_plural = 'Angebote'
        permissions = (('view_angebot', 'Can view Angebote'),)
    
    def __unicode__(self):
        """Return a Unicode/String representation of the Object."""
        return u"Angebot %s an %s" % (self.designator, self.firma)
    
    @models.permalink
    def get_absolute_url(self):
        """Gibt die canonische URL für das Objekt zurück."""
        return ('benedict.views.show_order_messages', (), {'order_id': quote(self.id)})
