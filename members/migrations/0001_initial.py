# Generated by Django 5.0a1 on 2023-09-29 17:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(blank=True, default='', max_length=250, null=True)),
                ('password', models.CharField(blank=True, default='', max_length=500, null=True)),
                ('email', models.CharField(blank=True, default='', max_length=250, null=True)),
                ('Aadharnumber', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('User_type', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('CreatedBy', models.BooleanField(default=False)),
                ('CreatedDate', models.DateTimeField(null=True)),
                ('UpdatedBy', models.IntegerField(null=True)),
                ('UpdatedDate', models.DateTimeField(null=True)),
                ('DeletedBy', models.IntegerField(null=True)),
                ('DeletedDate', models.DateTimeField(null=True)),
            ],
        ),
    ]