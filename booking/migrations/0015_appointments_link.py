# Generated by Django 4.2.3 on 2023-08-24 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0014_appointments_is_rescheduled'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointments',
            name='link',
            field=models.URLField(null=True),
        ),
    ]
