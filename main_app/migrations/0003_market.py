# Generated by Django 4.0.2 on 2022-02-18 15:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_remove_record_genre'),
    ]

    operations = [
        migrations.CreateModel(
            name='Market',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('genre', models.CharField(choices=[('B', 'Bought'), ('S', 'Sold')], default='B', max_length=1)),
                ('record', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.record')),
            ],
        ),
    ]
