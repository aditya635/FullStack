# Generated by Django 3.2.3 on 2021-06-17 10:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image_name',
            field=models.ImageField(null=True, upload_to='posts'),
        ),
    ]
