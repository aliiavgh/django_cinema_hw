# Generated by Django 4.1.4 on 2022-12-11 17:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='rating',
        ),
        migrations.AddField(
            model_name='rating',
            name='movie',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='movies.movie'),
            preserve_default=False,
        ),
    ]
