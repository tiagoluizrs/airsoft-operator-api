# Generated by Django 4.2.7 on 2024-08-25 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_alter_profile_patent_alter_profile_team'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.TextField(blank=True, null=True),
        ),
    ]
