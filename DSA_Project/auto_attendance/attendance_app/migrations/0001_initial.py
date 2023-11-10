# Generated by Django 4.2.4 on 2023-11-09 15:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('roll_no', models.CharField(max_length=20)),
                ('year', models.CharField(max_length=20)),
                ('department', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='ReferenceFace',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='reference_faces/')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='attendance_app.student')),
            ],
        ),
    ]