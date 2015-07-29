from django.conf import settings
from django.contrib.sites.models import Site
from django.core.urlresolvers import reverse
from django.db import models

from img_utils import image_diff
from media.models import Photo

import subprocess, urllib, os, datetime

class Page(models.Model):
  path = models.TextField()
  site = models.ForeignKey(Site)
  def get_absolute_url(self):
    return reverse('page_detail',args=[self.pk])
  def get_site_url(self):
    if '://' in self.site.domain:
      return self.site.domain+self.path
    return 'http://%s%s'%(self.site.domain,self.path)
  __unicode__ = lambda self: self.get_site_url()
  def test(self,screensize):
    page_test,new = PageTest.objects.get_or_create(page=self,screensize=screensize)
    w = screensize.width or 1400
    h = screensize.height or 3000
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
      self.get_site_url(),
      output_path,
      ]
    print ' '.join(parts)
    process = subprocess.Popen(' '.join(parts),shell=True)
    process.communicate()[0]
    if page_test.test_image:
      os.remove(page_test.test_image.path)

    # image has never been tested before
    if not page_test.stable_image:
      page_test.stable_image = output_path.split('media/')[-1]
      page_testaccepted = True
      page_test.save()
      return True

    diff_path = os.path.join(diff_dir,"%s.png"%page_test.id)
    different = image_diff(page_test.stable_image.path,output_path,diff_path)

    if not different:
      return True

    # page has changed!
    page_test.test_image = output_path.split('media/')[-1]
    page_test.diff_image = diff_path.split('media/')[-1]
    page_test.accepted = False
    page_test.save()
    return False

SIZE_ICON_CHOICES = (
  ('desktop','Desktop'),
  ('mobile','Mobile'),
  ('tablet','Tablet'),
)

class ScreenSize(models.Model):
  _ht = "In pixels; 0 will default to an automatic size"
  width = models.IntegerField(default=0,help_text=_ht)
  height = models.IntegerField(default=0,help_text=_ht)
  icon = models.CharField(max_length=16,choices=SIZE_ICON_CHOICES)
  name = models.CharField(max_length=64,null=True,blank=True)
  sites = models.ManyToManyField(Site)
  __unicode__ = lambda self: "%s (%sx%s)"%(self.name or "Unnamed",self.width,self.height)

class PageTest(models.Model):
  page = models.ForeignKey(Page)
  screensize = models.ForeignKey(ScreenSize)
  stable_image = models.ImageField(upload_to='screenshots',null=True,blank=True)
  test_image = models.ImageField(upload_to='screenshots',null=True,blank=True)
  diff_image = models.ImageField(upload_to='diffs',null=True,blank=True)
  design = models.ForeignKey(Photo,null=True,blank=True)
  accepted = models.BooleanField(default=True)
  error_code = models.IntegerField(null=True,blank=True)
  def get_images(self):
    return [
      ('Stable',self.stable_image),
      ('Test',self.test_image),
      ('Diff',self.diff_image),
      ]
  def accept(self):
    self.stable_image = self.test_image
    self.test_image = self.diff_image = None
    self.accepted = True
    self.save()
