# Generated by Django 2.2 on 2020-12-13 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_auto_20201213_1943'),
    ]

    operations = [
        migrations.AddField(
            model_name='enduserinfo',
            name='photo',
            field=models.ImageField(blank=True, upload_to=''),
        ),
    ]
