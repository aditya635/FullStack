# Generated by Django 3.2.3 on 2021-06-11 12:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book_outlet', '0006_auto_20210611_1613'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='published_countries',
            field=models.ManyToManyField(null=True, to='book_outlet.Country'),
        ),
    ]
