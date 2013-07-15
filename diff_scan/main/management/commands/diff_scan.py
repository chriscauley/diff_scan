from django.core.management.base import BaseCommand, CommandError
from django.contrib.sites.models import Site
from main.models import Page

from simplejson import loads
import sys

class Command(BaseCommand):
    args = '/path/to/manifest.json'
    def handle(self, *args, **options):
        if len(args) < 1:
            print 'You must specify a json file as the first argument'
            return
        f = open(args[0],'r')
        manifest = loads(f.read())
        site = Site.objects.get_or_create(domain=manifest['domain'],name=manifest['domain'])[0]
        pages = [Page.objects.get_or_create(site=site,path=p)[0] for p in manifest['pages']]
        for p in pages:
            p.test()
        test_pages = Page.objects.filter(site=site,accepted=False)
        print "there are %s pages that need to be approved"%test_pages.count()
