# Generated by Django 2.2.4 on 2020-04-27 22:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('python_exam_app', '0003_trip'),
    ]

    operations = [
        migrations.AddField(
            model_name='trip',
            name='description',
            field=models.CharField(default=2, max_length=255),
            preserve_default=False,
        ),
    ]