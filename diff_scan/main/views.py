from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404

from main.models import Page, PageTest

def test(request,pk):
    page = get_object_or_404(Page,pk=pk)
    for size in page.site.screensize_set.all():
        page.test(size)
    return HttpResponseRedirect('/admin/main/page/%s/'%pk)
