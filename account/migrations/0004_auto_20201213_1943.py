# Generated by Django 2.2 on 2020-12-13 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_auto_20201213_1724'),
    ]

    operations = [
        migrations.AlterField(
            model_name='enduserprofile',
            name='address',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
