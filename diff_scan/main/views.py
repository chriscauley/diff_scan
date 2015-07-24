from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.template.response import TemplateResponse

from .forms import BulkURLForm
from .models import Page, PageTest

def test(request,pk):
    page = get_object_or_404(Page,pk=pk)
    for size in page.site.screensize_set.all():
        page.test(size)
    return HttpResponseRedirect('/admin/main/page/%s/'%pk)

def bulk_add_url(request):
    form = BulkURLForm(request.POST or None)
    if form.is_valid():
        new,old,errors = form.save()
        messages.success(request,"%s urls have been added; %s were redundant."%(new,old))
        for error in errors:
            messages.error(request,error)
        return HttpResponseRedirect(request.path)
    values = {'form': form}
    return TemplateResponse(request,"bulk_upload.html",values)

def index(request):
    pages = Page.objects.all()
    values = {
        'pages': pages,
        }
    return TemplateResponse(request,"index.html",values)
