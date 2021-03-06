# Generated by Django 2.1.8 on 2019-05-03 21:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('omdbapi', '0002_auto_20190503_1929'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='writer',
            field=models.CharField(blank=True, max_length=1000),
        ),
        migrations.AlterField(
            model_name='rating',
            name='movie',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ratings', to='omdbapi.Movie'),
        ),
    ]
