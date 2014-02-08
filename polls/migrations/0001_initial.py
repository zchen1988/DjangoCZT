# encoding: utf8
from django.db import models, migrations


class Migration(migrations.Migration):
    
    dependencies = []

    operations = [
        migrations.CreateModel(
            fields = [(u'id', models.AutoField(verbose_name=u'ID', serialize=False, auto_created=True, primary_key=True),), ('question_text', models.CharField(max_length=200),), ('pub_date', models.DateTimeField(verbose_name='date published'),)],
            bases = (models.Model,),
            options = {},
            name = 'Question',
        ),
        migrations.CreateModel(
            fields = [(u'id', models.AutoField(verbose_name=u'ID', serialize=False, auto_created=True, primary_key=True),), ('question', models.ForeignKey(to='polls.Question', to_field=u'id'),), ('choice_text', models.CharField(max_length=200),), ('votes', models.IntegerField(default=0),)],
            bases = (models.Model,),
            options = {},
            name = 'Choice',
        ),
    ]
