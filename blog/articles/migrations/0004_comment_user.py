# Generated by Django 2.0.5 on 2018-05-25 11:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0003_auto_20180525_1449'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='user',
            field=models.CharField(default='anonymous', max_length=100),
        ),
    ]