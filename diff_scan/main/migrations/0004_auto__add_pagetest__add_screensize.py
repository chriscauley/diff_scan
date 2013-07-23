# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'PageTest'
        db.create_table(u'main_pagetest', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal(u'main', ['PageTest'])

        # Adding model 'ScreenSize'
        db.create_table(u'main_screensize', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('width', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('height', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=64, null=True, blank=True)),
        ))
        db.send_create_signal(u'main', ['ScreenSize'])

        # Adding M2M table for field screen_sizes on 'Page'
        m2m_table_name = db.shorten_name(u'main_page_screen_sizes')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('page', models.ForeignKey(orm[u'main.page'], null=False)),
            ('screensize', models.ForeignKey(orm[u'main.screensize'], null=False))
        ))
        db.create_unique(m2m_table_name, ['page_id', 'screensize_id'])


    def backwards(self, orm):
        # Deleting model 'PageTest'
        db.delete_table(u'main_pagetest')

        # Deleting model 'ScreenSize'
        db.delete_table(u'main_screensize')

        # Removing M2M table for field screen_sizes on 'Page'
        db.delete_table(db.shorten_name(u'main_page_screen_sizes'))


    models = {
        u'main.page': {
            'Meta': {'object_name': 'Page'},
            'accepted': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'diff_image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'path': ('django.db.models.fields.TextField', [], {}),
            'screen_sizes': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['main.ScreenSize']", 'null': 'True', 'blank': 'True'}),
            'site': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['sites.Site']"}),
            'stable_image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'test_image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'})
        },
        u'main.pagetest': {
            'Meta': {'object_name': 'PageTest'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'main.screensize': {
            'Meta': {'object_name': 'ScreenSize'},
            'height': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '64', 'null': 'True', 'blank': 'True'}),
            'width': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        u'sites.site': {
            'Meta': {'ordering': "('domain',)", 'object_name': 'Site', 'db_table': "'django_site'"},
            'domain': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['main']