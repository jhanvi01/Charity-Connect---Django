# Generated by Django 3.2.5 on 2021-09-16 04:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('NGO', '0003_requirements'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=120)),
                ('lastname', models.CharField(max_length=120)),
                ('phoneno', models.CharField(max_length=120)),
                ('email', models.CharField(max_length=120)),
                ('querry', models.TextField()),
                ('date', models.DateField()),
            ],
        ),
    ]
