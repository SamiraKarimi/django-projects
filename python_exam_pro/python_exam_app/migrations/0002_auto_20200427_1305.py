# Generated by Django 2.2.4 on 2020-04-27 18:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('python_exam_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='first_name',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='last_name',
            new_name='user_name',
        ),
        migrations.RemoveField(
            model_name='user',
            name='email',
        ),
        migrations.DeleteModel(
            name='Item',
        ),
    ]