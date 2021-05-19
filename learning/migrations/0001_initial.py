# Generated by Django 3.2 on 2021-05-19 12:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='カテゴリ名')),
                ('name_en', models.CharField(max_length=10, verbose_name='カテゴリ名英語')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('url', models.URLField(blank=True, null=True, verbose_name='URL')),
                ('title', models.CharField(max_length=50, verbose_name='タイトル')),
                ('subtitle', models.TextField(blank=True, max_length=300, null=True, verbose_name='サブタイトル')),
                ('section', models.CharField(blank=True, max_length=50, null=True, verbose_name='該当箇所')),
                ('content', models.TextField(max_length=1000, verbose_name='本文')),
                ('what', models.TextField(max_length=200, verbose_name='何')),
                ('why', models.TextField(max_length=200, verbose_name='理由')),
                ('sowhat', models.TextField(max_length=200, verbose_name='だから何')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='learning.category')),
            ],
        ),
    ]
