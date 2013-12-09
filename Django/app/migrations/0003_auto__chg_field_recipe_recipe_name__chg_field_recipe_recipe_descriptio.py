# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Recipe.recipe_name'
        db.alter_column(u'app_recipe', 'recipe_name', self.gf('django.db.models.fields.CharField')(default='', max_length=100))

        # Changing field 'Recipe.recipe_description'
        db.alter_column(u'app_recipe', 'recipe_description', self.gf('django.db.models.fields.CharField')(max_length=4000, null=True))

        # Changing field 'Recipe.recipe_notes'
        db.alter_column(u'app_recipe', 'recipe_notes', self.gf('django.db.models.fields.CharField')(max_length=4000, null=True))

        # Changing field 'Recipe.recipe_yield'
        db.alter_column(u'app_recipe', 'recipe_yield', self.gf('django.db.models.fields.CharField')(max_length=20, null=True))

        # Changing field 'Recipe.recipe_directions'
        db.alter_column(u'app_recipe', 'recipe_directions', self.gf('django.db.models.fields.CharField')(max_length=4000, null=True))

        # Changing field 'Recipe.recipe_source'
        db.alter_column(u'app_recipe', 'recipe_source', self.gf('django.db.models.fields.CharField')(max_length=255, null=True))

    def backwards(self, orm):

        # Changing field 'Recipe.recipe_name'
        db.alter_column(u'app_recipe', 'recipe_name', self.gf('django.db.models.fields.CharField')(max_length=100, null=True))

        # User chose to not deal with backwards NULL issues for 'Recipe.recipe_description'
        raise RuntimeError("Cannot reverse this migration. 'Recipe.recipe_description' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration
        # Changing field 'Recipe.recipe_description'
        db.alter_column(u'app_recipe', 'recipe_description', self.gf('django.db.models.fields.CharField')(max_length=4000))

        # User chose to not deal with backwards NULL issues for 'Recipe.recipe_notes'
        raise RuntimeError("Cannot reverse this migration. 'Recipe.recipe_notes' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration
        # Changing field 'Recipe.recipe_notes'
        db.alter_column(u'app_recipe', 'recipe_notes', self.gf('django.db.models.fields.CharField')(max_length=4000))

        # User chose to not deal with backwards NULL issues for 'Recipe.recipe_yield'
        raise RuntimeError("Cannot reverse this migration. 'Recipe.recipe_yield' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration
        # Changing field 'Recipe.recipe_yield'
        db.alter_column(u'app_recipe', 'recipe_yield', self.gf('django.db.models.fields.CharField')(max_length=20))

        # User chose to not deal with backwards NULL issues for 'Recipe.recipe_directions'
        raise RuntimeError("Cannot reverse this migration. 'Recipe.recipe_directions' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration
        # Changing field 'Recipe.recipe_directions'
        db.alter_column(u'app_recipe', 'recipe_directions', self.gf('django.db.models.fields.CharField')(max_length=4000))

        # User chose to not deal with backwards NULL issues for 'Recipe.recipe_source'
        raise RuntimeError("Cannot reverse this migration. 'Recipe.recipe_source' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration
        # Changing field 'Recipe.recipe_source'
        db.alter_column(u'app_recipe', 'recipe_source', self.gf('django.db.models.fields.CharField')(max_length=255))

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
            'archive': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'private': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'recipe_cook_time': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'recipe_description': ('django.db.models.fields.CharField', [], {'max_length': '4000', 'null': 'True', 'blank': 'True'}),
            'recipe_directions': ('django.db.models.fields.CharField', [], {'max_length': '4000', 'null': 'True', 'blank': 'True'}),
            'recipe_id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'recipe_lists': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['app.RecipeList']", 'symmetrical': 'False'}),
            'recipe_name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'recipe_notes': ('django.db.models.fields.CharField', [], {'max_length': '4000', 'null': 'True', 'blank': 'True'}),
            'recipe_prep_time': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'recipe_source': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'recipe_total_time': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'recipe_yield': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'tag': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['app.Tag']"}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'default': '0', 'to': u"orm['auth.User']"})
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