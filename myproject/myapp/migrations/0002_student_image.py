# Generated by Django 4.1.5 on 2023-03-31 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='image',
            field=models.ImageField(default='profile_pig.png', upload_to='media'),
        ),
    ]
