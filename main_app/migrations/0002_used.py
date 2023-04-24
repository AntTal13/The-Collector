# Generated by Django 4.2 on 2023-04-24 17:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Used',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('meal', models.CharField(choices=[('P', 'Personal Gain'), ('A', 'Against Avengers'), ('S', 'Showing Off...Again')], default='P', max_length=1)),
                ('stone', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.stone')),
            ],
        ),
    ]
