# Generated by Django 2.2.3 on 2019-12-10 20:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('tel', models.CharField(max_length=15, primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=50, null=True)),
                ('name', models.CharField(max_length=200, null=True)),
                ('last_name', models.CharField(max_length=200, null=True)),
                ('phone', models.CharField(max_length=15, null=True)),
                ('type', models.IntegerField(default=5)),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event', models.CharField(max_length=100)),
                ('context', models.TextField()),
            ],
        ),
    ]