# Generated by Django 4.2.7 on 2024-08-25 16:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_alter_profile_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='fpsweapon',
            old_name='profileWeapon',
            new_name='profile_weapon',
        ),
    ]
