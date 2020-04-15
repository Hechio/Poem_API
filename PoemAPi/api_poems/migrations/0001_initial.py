# Generated by Django 3.0.5 on 2020-04-15 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Poem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('poem', models.CharField(max_length=1000)),
                ('poet', models.CharField(max_length=100)),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]