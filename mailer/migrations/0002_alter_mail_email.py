# Generated by Django 4.2.6 on 2023-11-05 10:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mailer', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mail',
            name='email',
            field=models.EmailField(max_length=254),
        ),
    ]
