# -*- coding: utf-8 -*-
"""
Views for %%PROJECTNAME%%.

%%COPYRIGHT%%
"""

### SAMPLE CODE FOLLOWS

from django.contrib.admin.models import LogEntry, ADDITION, CHANGE, DELETION
from django.contrib.auth.decorators import permission_required
from django.contrib.contenttypes.models import ContentType
from django.core.xheaders import populate_xheaders
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render_to_response
from django.template import RequestContext
from django.utils.translation import ungettext_lazy as _
from django.views.decorators.cache import never_cache, cache_page
from django.views.decorators.http import require_POST

@require_POST
@permission_required('anbietr.view_angebot')
@never_cache
def show_order_pdf(request, objid):
    """Some descriptive text."""
    angebot = get_object_or_404(Angebot, id=objid)
    response = HttpResponse(mimetype='application/pdf')
    response['Content-Disposition'] = 'attachment; filename=%s' % (filename % objid)
    response.write(angebot.generate_pdf())
    LogEntry.objects.log_action(request.user.id, ContentType.objects.get_for_model(Angebot).id,
                                angebot.id, unicode(angebot), CHANGE, 'Output erzeugt') 
    populate_xheaders(request, response, Angebot, angebot.id)
    return response
    

def anfrage(request, template):
    if request.method == 'POST': # If the form has been submitted...
        form = MyForm(request.POST)
        if form.is_valid():
            # All validation rules pass
            new_inquiry = form.save()
            # load instance from db to get result of post-save hook
            new_inquiry = Inquiry.objects.get(pk=new_inquiry.id)
            return HttpResponseRedirect('thanks/?guid=%s' % new_inquiry.guid)
    else:
        form = InquiryForm() # An unbound form
    return render_to_response('curm2/%s.html' % template, {'form': form },
                              context_instance=RequestContext(request))
    

@cache_page(60 * 15) # 15 Minutes
def anfrage_erfassen_thanks(request):
    return render_to_response('curm2/anfrage_erfassen_thanks.html',
                              context_instance=RequestContext(request))
    
