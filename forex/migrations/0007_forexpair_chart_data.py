# Generated by Django 3.2.16 on 2023-08-21 16:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forex', '0006_remove_forexpair_chart_data'),
    ]

    operations = [
        migrations.AddField(
            model_name='forexpair',
            name='chart_data',
            field=models.TextField(blank=True, null=True),
        ),
    ]