from django.db import models
import subprocess, urllib, os

from diff_scan.utils import image_diff

class Page(models.Model):
  url = models.TextField()
  stable_image = models.ImageField(upload_to='screenshots',null=True,blank=True)
  test_image = models.ImageField(upload_to='screenshots',null=True,blank=True)
  diff_image = models.ImageField(upload_to='diffs',null=True,blank=True)
  accepted = models.BooleanField(default=True)
  domain = 'http://127.0.0.1:8000' #! needs to be dynamic
  def test(self):
    output_dir = os.path.join(settings.MEDIA_URL,'screenshots',urllib.quote_plus(self.url))
    diff_dir = os.path.join(settings.MEDIA_URL,'diffs')
    for d in [settings.MEDIA_URL,output_dir,diff_dir]:
      if not os.path.exists(output_dir):
        os.mkdir(output_dir)
    f_name = datetime.datetime.now().strftime("%Y%m%d%H%M%S.png")
    output_path = os.path.join(output_dir,f_name)
    process = subprocess.Popen('webkit2png %s%s > %s'%(self.domain,self.url,output_path))
    process.communicate()[0]
    if self.test_image:
      os.remove(self.test_image)
    if not self.stable_image:
      self.stable_image = output_path
      accepted = True
    else:
      self.test_image = output_path
      self.diff_image = os.path.join(diff_dir,urllib.quote_plus(self.url))
      image_diff(self.stable_image,self.test_image,self.test_image)
      self.accepted = False
    self.save()

  def accept(self):
    self.stable_image = self.test_image
    self.test_image = self.diff_image = None
    self.accepted = True
    self.save()
