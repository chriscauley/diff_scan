from django.conf import settings
from django.contrib.sites.models import Site
from django.db import models

from utils import image_diff

import subprocess, urllib, os, datetime

class Page(models.Model):
  path = models.TextField()
  site = models.ForeignKey(Site)
  def get_absolute_url(self):
    if '://' in self.site.domain:
      return self.site.domain+self.path
    return 'http://%s%s'%(self.site.domain,self.path)
  __unicode__ = lambda self: self.get_absolute_url()
  def test(self,screensize):
    pagetest,new = PageTest.objects.get_or_create(page=self,screensize=screensize)
    w = screensize.width
    h = screensize.height
    screenshot_dir = os.path.join(settings.MEDIA_ROOT,'screenshots')
    output_dir = os.path.join(settings.MEDIA_ROOT,'screenshots',str(self.id))
    diff_dir = os.path.join(settings.MEDIA_ROOT,'diffs')
    for d in [settings.MEDIA_ROOT,screenshot_dir,output_dir,diff_dir]:
      if not os.path.exists(d):
        os.mkdir(d)
    f_name = datetime.datetime.now().strftime("%Y%m%d%H%M%S.png")
    output_path = os.path.join(output_dir,f_name)
    parts = [
      "wkhtmltoimage",
      "--width %s"%w if w else '',
      "--height %s"%h if h else '',
      self.get_absolute_url(),
      output_path,
      ]
    print ' '.join(parts)
    process = subprocess.Popen(' '.join(parts),shell=True)
    process.communicate()[0]
    if pagetest.test_image:
      os.remove(pagetest.test_image.path)

    # image has never been tested before
    if not pagetest.stable_image:
      pagetest.stable_image = output_path.split('media/')[-1]
      accepted = True
      pagetest.save()
      return

    diff_path = os.path.join(diff_dir,"%s.png"%pagetest.id)
    different = image_diff(pagetest.stable_image.path,output_path,diff_path)

    if not different:
      return

    # page has changed!
    pagetest.test_image = output_path.split('media/')[-1]
    pagetest.diff_image = diff_path.split('media/')[-1]
    pagetest.accepted = False
    pagetest.save()

class ScreenSize(models.Model):
  _ht = "In pixels; 0 will default to an automatic size"
  width = models.IntegerField(default=0,help_text=_ht)
  height = models.IntegerField(default=0,help_text=_ht)
  name = models.CharField(max_length=64,null=True,blank=True)
  sites = models.ManyToManyField(Site)
  __unicode__ = lambda self: "%s (%sx%s)"%(self.name or "Unnamed",self.width,self.height)

class PageTest(models.Model):
  page = models.ForeignKey(Page)
  screensize = models.ForeignKey(ScreenSize)
  stable_image = models.ImageField(upload_to='screenshots',null=True,blank=True)
  test_image = models.ImageField(upload_to='screenshots',null=True,blank=True)
  diff_image = models.ImageField(upload_to='diffs',null=True,blank=True)
  accepted = models.BooleanField(default=True)
  error_code = models.IntegerField(null=True,blank=True)
  def accept(self):
    self.stable_image = self.test_image
    self.test_image = self.diff_image = None
    self.accepted = True
    self.save()
