# Generated by Django 2.2.5 on 2019-10-09 20:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='casting',
            name='pay',
            field=models.IntegerField(null=True),
        ),
    ]
