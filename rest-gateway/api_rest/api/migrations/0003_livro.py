# Generated by Django 4.1.6 on 2023-06-22 03:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_task_delete_produto'),
    ]

    operations = [
        migrations.CreateModel(
            name='Livro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('author', models.CharField(max_length=255)),
                ('publication_date', models.DateField()),
                ('publisher', models.CharField(max_length=255)),
                ('isbn', models.CharField(max_length=13)),
                ('description', models.TextField()),
                ('cover_image_url', models.URLField()),
            ],
        ),
    ]
