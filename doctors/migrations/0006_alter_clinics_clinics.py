# Generated by Django 4.1 on 2022-08-12 08:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctors', '0005_clinics'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clinics',
            name='clinics',
            field=models.CharField(choices=[('M', 'Maweni'), ('B', 'Babtist'), ('U', 'Upendo')], max_length=20, null=True),
        ),
    ]
