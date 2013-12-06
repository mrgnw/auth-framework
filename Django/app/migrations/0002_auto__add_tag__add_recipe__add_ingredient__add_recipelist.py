# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Tag'
        db.create_table(u'app_tag', (
            ('tag_id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('tag_name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('frequency', self.gf('django.db.models.fields.IntegerField')()),
            ('created', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal(u'app', ['Tag'])

        # Adding model 'Recipe'
        db.create_table(u'app_recipe', (
            ('recipe_id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('tag', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['app.Tag'])),
            ('recipe_name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('recipe_description', self.gf('django.db.models.fields.CharField')(max_length=4000)),
            ('recipe_directions', self.gf('django.db.models.fields.CharField')(max_length=4000)),
            ('recipe_notes', self.gf('django.db.models.fields.CharField')(max_length=4000)),
            ('recipe_yield', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('recipe_prep_time', self.gf('django.db.models.fields.IntegerField')()),
            ('recipe_cook_time', self.gf('django.db.models.fields.IntegerField')()),
            ('recipe_total_time', self.gf('django.db.models.fields.IntegerField')()),
            ('recipe_source', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('private', self.gf('django.db.models.fields.IntegerField')()),
            ('archive', self.gf('django.db.models.fields.IntegerField')()),
            ('created', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal(u'app', ['Recipe'])

        # Adding M2M table for field recipe_lists on 'Recipe'
        m2m_table_name = db.shorten_name(u'app_recipe_recipe_lists')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('recipe', models.ForeignKey(orm[u'app.recipe'], null=False)),
            ('recipelist', models.ForeignKey(orm[u'app.recipelist'], null=False))
        ))
        db.create_unique(m2m_table_name, ['recipe_id', 'recipelist_id'])

        # Adding model 'Ingredient'
        db.create_table(u'app_ingredient', (
            ('ingredient_id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('ingredient_name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('recipe', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['app.Recipe'])),
            ('measurement', self.gf('django.db.models.fields.IntegerField')()),
            ('measurement_type', self.gf('django.db.models.fields.CharField')(max_length=10)),
        ))
        db.send_create_signal(u'app', ['Ingredient'])

        # Adding model 'RecipeList'
        db.create_table(u'app_recipelist', (
            ('recipe_list_id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('recipe_list_name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('created', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal(u'app', ['RecipeList'])


    def backwards(self, orm):
        # Deleting model 'Tag'
        db.delete_table(u'app_tag')

        # Deleting model 'Recipe'
        db.delete_table(u'app_recipe')

        # Removing M2M table for field recipe_lists on 'Recipe'
        db.delete_table(db.shorten_name(u'app_recipe_recipe_lists'))

        # Deleting model 'Ingredient'
        db.delete_table(u'app_ingredient')

        # Deleting model 'RecipeList'
        db.delete_table(u'app_recipelist')


    models = {
        u'app.address': {
            'Meta': {'object_name': 'Address'},
            'city': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'country': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'street': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'app.ingredient': {
            'Meta': {'ordering': "('ingredient_name',)", 'object_name': 'Ingredient'},
            'ingredient_id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ingredient_name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'measurement': ('django.db.models.fields.IntegerField', [], {}),
            'measurement_type': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'recipe': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['app.Recipe']"})
        },
        u'app.recipe': {
            'Meta': {'ordering': "('created',)", 'object_name': 'Recipe'},
            'archive': ('django.db.models.fields.IntegerField', [], {}),
            'created': ('django.db.models.fields.DateTimeField', [], {}),
            'private': ('django.db.models.fields.IntegerField', [], {}),
            'recipe_cook_time': ('django.db.models.fields.IntegerField', [], {}),
            'recipe_description': ('django.db.models.fields.CharField', [], {'max_length': '4000'}),
            'recipe_directions': ('django.db.models.fields.CharField', [], {'max_length': '4000'}),
            'recipe_id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'recipe_lists': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['app.RecipeList']", 'symmetrical': 'False'}),
            'recipe_name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'recipe_notes': ('django.db.models.fields.CharField', [], {'max_length': '4000'}),
            'recipe_prep_time': ('django.db.models.fields.IntegerField', [], {}),
            'recipe_source': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'recipe_total_time': ('django.db.models.fields.IntegerField', [], {}),
            'recipe_yield': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'tag': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['app.Tag']"}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"})
        },
        u'app.recipelist': {
            'Meta': {'ordering': "('created',)", 'object_name': 'RecipeList'},
            'created': ('django.db.models.fields.DateTimeField', [], {}),
            'recipe_list_id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'recipe_list_name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'app.tag': {
            'Meta': {'ordering': "('created',)", 'object_name': 'Tag'},
            'created': ('django.db.models.fields.DateTimeField', [], {}),
            'frequency': ('django.db.models.fields.IntegerField', [], {}),
            'tag_id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'tag_name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['app']