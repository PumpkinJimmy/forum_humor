# Generated by Django 3.2 on 2021-11-24 11:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ForumUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('humor', models.IntegerField()),
                ('tag', models.CharField(max_length=30)),
            ],
        ),
    ]