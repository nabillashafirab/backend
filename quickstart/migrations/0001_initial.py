# Generated by Django 4.2.7 on 2023-11-16 11:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ClassName',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Operator',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('rarity', models.IntegerField(choices=[(1, '1-Star'), (2, '2-Star'), (3, '3-Star'), (4, '4-Star'), (5, '5-Star'), (6, '6-Star')])),
                ('class_name', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='quickstart.classname')),
                ('tags', models.ManyToManyField(related_name='operators', to='quickstart.tag')),
            ],
        ),
    ]
