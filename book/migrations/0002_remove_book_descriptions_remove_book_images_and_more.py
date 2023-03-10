# Generated by Django 4.1.6 on 2023-02-21 11:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='descriptions',
        ),
        migrations.RemoveField(
            model_name='book',
            name='images',
        ),
        migrations.RemoveField(
            model_name='book',
            name='titles',
        ),
        migrations.AddField(
            model_name='book',
            name='description',
            field=models.TextField(null=True, verbose_name='описание книги'),
        ),
        migrations.AddField(
            model_name='book',
            name='genre',
            field=models.CharField(choices=[('HORROR', 'HORROR'), ('NOVEL', 'NOVEL'), ('FANTASY', 'FANTASY'), ('PSYCHOLOGY', 'PSYCHOLOGY'), ('RELIGION', 'RELIGION')], max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='book',
            name='image',
            field=models.ImageField(null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='book',
            name='price',
            field=models.PositiveIntegerField(null=True, verbose_name='цена'),
        ),
        migrations.AddField(
            model_name='book',
            name='title',
            field=models.CharField(max_length=100, null=True, verbose_name='название книги'),
        ),
        migrations.AddField(
            model_name='book',
            name='video',
            field=models.URLField(null=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='created_dates',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='updated_dates',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
