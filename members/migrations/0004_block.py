# Generated by Django 4.2.5 on 2023-10-14 02:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0003_account_detils'),
    ]

    operations = [
        migrations.CreateModel(
            name='Block',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('index', models.PositiveIntegerField()),
                ('timestamp', models.DateTimeField()),
                ('previous_hash', models.CharField(max_length=64)),
                ('data', models.DecimalField(decimal_places=2, max_digits=10)),
                ('nonce', models.PositiveIntegerField()),
                ('hash', models.CharField(max_length=64)),
            ],
        ),
    ]