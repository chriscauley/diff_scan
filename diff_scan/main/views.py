from django.http import HttpResponseRedirect

from main.models import Page

def test(request,pk):
    Page.objects.get(pk=pk).test()
    return HttpResponseRedirect('/admin/main/page/%s/'%pk)
