# Generated by Django 3.1.6 on 2021-02-07 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webpages', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='slider',
            name='button_link',
            field=models.CharField(default='/contact', max_length=30),
            preserve_default=False,
        ),
    ]
