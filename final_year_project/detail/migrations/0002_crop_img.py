# Generated by Django 3.1.2 on 2021-02-12 09:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('detail', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='crop',
            name='img',
            field=models.ImageField(default=2, upload_to='crops'),
            preserve_default=False,
        ),
    ]
