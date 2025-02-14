# Generated by Django 5.0 on 2024-05-05 09:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('task', '0005_delete_output_delete_save'),
    ]

    operations = [
        migrations.CreateModel(
            name='Output',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=255, null=True)),
                ('year', models.IntegerField(null=True)),
                ('journal', models.CharField(max_length=255, null=True)),
                ('authors', models.TextField(null=True)),
                ('genre', models.CharField(max_length=255, null=True)),
                ('description', models.TextField(null=True)),
                ('constructs', models.TextField(null=True)),
                ('perspectives', models.TextField(null=True)),
                ('context', models.TextField(null=True)),
                ('study', models.TextField(null=True)),
                ('levels', models.TextField(null=True)),
                ('notes', models.TextField(null=True)),
                ('findings', models.TextField(null=True)),
                ('summary', models.TextField(null=True)),
                ('insights', models.TextField(null=True)),
                ('points', models.TextField(null=True)),
                ('use', models.TextField(null=True)),
                ('additional', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Save',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=255, null=True)),
                ('year', models.IntegerField(null=True)),
                ('journal', models.CharField(max_length=255, null=True)),
                ('authors', models.TextField(null=True)),
                ('genre', models.CharField(max_length=255, null=True)),
                ('description', models.TextField(null=True)),
                ('constructs', models.TextField(null=True)),
                ('perspectives', models.TextField(null=True)),
                ('context', models.TextField(null=True)),
                ('study', models.TextField(null=True)),
                ('levels', models.TextField(null=True)),
                ('notes', models.TextField(null=True)),
                ('findings', models.TextField(null=True)),
                ('summary', models.TextField(null=True)),
                ('insights', models.TextField(null=True)),
                ('points', models.TextField(null=True)),
                ('use', models.TextField(null=True)),
                ('additional', models.TextField(null=True)),
            ],
        ),
    ]
