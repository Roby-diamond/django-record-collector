# Generated by Django 4.0.2 on 2022-02-18 16:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0005_genre_alter_market_options_alter_market_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='record',
            name='genres',
            field=models.ManyToManyField(to='main_app.Genre'),
        ),
    ]