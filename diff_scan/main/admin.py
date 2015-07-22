from django.contrib import admin

from main.models import Page, ScreenSize, PageTest

class PageTestInline(admin.TabularInline):
  has_add_permission = lambda self, request, obj=None: False
  model = PageTest

class PageAdmin(admin.ModelAdmin):
  readonly_fields = ('run_all_tests',)
  inlines = [PageTestInline]
  def run_all_tests(self,obj=None):
    if not obj:
      return "Please save before trying to run tests."
    return "<a href='/test/%s/'>Run all tests</a>"%obj.pk
  run_all_tests.allow_tags = True

admin.site.register(Page,PageAdmin)
admin.site.register(ScreenSize)
