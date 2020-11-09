# Generated by Django 3.1.3 on 2020-11-09 07:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contactusform',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('phone_no', models.TextField(max_length=10)),
                ('description', models.TextField(max_length=300)),
            ],
            options={
                'ordering': ('id',),
            },
        ),
    ]