# Generated by Django 4.2.6 on 2023-12-09 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='pic',
            field=models.ImageField(blank=True, null=True, upload_to='student_pics'),
        ),
    ]
