# Generated by Django 2.1.7 on 2019-03-11 04:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookmarks', '0002_bookmark_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookmark',
            name='alt',
            field=models.TextField(default=0),
            preserve_default=False,
        ),
    ]
