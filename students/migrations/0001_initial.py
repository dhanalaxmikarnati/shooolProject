# Generated by Django 4.2.6 on 2023-12-09 08:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('mentors', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('unique_code', models.CharField(max_length=20, unique=True)),
                ('name', models.CharField(max_length=100)),
                ('aadhar', models.CharField(max_length=12)),
                ('pic', models.ImageField(blank=True, null=True, upload_to='student_pics/')),
                ('class_level', models.CharField(max_length=20)),
                ('address', models.TextField()),
                ('section', models.CharField(max_length=10)),
                ('mentor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mentors.mentor')),
            ],
        ),
    ]
