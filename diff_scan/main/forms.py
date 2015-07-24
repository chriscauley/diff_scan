from django import forms
from django.contrib.sites.models import Site

from .models import Page

class BulkURLForm(forms.Form):
  urls = forms.CharField(widget=forms.Textarea)
  site = forms.ModelChoiceField(queryset=Site.objects.all())
  def save(self):
    urls = self.cleaned_data['urls'].replace('\r','').split('\n')
    new,old,errors = 0,0,[]
    for url in urls:
      if '://' in url:
        url = '/' + '/'.join(url.split('://')[-1].split('/')[1:])
      if not url.startswith('/'):
        errors.append('"%s" failed: no relative paths allowed'%url)
        continue
      page,created = Page.objects.get_or_create(path=url,site=self.cleaned_data['site'])
      if created:
        new += 1
      else:
        old += 1
    return new,old,errors
