# Generated by Django 2.2 on 2020-02-27 10:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('C', 'Clothes'), ('Fw', 'Footwear'), ('Te', 'Technology'), ('Ve', 'Vehicles')], default='C', max_length=2),
        ),
        migrations.AddField(
            model_name='product',
            name='label',
            field=models.CharField(choices=[('P', 'primary'), ('S', 'secondary'), ('D', 'danger')], default='P', max_length=1),
        ),
    ]