# Generated by Django 3.2.16 on 2023-10-28 12:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forex', '0045_alter_optiontrade_countdown'),
    ]

    operations = [
        migrations.AlterField(
            model_name='optiontrade',
            name='countdown',
            field=models.CharField(default=0, max_length=10),
        ),
    ]
