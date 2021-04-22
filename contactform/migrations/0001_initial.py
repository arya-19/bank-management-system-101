# Generated by Django 3.1.5 on 2021-04-11 12:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ContactForm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.CharField(default='-', max_length=50)),
                ('subj', models.CharField(default='-', max_length=50)),
                ('msg', models.TextField(default='-')),
            ],
        ),
    ]
