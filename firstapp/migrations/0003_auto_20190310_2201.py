# Generated by Django 2.1.7 on 2019-03-10 20:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0002_pizza'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='pizzashop',
            options={'verbose_name': 'Піццерія', 'verbose_name_plural': 'Піцерії'},
        ),
        migrations.AddField(
            model_name='pizza',
            name='photo',
            field=models.ImageField(blank=True, default='', upload_to='firstapp/photos', verbose_name='Photo'),
        ),
    ]
