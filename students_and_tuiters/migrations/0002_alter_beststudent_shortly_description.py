# Generated by Django 4.2.1 on 2023-05-22 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students_and_tuiters', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='beststudent',
            name='shortly_description',
            field=models.TextField(max_length=250, verbose_name='qisqacha izoh'),
        ),
    ]
