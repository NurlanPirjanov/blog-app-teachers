# Generated by Django 4.1.6 on 2023-04-28 17:40

import ckeditor.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Janaliqqa title jazıń', max_length=255)),
                ('summary', models.CharField(blank=True, max_length=200)),
                ('body', ckeditor.fields.RichTextField()),
                ('video_youtube', models.CharField(blank=True, max_length=255)),
                ('photo', models.ImageField(blank=True, upload_to='images/')),
                ('date', models.DateField(auto_now_add=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Janalıq',
                'verbose_name_plural': 'Janalıqlar',
                'ordering': ['-id'],
            },
        ),
    ]
