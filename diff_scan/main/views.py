from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.template.response import TemplateResponse

from .forms import BulkURLForm
from .models import Page, PageTest

def index(request):
  pages = Page.objects.all()
  values = {
    'pages': pages,
    }
  return TemplateResponse(request,"index.html",values)

def page_detail(request,pk):
  page = get_object_or_404(Page,pk=pk)
  values = {
    'page': page,
  }
  return TemplateResponse(request,"page_detail.html",values)

def action(request,action,page_pk,test_pk):
  page = get_object_or_404(Page,pk=page_pk)
  tests = page.pagetest_set.all()
  if test_pk:
    tests = tests.filter(pk=test_pk)
  for test in tests:
    if action == 'clear':
      test.stable_image = test.test_image = test.diff_image = ''
      test.save()
      messages.success(request,"PageTest cleared: %s"%test)
    elif action == 'test':
      accepted = page.test(test.screensize)
      if accepted:
        messages.success(request,"Test Passed: %s"%test)
      else:
        messages.error(request,"Test Failed: %s"%test)
    elif action == 'accept':
      test.accept()
      messages.success(request,"Test Accepted: %s"%test)
  return HttpResponseRedirect(page.get_absolute_url())

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

