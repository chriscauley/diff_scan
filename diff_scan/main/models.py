from django.conf import settings
from django.contrib.sites.models import Site
from django.db import models

from utils import image_diff

import subprocess, urllib, os, datetime

class Page(models.Model):
  path = models.TextField()
  stable_image = models.ImageField(upload_to='screenshots',null=True,blank=True)
  test_image = models.ImageField(upload_to='screenshots',null=True,blank=True)
  diff_image = models.ImageField(upload_to='diffs',null=True,blank=True)
  site = models.ForeignKey(Site)
  accepted = models.BooleanField(default=True)
  def get_absolute_url(self):
    if '://' in self.site.domain:
      return self.site.domain+self.path
    return 'http://%s%s'%(self.site.domain,self.path)
  __unicode__ = lambda self: self.get_absolute_url()
  def test(self):
    screenshot_dir = os.path.join(settings.MEDIA_ROOT,'screenshots')
    output_dir = os.path.join(settings.MEDIA_ROOT,'screenshots',str(self.id))
    diff_dir = os.path.join(settings.MEDIA_ROOT,'diffs')
    for d in [settings.MEDIA_ROOT,screenshot_dir,output_dir,diff_dir]:
      if not os.path.exists(d):
        os.mkdir(d)
    f_name = datetime.datetime.now().strftime("%Y%m%d%H%M%S.png")
    output_path = os.path.join(output_dir,f_name)
    process = subprocess.Popen('xvfb-run --server-args="-screen 0, 1024x768x24" webkit2png %s > %s'%(self.get_absolute_url(),output_path),shell=True)
    process.communicate()[0]
    if self.test_image:
      os.remove(self.test_image.path)

    # image has never been tested before
    if not self.stable_image:
      self.stable_image = output_path.split('media/')[-1]
      accepted = True
      self.save()
      return

    diff_path = os.path.join(diff_dir,"%s.png"%self.id)
    different = image_diff(self.stable_image.path,output_path,diff_path)

    if not different:
      return

    # page has changed!
    self.test_image = output_path.split('media/')[-1]
    self.diff_image = diff_path.split('media/')[-1]
    self.accepted = False
    self.save()

  def accept(self):
    self.stable_image = self.test_image
    self.test_image = self.diff_image = None
    self.accepted = True
    self.save()
