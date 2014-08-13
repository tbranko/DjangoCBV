# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Gun'
        db.create_table(u'core_gun', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('make', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('model', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal('core', ['Gun'])


    def backwards(self, orm):
        # Deleting model 'Gun'
        db.delete_table(u'core_gun')


    models = {
        'core.gun': {
            'Meta': {'object_name': 'Gun'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'make': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['core']