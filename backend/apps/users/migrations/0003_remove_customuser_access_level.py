# Generated by Django 5.1.1 on 2024-10-17 11:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_customuser_access_level_alter_customuser_cpf_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='access_level',
        ),
    ]
